# Ph-UI!!!

For lab this week, we focus on the prototyping the physical look and feel of the device.


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

E) [Record the interaction](#part-e-record-the-interactions)

F) ['Looks-Like' Prototype](#part-f-looks-like-prototype)

G) ['Works-Like' Prototype](#part-g-works-like-prototype)

H) ['Acts-Like' Prototype](#part-h-acts-like-prototype)

I) [Reflections](#part-i-reflections)



## The Report

### Part A Capacitive Sensing

We use the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in this experiment. At boot it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes it considers it a user touch. We attach conductive fabric, to build our own [morse code](https://en.wikipedia.org/wiki/Morse_code) interpreter.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/cap_sensor.png" height="240" /></p>

The capacitive sensor board is connected to the raspberry pi using the qwiic connectors. Then alligator clips are used to attach small strips of conductive sheet to 2 nodes (in our case 8 and 10.) In the image above, the yellow clip represents the 'dit' (morse sound for dot) and the black clip is the 'dah' (morse for dash). The code is available at `cap_morse.py`.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/cap_morse.gif" height="420" /></p>

### Part B OLED screen

We also use the [Adafruit OLED Screens](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples) to display the decoded alphabets/numbers received from the capacitive sensor-based Morse Generator. The code for the same can be found at `oled_morse.py`.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/oled_morse.gif" height="420" /></p>

I use a spoon to touch the conductive sheet, as I realise that the system is more robust when the touch occurs using the spoon than my finger.

### Part C Paper Display

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

It holds a pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>


Make a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**a. Document the design for your paper display.** (e.g. if you had to make it again from scratch, what information would you need?). Include interim iterations (or at least tell us about them).

**b. Make a video of your paper display in action.**

**c. Explain the rationale for the design.** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

### Part D Materiality

**Open Ended**: We are putting very few constraints on this part but we want you to get creative.

Design a system with the Pi and anything from your kit with a focus on form, and materiality. The "stuff" that enclose the system should be informed by the desired interaction. What would a computer made of rocks be like? How would an ipod made of grass behave? Would a roomba made of gold clean your floor any differently?

**a. document the material prototype.** Include candidates that were considered even if they were set aside later.

**b. explain the selection.**

### Part E Record Interactions

### Part 2.

### Part F 'Looks-Like' Prototype

### Part G 'Works-Like' Prototype

### Part H 'Acts-Like' Prototype

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design.

Reiterating:
### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device



### Part I Reflections