import enum
import os
import signal
import time

import digitalio
import board
import adafruit_rgb_display.st7789 as st7789
import busio
import qwiic_twist
import qwiic_button

from PIL import Image, ImageDraw, ImageFont
from subprocess import call, Popen

cwd = os.getcwd()

def speak(command):
    call(f"espeak -ven -k5 -s150 --stdout '{command}' | aplay", shell=True)
    time.sleep(0.5)

def signal_handler(sig, frame):
    print('Closing Gracefully')
    audio_stream.terminate()
    sys.exit(0)

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

hardware = 'plughw:2,0'
audio_stream = Popen("/usr/bin/cvlc alsa://"+hardware+" --sout='#transcode{vcodec=none,acodec=mp3,ab=256,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/}' --no-sout-all --sout-keep", shell=True)


# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Set up the rotary pin
twist = qwiic_twist.QwiicTwist()
twist.begin()
twist_count = 0
twist.set_blue(255)
twist.set_red(100)
twist.set_green(255)

# Set up buttons
#redButton = qwiic_button.QwiicButton()
#redButton.begin()

#greenButton = qwiic_button.QwiicButton(0x62)
#greenButton.begin()

# Configure screen buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

def image_formatting(image2, width=240, height=135):
    image2 = image2.convert('RGB')
    # Scale the image to the smaller screen dimension
    image2 = image2.resize((width, height), Image.BICUBIC)
    return image2


class Scene(enum.Enum):
    WELCOME = 0
    ARE_YOU_READY = 1
    DIAGON_ALLEY = 2
    BRICK_IMAGE = 3
    OLLIVANDERS = 4
    CHOOSE_WAND = 5
    HOGWARTS_EXPRESS = 6
    BEANS = 7
    SUITCASE = 8
    USE_SPELL = 9
    SORTING_HAT = 10
    CHOOSE_HOUSE = 11
    THANK_YOU = 12

img_dict = {
    Scene.WELCOME: 'welcome_hogwarts.jpeg',
    Scene.ARE_YOU_READY: 'ready.png',
    Scene.DIAGON_ALLEY: 'diagon-alley.png',
    Scene.BRICK_IMAGE: 'puzzle.png',
    Scene.OLLIVANDERS: 'ollivanders.jpg',
    Scene.CHOOSE_WAND: 'wands.jpeg',
    Scene.BEANS: 'beans.png',
    Scene.SUITCASE: '',
    Scene.USE_SPELL: '',
    Scene.SORTING_HAT: '',
    Scene.CHOOSE_HOUSE: '',
    Scene.THANK_YOU: ''
}

houses = ['Gryffinndor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']

screen = Scene.WELCOME

while True:
    display_img = Image.open(f'{cwd}/imgs/{img_dict[screen]}')
    display_img = image_formatting(display_img, width, height)
    disp.image(display_img, rotation)

    if screen == Scene.WELCOME:
        speak(f'We are pleased to inform that you have been admitted to Hogwarts School of Witchcraft and Wizardry!')
        speak(f'Before you join us next week, you are required to complete 5 tasks.')
        next_screen = Scene.ARE_YOU_READY

    if screen == Scene.ARE_YOU_READY:
        speak(f'Are you ready? Say YES or NO. Press the red button to repeat.')
        # TODO Add red button func
        decision = int(input('Enter your choice: '))
        while decision != 1:
            decision = int(input('Press Ctrl-C to exit. Otherwise, enter 1: '))
        next_screen = Scene.DIAGON_ALLEY
        time.sleep(0.1)

    if screen == Scene.DIAGON_ALLEY:
        speak(f'Your first task is to enter Diagon Alley')
        next_screen = Scene.BRICK_IMAGE

    if screen == Scene.BRICK_IMAGE:
        # TODO add puzzle question
        while True:
            decision = input()
            if decision == 1:
                speak(f"Correct! Welcome to Diagon Alley.")
                next_screen = Scene.OLLIVANDERS
                break
            else:
                speak(f"Wrong Answer! Think again!")

    if screen == Scene.OLLIVANDERS:
        speak(f'Task Number 2')
        speak(f'You definitely need a wand before you are off to learn magic!')
        speak(f'Let us find you one.')
        next_screen = Scene.CHOOSE_WAND

    if screen == Scene.CHOOSE_WAND:
        speak(f'Use 3 words to describe yourself!')
        speak(f'This will help Ollivander pick a wand for you.')
        input()
        speak(f"Hmm! Wood from Black Walnut and a Core of Dragon Heartstring, that is perfect for you.")
        
    if screen == Scene.BEANS:
        while True:
            decision = input()
            if decision == 1:
                speak(f"Now, that is an interesting choice!")
                next_screen = Scene.SUITCASE
                break
            else:
                speak(f"Boring Choice! Try something unique.")
    
    if screen == Scene.SUITCASE:
        speak('Welcome to Hogwarts!')
        speak(f'Before you proceed to The Great Hall, you need to get dressed.')
        speak(f'But you forgot the keys to your suitcase at home.')
        speak(f'Try to remember and use the spell to open the lock!')
        next_screen = Scene.USE_SPELL
    
    if screen == Scene.USE_SPELL:
        while True:
            decision = input()
            if decision == 1:
                speak(f"Good Memory! Now get changed quickly! Dinner is about to begin.")
                next_screen = Scene.SORTING_HAT
                break
            else:
                speak(f"Think harder! You can do this.")
    
    if screen == Scene.SORTING_HAT:
        speak(f'Hogwarts has 4 houses.')
        speak(', '.join(houses))
        speak(f'Use the rotating wheel to choose your House.')
        speak(f'Press the wheel to confirm.')
        next_screen = Scene.CHOOSE_HOUSE
    
    if screen == Scene.CHOOSE_HOUSE:
        while not twist.is_pressed():
            choice = houses[twist.count % 4]
            # TODO Add highlighting to house selected
        
        # choice = houses[twist.count % 4]
        speak(f'What are the 2 colors that represent {choice}?')
        time.sleep(1)
        # TODO fix
        if input() == 1:
            speak(f"That is the correct answer!")
            speak(f'You are now part of {choice}.')
            next_screen = Scene.THANK_YOU
        else:
            speak(f"Wrong answer try again.")
        

    if screen == Scene.THANK_YOU:
        time.sleep(0.5)
        speak(f'Thank you for playing!')
        speak(f'Good luck for your future at Hogwarts.')
        time.sleep(2)
        backlight.value = False
        break
    
    time.sleep(0.1)
    screen = next_screen

signal.signal(signal.SIGINT, signal_handler)
