# Ph-UI!!!

For lab this week, we focus on the prototyping the physical look and feel of the device. The parts across Lab 1 and Lab 2 have been merged to make the reading more coherent.


## Readings

* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)

* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 

* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 

* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.

* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 

<p align="center">
<img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg" width="240" >
</p>
<p align="center">Dyson Vacuum Cardboard Prototypes</p>

## Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d-materiality) 

E) ['Looks-Like' Prototype](#part-e-looks-like-prototype)

F) ['Works-Like' Prototype](#part-f-works-like-prototype)

G) ['Acts-Like' Prototype](#part-g-acts-like-prototype)

H) [Reflections](#part-h-reflections)


## The Report

We use the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator), [Adafruit OLED Screens](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples), red LED buttons, and the Raspberry Pi in this experiment. We prototype a mini version of our own [morse code](https://en.wikipedia.org/wiki/Morse_code) interpreter, for those who seek to learn about this secretive language.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/morse.png" height="280" /></p>

The device can translate Morse characters (composed of `.` and `-`) to english alphabet and arabic numerals, and vice versa. A button is used to denote the direction of translation. The following sections cover the deliverables for this lab, and the incremental development of the device.
### Part A. Capacitive Sensing

At boot it measures the capacitance on each of the 12 contacts of the capacitive sensor. Whenever that capacitance changes it considers it a user touch. We attach conductive fabric, to 2 nodes of the capacitive touch to translate morse characters to english alphabet and arabic numerals.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/cap_sensor.png" height="240" /></p>

The capacitive sensor board is connected to the raspberry pi using the qwiic connectors. Then alligator clips are used to attach small strips of conductive sheet to 2 nodes (in our case 8 and 10.) In the image above, the yellow clip represents the `dit` (morse sound for dot) and the black clip is the `dah` (morse for dash). The code is available at `cap_morse.py`.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/cap_morse.gif" height="420" /></p>

### Part B. OLED screen

We also use the [Adafruit OLED Screens](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples) to display the decoded alphabets/numbers received from the capacitive sensor-based Morse Generator. The code for the same can be found at `oled_morse.py`.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/oled_morse.gif" height="420" /></p>

I use a spoon to touch the conductive sheet, as I realise that the system is more robust when the touch occurs using the spoon than my finger.

### Part C. Paper Display

The device idea was first prototyped on paper to get an understanding of the components and structure required.
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/paper-proto.png" height="180" /></p>


Things needed to build the paper prototype:
* Cardboard
* Olfa Knife and Cutting Board
* Glue
* Ruler and Markers
* Tape
 
A sheet of cardboard is marked with the following dimensions to create the box which holds the Raspberry Pi. The edges are then glued together to create an open box.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/box.png" height="180" /></p>

To build the numpad, 10 1cm-edge squares are cut to provide a raised platform to simulate the feel of a button. A printout of the T9-keypad is used as stickers on these buttons to guide the user about which letters are associated with which number. Finally, two button in the shape of a circle and rectangle are cut out, to denote the Morse symbols.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/numbers.png" height="240" /></p>

**Rationale for the Design.** A design similar to older mobile phones with a T9 keypad is used as inspiration for this device. Familiarity with using these mobile phones for typing text messages will make it easy for the user to adapt to it. In addition to the T9 keypad, a button in the shape of a circle (representing the Morse `dit`) and another button in the shape of a rectangle (for `dah`) are used to make it intuitive. The objective of this device is to teach a person how to use and understand Morse Code which in itself is challenging. Hence, the device is built in a way that every user feels a sense of familiarity associated with it.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/design.png" height="240" /></p>

It should be small and handy. The dimensions of the device are kept to a minimum to only hold the keypad, screen and the Raspberry Pi. It would have been ideal to have a slimmer device, but the thickness of the Raspberry Pi was a constraint in this regard.

**Interacting with the Paper Display.** A prototype of the prototype is created, which does not have any functionality yet. Following are 2 interactions with this prototype: 1) when the led off, the device converts English text to Morse Code 2) when the red led is on, Morse Code is converted to English. 

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/paper-display.gif" height="480" /></p>

### Part D. Materiality

**Choice of Material**:  Cardboard was used to build the prototype for this device because it is inexpensive, versatile and can be cut, folded, and shaped with at-home equipment. By using an Olfa knife, it is easy to make a box out of a small sheet of cardboard, which is good enough to contain the Raspberry Pi, the T9-keypad (used to input the message), and additional sensors.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/material.png" height="240" /></p>

The capacitive touch sensor, OLED screen and red button are placed on a small sheet of cardboard. Next, a small rectangular box is built to store the Raspberry Pi. Small cutouts are made on the side of this box to allow for a power cord and a 3.5mm audio jack. 

The sheet holding the sensors is taped onto one of the side of the cardboard, such that it is easy to slide the Pi in and out of the device, and/or connect it with other sensors. 

**Other Alternatives**:  As devices of this kind are usually made of metal or plaastic, they were considered to build the prototype. Plastic Sheets were discarded because they are not environment friendly, while cardboard is bio-degradable and easily available at everyone's houses. Metal sheets are also not particularly friendly to the environment, but they are extremely complicated to cut, mold and shape.

### Part E. 'Looks-Like' Prototype 
Different angles of the final physical prototype is shown in the image below. 

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/looks-like.png" height="280" /></p>

The top-view show the final appearance of the Morse Decoder, after which we see how the box contains the Raspberry Pi. This makes it easy to open the circuit work on the Pi and easily put it back in the box. As mentioned before, the box is made as small as possible to make the device easy to carry around. The third image indicates how easy it is to connect a power supply to the device. (Ofcourse, we would like the actual device to be wireless!!) The last image shows the device operational.

### Part F. 'Works-Like' Prototype
(show us what the device can do)

Sensors/Devices used for making this prototype include: 
* Raspberry Pi, 
* OLED Display
* Red LED Button
* Capacitive Touch Sensor
* Conductive Tape

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/schematic.png" height="280" /></p>

This device has 2 modes:
1. Translating English Letters to Morse Symbols: When the red LED is off, the user is in this mode. This is the first stage of learning, where the user inputs letter using the T9-keypad and their corresponding Morse Code appear on the screen.
1. Translating Morse Characters to Alphabets/Arabic Numbers: This mode is in play when the red LED is on. Once the user is more familiar with the Morse Code, they can use the buttons below the OLED display, i.e., the dot and dash to input a code in Morse language. The device will then translate their code to English letters.

The user can toggle between modes by pressing the red LED button. The code for this experiment can be found at `morse.py`. The demo of the device in action can be seen in the next section.

### Part G. 'Acts-Like' Prototype
This device is catered to users who want to learn Morse Code. This can be depicted using the storyboard below:
(videos/storyboards/other means of showing how a person would interact with the device)

### Part H. Reflections
This assignment emphasizes on the value of interactive device design in addition to its functionality. It is important the user finds it intuitive to use the device. Building a working prototype required a lot of strategizing and several iterations. 

Some things that could have been better are:
* **Neater design** - First experience with cardboard prototyping, hence the edges are not as clean as they could have been. The conductive tape is visible, which is not pleasant to the eye.
* **Capacitive Touch Sensor** - The sensor used for prototyping this experiment is not very robust. It misses several touches and also counts them multiple times on some occassions. The device would work more effectively if the sensors could detect every capacitive change more accurately.
* **Bigger Screen** - The words coded/encoded using Morse had to be restricted to a few letters due the dimension constraints of the screen, which is less than 3cm in length. It would have been interesting to explore coding/encoding sentences.

Some things I wanted to add:
* Light and Sound to convey the Morse Code, instead of characters. However, this device is presented as a starter to those who wish to learn to read and deciper Morse Code.