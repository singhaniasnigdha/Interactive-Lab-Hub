import os
import sys
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

time1 = float('inf')
code, word = "", ""
end_sent = True

while True:  
    if time.time() - time1 > UNIT_TIME * 7 and not end_sent:
        word =  ""
        end_sent = True
    
    if time.time() - time1 > UNIT_TIME * 3 and len(code) > 0:
        word += CODE_TO_LTR.get(code, "")
        print(f"{code} = {word}", file=sys.stderr)
        code = ""
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
