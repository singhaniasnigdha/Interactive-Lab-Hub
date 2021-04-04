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
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Set up button
redButton = qwiic_button.QwiicButton()
redButton.begin()

# start with a blank screen
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

time1 = float('inf')
num_code, word = "", ""
prev_code, code = "", ""
end_sent = True

convert_to_alpha = True

def check_button(redButton):
    should_terminate = False
    while not should_terminate:
        if redButton.is_button_pressed():
            convert_to_alpha = not convert_to_alpha
            if convert_to_alpha:
                redButton.LED_on(255)
            else:
                redButton.LED_off()

def alpha_to_morse(num_code, word, code, time1, end_sent, oled):
    if time.time() - time1 > UNIT_TIME * 7 and not end_sent:
        end_sent = True
        # undraw the previous code
        draw.text((0, 10), word, font=font2, fill=0)
        draw.text((40, 10), code, font=font2, fill=0)
        word, code = "", ""
    
    if time.time() - time1 > UNIT_TIME and len(num_code) > 0:
        # undraw the previous code
        draw.text((0, 10), word, font=font2, fill=0)
        draw.text((40, 10), code, font=font2, fill=0)
        
        # Draw the current code
        word += T9_INPUT[int(num_code)]
        code += " " + LTR_TO_CODE[word[-1]]
        draw.text((0, 10), word, font=font2, fill=255)
        draw.text((40, 10), code, font=font2, fill=255)
        
        # Display image
        oled.image(image)
        oled.show()

        num_code = ""
        end_sent = False
    
    for cap, num in CAP_TO_NUM.items():
        if mpr121[cap].value:
            num_code += str(num)
            time1 = time.time()

    return num_code, word, code, time1, end_sent, oled

def morse_to_alpha(code, prev_code, time1, end_sent, oled):
    if time.time() - time1 > UNIT_TIME * 7 and not end_sent:
        end_sent = True
    
    if time.time() - time1 > UNIT_TIME * 3 and len(code) > 0:
        # undraw the previous code
        draw.text((0, 10), prev_code, font=font2, fill=0)
        draw.text((40, 10), CODE_TO_LTR.get(prev_code, ""), font=font2, fill=0)
        # Draw the current code
        draw.text((0, 10), code, font=font2, fill=255)
        draw.text((40, 10), CODE_TO_LTR.get(code, ""), font=font2, fill=255)
        # Display image
        oled.image(image)
        oled.show()

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
    return code, prev_code, time1, end_sent, oled

while True:
    check_button(redButton)
    
    if convert_to_alpha:
        code, prev_code, time1, end_sent, oled = morse_to_alpha(code, prev_code, time1, end_sent, oled)  
    else:
        num_code, word, code, time1, end_sent, oled = alpha_to_morse(num_code, word, code, time1, end_sent, oled)
    
    time.sleep(UNIT_TIME/8)
