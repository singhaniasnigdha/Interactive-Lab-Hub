import os
import sys
import time

import board
import busio
import adafruit_mpr121

code=""
word=" "

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

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

time1 = float('inf')

def check_letter_break(word, code):
    if time.time() - time1 > UNIT_TIME * 3:
        word += CODE_TO_LTR.get(code, "")
        print(word, file=sys.stderr)
        code = ""
    return word, code

def check_word_break(word, code):
    if time.time() - time1 > UNIT_TIME * 7:
        word += CODE_TO_LTR.get(code, "") + " "
        print(word, file=sys.stderr)
        code = ""
    return word, code

while True:
    word, code = check_letter_break(word, code)
    word, code = check_word_break(word, code)
    
    if mpr121[8].value:

        code = code + '.'
        print(".", end="", file=sys.stderr)
        os.system('mpg123 sounds/dit.mp3 &')
        time1 = time.time()
    
    if mpr121[10].value:
        code = code + '-'
        print("-", end="", file=sys.stderr)
        os.system('mpg123 sounds/dah.mp3 &')
        time1 = time.time()
        time.sleep(UNIT_TIME * 2)

    
    time.sleep(UNIT_TIME)
