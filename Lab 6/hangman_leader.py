import os
import time
import subprocess
import uuid

import adafruit_ssd1306
import board
import busio
import digitalio
import qwiic_button
import qwiic_twist

import paho.mqtt.client as mqtt
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

player_topic = 'IDD/hangman_player'
leader_topic = 'IDD/hangman_leader'


def show_word_oled(oled_obj, word, color=255):
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    
    oled_obj['draw'].text((0, 10), word, font=font, fill=color)
    oled_obj['oled'].image(oled_obj['image'])
    oled_obj['oled'].show()

def get_word_length(rot_encoder, disp_obj, max_len=12):
    rot_encoder.set_count(0); rot_encoder.set_red(150)
    prev_choice = None
    while not rot_encoder.is_pressed():
        choice = rot_encoder.count % max_len
        if prev_choice != choice:
            show_word_oled(disp_obj, f'Enter Word Length: {prev_choice}', color=0)
            show_word_oled(disp_obj, f'Enter Word Length: {choice}')
            prev_choice = choice
        time.sleep(0.5)
    rot_encoder.set_red(0)
    return choice

def get_word_pos(rot_encoder, disp_obj, max_len=12):
    padding = 2
    shape_width = 3
    top = padding
    bottom = 32-padding
    
    def draw_rectangle(start_pos, outline_color=255):
        if start_pos is None:
            return
        x = start_pos * 2 * shape_width
        disp_obj['draw'].rectangle((x, top, x+shape_width, bottom), outline=outline_color, fill=0)
        disp_obj['oled'].image(disp_obj['image'])
        disp_obj['oled'].show()
    
    rot_encoder.set_count(0); rot_encoder.set_red(150)
    prev_pos = None
    while not rot_encoder.is_pressed():
        curr_pos = rot_encoder.count % max_len
        if prev_pos != curr_pos:
            draw_rectangle(prev_pos, outline_color=0)
            draw_rectangle(curr_pos)
            prev_pos = curr_pos
        time.sleep(0.5)
    
    rot_encoder.set_red(0)
    draw_rectangle(prev_pos, outline_color=0)
    return curr_pos

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
    is_green = green.is_button_pressed()
    if is_green:
        red.LED_off(); green.LED_on(255)
    else:
        red.LED_on(255); green.LED_off()
    return is_green

def get_mqtt_client(on_message):
    def on_connect(client, userdata, flags, rc):
        print(f"connected with result code {rc}")
        client.subscribe(leader_topic)

    client = mqtt.Client(str(uuid.uuid1()))
    client.tls_set()
    client.username_pw_set('idd', 'device@theFarm')

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect('farlab.infosci.cornell.edu', port=8883)
    return client

def on_player_message(client, userdata, msg):
    selected_char = msg.payload.decode('UTF-8')
    print(f"topic: {msg.topic} msg: {selected_char}")

    global hangman_pos, word
    is_correct_guess = blink_button(redButton, greenButton)
    if is_correct_guess:
        word_pos = get_word_pos(twist, oled_obj, max_len=word_len)
        show_word_oled(oled_obj, ' '.join(list(word)), color=0)
        word = word[:word_pos] + selected_char + word[word_pos+1:]
        greenButton.LED_off()
    else:
        hangman_pos += 1
        redButton.LED_off()
    client.publish(player_topic, f"{word},{hangman_pos},{is_correct_guess},{None}")

show_hangman_tft('welcome.png', disp)
client = get_mqtt_client(on_player_message)

while True:
    if word_len == 0:
        word_len = get_word_length(twist, oled_obj)
        word = "_" * word_len
        show_word_oled(oled_obj, f'Enter Word Length: {word_len}', color=0)
        # Send message to player
        client.publish(player_topic, f"{word},{hangman_pos},{None},{True}")
        
    else: 
        client.loop()
        show_word_oled(oled_obj, ' '.join(list(word)))
        show_hangman_tft(f'hangman-{hangman_pos}.png', disp)
        
        if hangman_pos == 6:
            show_hangman_tft("lose.png", disp)
            time.sleep(5)
            redButton.LED_off()
            break
        if '_' not in word:
            show_hangman_tft("win.gif", disp)
            time.sleep(5)
            greenButton.LED_off()
            break

