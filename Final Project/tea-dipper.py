import digitalio
import board
import busio
import qwiic_button
import qwiic_twist

import os
import time

import RPi.GPIO as GPIO
import adafruit_rgb_display.st7789 as st7789

from PIL import Image, ImageDraw, ImageFont

cwd = os.getcwd()
i2c = busio.I2C(board.SCL, board.SDA)

MOTOR_PIN = 18

def image_formatting(img):
    img = img.convert('RGB')
    # Scale the image to the smaller screen dimension
    img = img.resize((240, 135), Image.BICUBIC)
    return img

def setup():
    # Setup the servo
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTOR_PIN, GPIO.OUT)
    servo = GPIO.PWM(MOTOR_PIN, 50)
    servo.start(100 / 18 + 2)

    # Setup SPI bus using hardware SPI:
    spi = board.SPI()

    # Create the ST7789 display:
    disp = st7789.ST7789(
        spi,
        cs=digitalio.DigitalInOut(board.CE0),
        dc=digitalio.DigitalInOut(board.D25),
        rst=None,
        baudrate=64000000,
        width=135,
        height=240,
        x_offset=53,
        y_offset=40,
    )

    # Set up the rotary pin
    twist = qwiic_twist.QwiicTwist()
    twist.begin()
    twist.set_blue(150)
    twist.set_red(0)
    twist.set_green(0)

    # Set up buttons
    redButton = qwiic_button.QwiicButton()
    redButton.begin()
    greenButton = qwiic_button.QwiicButton(address=0x62)
    greenButton.begin()

    # Alternatively load a TTF font.  Make sure the .ttf font file is in the
    # same directory as the python script!
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)

    # Turn on the backlight
    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True

    return servo, disp, twist, redButton, greenButton, font

def show_image(disp, filename, rotation=90):
    image = Image.open(f'{cwd}/img/{filename}')
    image = image_formatting(image)
    disp.image(image, rotation)

def show_selected_time(disp, selected_time):
    show_image(disp, f'{selected_time}-time.png')

def choose_dip_time(rot_encoder, default_dip_time, max_time=5):
    prev_choice = default_dip_time
    show_selected_time(disp, default_dip_time)
    time.sleep(0.5)

    rot_encoder.set_count(2); rot_encoder.set_red(150)
    while not rot_encoder.is_pressed():
        choice = (rot_encoder.count % max_time) + 1
        if prev_choice != choice:
            show_selected_time(disp, choice)
            prev_choice = choice
        time.sleep(0.5)
    rot_encoder.set_red(0)
    return choice

servo, disp, twist, redButton, greenButton, font = setup()
default_dip_time, start_dip = 3, False
dip_time = default_dip_time

while True:
    if start_dip:
        start_time = time.time()
        redButton.LED_on(255)
        while time.time() - start_time < (dip_time * 60):
            servo.ChangeDutyCycle(80 / 18 + 2)
            time.sleep(1.5)
            servo.ChangeDutyCycle(100 / 18 + 2)
            time.sleep(1.5)
            
            if redButton.is_button_pressed():
                break
        # TODO: speaker says tea is ready
        redButton.LED_off()
        start_dip = False
    
    show_image(disp, 'tea-time.jpg')
    time.sleep(3)

    # Choose Dip Time
    dip_time = choose_dip_time(twist, default_dip_time, max_time=5)
    show_image(disp, 'start.png')
    # Blink Button to ask user to press when to begin
    while not greenButton.is_button_pressed():
        greenButton.LED_on(255)
        time.sleep(0.5)
        greenButton.LED_off()
        time.sleep(0.5)
    
    start_dip = True