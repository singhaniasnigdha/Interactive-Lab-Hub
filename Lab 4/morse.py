import os
import sys
import time

import board
import busio
import adafruit_mpr121
import adafruit_ssd1306
import qwiic_button

from PIL import Image, ImageDraw, ImageFont

LTR_TO_CODE = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', 
                    '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}

CODE_TO_LTR = {v: k for k, v in LTR_TO_CODE.items()}

T9_INPUT = {
    2: 'A', 22: 'B', 222: 'C',
    3: 'D', 33: 'E', 333: 'F',
    4: 'G', 44: 'H', 444: 'I', 
    5: 'J', 55: 'K', 555: 'L', 
    6: 'M', 66: 'N', 666: 'O', 
    7: 'P', 77: 'Q', 777: 'R', 7777: 'S',
    8: 'T', 88: 'U', 888: 'V', 
    9: 'W', 99: 'X', 999: 'Y', 9999: 'Z'
}

CAP_TO_NUM = {
    1: 7, 2: 5, 3: 4, 7: 2, 8: 3, 9: 6, 10: 9, 11: 8
}

UNIT_TIME = 1

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.
oled_obj = {
    'oled': adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
}

# Set up button
redButton = qwiic_button.QwiicButton()
redButton.begin()
redButton.LED_on(255)

# start with a blank screen
oled_obj['oled'].fill(0)
oled_obj['oled'].show()

# Create blank image for drawing
oled_obj['image'] = Image.new("1", (oled_obj['oled'].width, oled_obj['oled'].height))
oled_obj['draw'] = ImageDraw.Draw(oled_obj['image'])

time1 = float('inf')
num_code, word = "", ""
prev_code, code = "", ""
end_sent = True

convert_to_alpha = True

def show_image(word1, word2, oled_obj, color=255):
    oled_obj['draw'].text((0, 10), word1, font=font2, fill=color)
    oled_obj['draw'].text((50, 10), word2, font=font2, fill=color)
    # Display image
    oled_obj['oled'].image(oled_obj['image'])
    oled_obj['oled'].show()

def check_button(redButton, convert_to_alpha, prev_code, word, code, num_code, oled_obj):
    if redButton.is_button_pressed():
        print(f"Old Mode: {convert_to_alpha}")
        convert_to_alpha = not convert_to_alpha
        print(f"New Mode: {convert_to_alpha}")
        
        if convert_to_alpha:
            # undraw the previous code
            show_image(word, code, oled_obj, color=0)
            redButton.LED_on(255)
        else:
            # undraw the previous code
            show_image(prev_code, CODE_TO_LTR.get(prev_code, ""), oled_obj, color=0)
            redButton.LED_off()
        time.sleep(1)
        
        num_code, code, word = "", "", ""
    
    return num_code, code, word, convert_to_alpha

def alpha_to_morse(num_code, word, code, time1, end_sent, oled_obj):
    if time.time() - time1 > UNIT_TIME * 7 and not end_sent:
        end_sent = True
        # undraw the previous code
        # show_image(word, code, oled_obj, color=0)
        word, code = "", ""
    
    if time.time() - time1 > UNIT_TIME and len(num_code) > 0:
        # undraw the previous code
        show_image(word, code, oled_obj, color=0)
        
        # Draw the current code
        word += T9_INPUT[int(num_code)]
        code += " " + LTR_TO_CODE[word[-1]]
        show_image(word, code, oled_obj)

        num_code = ""
        end_sent = False
    
    for cap, num in CAP_TO_NUM.items():
        if mpr121[cap].value:
            num_code += str(num)
            time1 = time.time()

    return num_code, word, code, time1, end_sent

def morse_to_alpha(code, prev_code, time1, end_sent, oled_obj):
    if time.time() - time1 > UNIT_TIME * 7 and not end_sent:
        end_sent = True
    
    if time.time() - time1 > UNIT_TIME * 3 and len(code) > 0:
        # undraw the previous code
        show_image(prev_code, CODE_TO_LTR.get(prev_code, ""), oled_obj, color=0)
        # Draw the current code
        show_image(code, CODE_TO_LTR.get(code, ""), oled_obj)

        prev_code, code = code, ""
        end_sent = False
    
    if mpr121[5].value:
        code = code + '.'
        # os.system('mpg123 sounds/dit.mp3 &')
        time1 = time.time()
    
    if mpr121[6].value:
        code = code + '-'
        # os.system('mpg123 sounds/dah.mp3 &')
        time1 = time.time()
    return code, prev_code, time1, end_sent

while True:
    num_code, code, word, convert_to_alpha = check_button(redButton, convert_to_alpha, prev_code, word, code, num_code, oled_obj)
    
    if convert_to_alpha:
        code, prev_code, time1, end_sent = morse_to_alpha(code, prev_code, time1, end_sent, oled_obj)  
    else:
        num_code, word, code, time1, end_sent = alpha_to_morse(num_code, word, code, time1, end_sent, oled_obj)
    
    time.sleep(UNIT_TIME/8)
