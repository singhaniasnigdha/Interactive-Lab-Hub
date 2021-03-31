import os
import sys
import time

import board
import busio
import adafruit_mpr121
import adafruit_ssd1306

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

UNIT_TIME = 1

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# start with a blank screen
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

def clear_screen(oled):
    oled.fill(0)
    oled.show()
    return ImageDraw.Draw(image)


time1 = float('inf')
prev_code, code = "", ""
end_sent = True

while True:  
    if time.time() - time1 > UNIT_TIME * 7 and not end_sent:
        end_sent = True
        clear_screen(oled)
    
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
    
    if mpr121[8].value:
        code = code + '.'
        # os.system('mpg123 sounds/dit.mp3 &')
        time1 = time.time()
    
    if mpr121[10].value:
        code = code + '-'
        # os.system('mpg123 sounds/dah.mp3 &')
        time1 = time.time()

    time.sleep(UNIT_TIME/4)
