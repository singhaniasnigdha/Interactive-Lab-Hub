import time
import os
import subprocess
import board
import busio
import adafruit_mpr121
import adafruit_ssd1306
import paho.mqtt.client as mqtt
import uuid
import digitalio

import adafruit_rgb_display.st7789 as st7789

from PIL import Image, ImageDraw, ImageFont

cwd = os.getcwd()
i2c = busio.I2C(board.SCL, board.SDA)

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

mprA = adafruit_mpr121.MPR121(i2c, address=0x5a)
mprB = adafruit_mpr121.MPR121(i2c, address=0x5b)

addr_map = {'A': {0: 'K',
                 1: 'S',
                 2: 'Y',
                 3: 'L',
                 4: 'C',
                 5: 'D',
                 6: 'A',
                 7: 'I',
                 8: 'R',
                 9: 'B',
                 10: 'Q',
                 11: 'J'},
            'B': {0: 'W',
                 1: 'V',
                 2: 'P',
                 3: 'H',
                 4: 'O',
                 5: 'G',
                 6: 'E',
                 7: 'M',
                 8: 'F',
                 9: 'T',
                 10: 'U',
                 11: 'N'}}

read_topic = 'IDD/hangman_player'
send_topic = 'IDD/hangman_leader'

# from the reader.py example
def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(read_topic)

prev_state = 'hangman-0.png'
waiting = True

# also from reader.py example
def on_message(client, userdata, msg):
    message = msg.payload.decode('UTF-8')
    print(f"topic: {msg.topic} msg: {message}")
    word, hangman_state, success_flag, start_flag = message.split(',')

    if start_flag == 'True':
        global waiting
        waiting = False
        show_word_oled(oled_obj, word)
        return

    if success_flag == 'True':
        show_hangman_tft(f'correct_letter.png', disp)
        time.sleep(2)
    else:
        show_hangman_tft(f'wrong_letter.png', disp)
        time.sleep(2)

    show_word_oled(oled_obj, word)
    show_hangman_tft(f'hangman-{hangman_state}.png', disp)
    global prev_state
    prev_state = f'hangman-{hangman_state}.png'

    if hangman_pos == 6:
        show_hangman_tft(f'lost.gif', disp)
        time.sleep(5)
    if '_' not in word:
        show_hangman_tft(f'win.gif', disp)
        time.sleep(5)

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.on_connect = on_connect
client.on_message = on_message

client.connect('farlab.infosci.cornell.edu', port=8883)

show_hangman_tft('welcome.png', disp)
while waiting:
    client.loop()
    time.sleep(1)

show_hangman_tft(prev_state, disp)

while True:
    client.loop()
    letter = ''
    for i in range(12):
        if mprA[i].value and mprA[i].raw_value < 200:
            print(addr_map['A'][i])
            letter = addr_map['A'][i]
        if mprB[i].value and mprB[i].raw_value < 200:
            print(addr_map['B'][i])
            letter = addr_map['B'][i]
    if letter != '':
        client.publish(send_topic, letter)
        show_hangman_tft(f'guess_{letter}.png', disp)
        time.sleep(5)
        show_hangman_tft(prev_state, disp)
    mprA.reset()
    mprB.reset()
    time.sleep(0.25)