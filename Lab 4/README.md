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

### For lab, we need:

1. Cardboard (start collecting those shipping boxes!)
1. Cutting board
1. Cutting tools
1. Markers

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

### Part A. Capacitive Sensing

We use the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in this experiment. At boot it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes it considers it a user touch. We attach conductive fabric, to build our own [morse code](https://en.wikipedia.org/wiki/Morse_code) interpreter.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/cap_sensor.png" height="240" /></p>

The capacitive sensor board is connected to the raspberry pi using the qwiic connectors. Then alligator clips are used to attach small strips of conductive sheet to 2 nodes (in our case 8 and 10.) In the image above, the yellow clip represents the 'dit' (morse sound for dot) and the black clip is the 'dah' (morse for dash). The code is available at `cap_morse.py`.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/cap_morse.gif" height="420" /></p>

### Part B. OLED screen

We also use the [Adafruit OLED Screens](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples) to display the decoded alphabets/numbers received from the capacitive sensor-based Morse Generator. The code for the same can be found at `oled_morse.py`.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/oled_morse.gif" height="420" /></p>

I use a spoon to touch the conductive sheet, as I realise that the system is more robust when the touch occurs using the spoon than my finger.

### Part C. Paper Display

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>


Make a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**a. Document the design for your paper display.** (e.g. if you had to make it again from scratch, what information would you need?). Include interim iterations (or at least tell us about them).

**b. Make a video of your paper display in action.**

**c. Rationale for the Design.** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

### Part D. Materiality

**Choice of Material**:  Cardboard was used to build the prototype for this device because it is inexpensive, versatile and can be cut, folded, and shaped with at-home equipment. By using an Olfa knife, it is easy to make a box out of a small sheet of cardboard, which is good enough to contain the Raspberry Pi, the T9-keypad (used to input the message), and additional sensors.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/material.png" height="240" /></p>

The capacitive touch sensor, OLED screen and red button are placed on a small sheet of cardboard. Next, a small rectangular box is built to store the Raspberry Pi. Small cutouts are made on the side of this box to allow for a power cord and a 3.5mm audio jack. 

The sheet holding the sensors is taped onto one of the side of the cardboard, such that it is easy to slide the Pi in and out of the device, and/or connect it with other sensors. 

**Other Alternatives**:  As devices of this kind are usually made of metal or plaastic, they were considered to build the prototype. Plastic Sheets were discarded because they are not environment friendly, while cardboard is bio-degradable and easily available at everyone's houses. Metal sheets are also not particularly friendly to the environment, but they are extremely complicated to cut, mold and shape.

### Part E. 'Looks-Like' Prototype

### Part F. 'Works-Like' Prototype

### Part G. 'Acts-Like' Prototype


### Part H. Reflections



Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design.

### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device