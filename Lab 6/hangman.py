import os
import time
import subprocess

import adafruit_mpr121
import adafruit_ssd1306
import digitalio
import board
import busio
import qwiic_twist
import qwiic_button

import adafruit_rgb_display.st7789 as st7789

from PIL import Image, ImageDraw, ImageFont

cwd = os.getcwd()

# Create the ST7789 display:
disp = st7789.ST7789(
    board.SPI(),
    cs=digitalio.DigitalInOut(board.CE0),
    dc=digitalio.DigitalInOut(board.D25),
    rst=None,
    baudrate=64000000,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Set up the rotary pin
twist = qwiic_twist.QwiicTwist()
twist.begin()
twist_count = 0
twist.set_blue(150)
twist.set_red(0)
twist.set_green(0)

# Set up buttons
redButton = qwiic_button.QwiicButton()
redButton.begin()

greenButton = qwiic_button.QwiicButton(address=0x62)
greenButton.begin()

# Set up Capacitive Touch Sensor
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.
oled_obj = {
    'oled': adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
}
# start with a blank screen
oled_obj['oled'].fill(0)
oled_obj['oled'].show()

# Create blank image for drawing
oled_obj['image'] = Image.new("1", (oled_obj['oled'].width, oled_obj['oled'].height))
oled_obj['draw'] = ImageDraw.Draw(oled_obj['image'])

# Initialise hangman
hangman_pos = 0
word, word_len = '', 0

def get_word_length(rot_encoder, max_len=10):
    rot_encoder.set_count(0)
    while not rot_encoder.is_pressed():
        choice = rot_encoder.count % max_len
        # TODO show choice on TFT
        time.sleep(0.2)
    return choice

def show_word_oled(oled_obj, word, color=255):
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    
    oled_obj['draw'].text((0, 10), word, font=font, fill=color)
    # Display image
    oled_obj['oled'].image(oled_obj['image'])
    oled_obj['oled'].show()

def show_hangman_tft(img_title, tft_obj):
    hangman_img = Image.open(f"{cwd}/imgs/{img_title}")
    hangman_img = hangman_img.convert('RGB').resize((135, 240), Image.BICUBIC)
    tft_obj.image(hangman_img, 0)
    time.sleep(0.5)

def blink_button(red, green):
    while not (red.is_button_pressed() or green.is_button_pressed()):
        red.LED_on(255); green.LED_on(255)
        time.sleep(0.5)
        red.LED_off(); green.LED_off()
        time.sleep(0.5)
    return green.is_button_pressed()

while True:
    if word_len == 0:
        # Ask leader to Enter Word Length
        word_len = get_word_length(twist)
        word = "_" * word_len
    else:
        show_word_oled(oled_obj, word)
        show_hangman_tft(f'hangman-{hangman_pos}.png', disp)
        
        if hangman_pos == 6:
            show_hangman_tft(f'lost.gif', disp)
            time.sleep(5)
            redButton.LED_off()
            break
        if '_' not in word:
            show_hangman_tft(f'win.gif', disp)
            time.sleep(5)
            greenButton.LED_off()
            break

        redButton.LED_off(); greenButton.LED_off()
        
        # TODO @Sam -- ask player to enter letter
        selected_char = 'A'

        is_correct_guess = blink_button(redButton, greenButton)
        if is_correct_guess:
            # TODO -- show highlight
            word_pos = get_word_length(twist, max_len=word_len)
            show_word_oled(oled_obj, word, color=0)
            word = word[:word_pos] + selected_char + word[word_pos+1:]
        else:
            hangman_pos += 1
        