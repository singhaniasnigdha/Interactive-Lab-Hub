import os
import time

import board
import busio
import adafruit_mpr121

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

time1 = time.time()
code, words = '', ''

def check_letter_break():
    if time.time() - time1 > UNIT_TIME * 3:
        words = f'{words}{CODE_TO_LTR.get(code, "")}  '
        print(words)
        code = ''
        print(' ', end='')

def check_word_break():
    if time.time() - time1 > UNIT_TIME * 7:
        words = f'{words}{CODE_TO_LTR.get(code, "")}  '
        print(words)
        code = ''
        print('\t', end='')

while True:
    if mpr121[8].value:
        check_letter_break()
        check_word_break()

        code = code + '.'
        print(".", end="")
        os.system('mpg123 dit.mp3 &')
        time1 = time.time()
        time.sleep(UNIT_TIME)
    
    if mpr121[10].value:
        check_letter_break()
        check_word_break()

        code = code + '-'
        print("-", end="")
        os.system('mpg123 dah.mp3 &')
        time1 = time.time()
        time.sleep(UNIT_TIME * 3)