# The Clock of Pi

Does it feel like time is moving strangely during the pandemic?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

### Acknowledgements
Sam Lee (snl48) and I worked together for this lab.  

### Raspberry Pi and Other Inventory
The inventory available for this lab is compiled at [Inventory List](partslist.md).

## Overview
Activities for this assignment are:

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## Part A. 
## Connect to your Pi

As preparation for this lab, we burn our Pi Image onto the SD card, and connect the Pi to our wifi. This allows us to SSH into the Pi using our devices on the same network. The detailed preparations can be found [here](prep-work/prep.md) 

The following allow us to connect to our Raspberry Pi 4, install, create and activate our python virtual environment.
```
ssh pi@ixe00
pi@ixe00:~ $ pip3 install virtualenv
pi@ixe00:~ $ virtualenv circuitpython
pi@ixe00:~ $ source circuitpython/bin/activate
(circuitpython) pi@ixe00:~ $ 

```

After setting up the virtual environment, we clone this repository for the assignment:
```
(circuitpython) pi@ixe00:~$ git clone https://github.com/singhaniasnigdha/Interactive-Lab-Hub.git
(circuitpython) pi@ixe00:~$ cd Interactive-Lab-Hub/Lab\ 2/
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub $ 
```

Next, install all the packages required for the this lab. All the packages are available at [requirements.txt](prep-work/requirements.txt).
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub $ pip install -r requirements.txt
```

## Part B. 
### Try out the Command Line Clock

We run the example [cli_clock.py](cli_clock.py) to test our device. 
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py 
02/24/2021 11:20:49
```

The time appears as output on the terminal, which is updated every second. The screenshot below shows the result from running this script.

*** Insert image/gif ***


## Part C. 
## Set up your RGB Display
The [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) display is added to the Raspberry Pi, and we use Python to control the contents on this display.

<p align="center"><img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" /></p>

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p align="center">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

#### Testing the Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

We test the screen by running our [screen_test.py](screen_test.py).
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python screen_test.py
```

The prompt asks the user to enter the name of a color, then press either of the buttons. The images below show the output from this script.

![](imgs/cli_clock.gif)

#### Displaying an image

[image.py](image.py) contains an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?


#### Displaying Info
You can look in `stats.py` for how to display text on the screen



## Part D. 
## Set up the Display Clock Demo

In `screen_clock.py`. Show the time by filling in the while loop. You can use the code in `cli_clock.py` and `stats.py` to figure this out.


## Part E.
## Modify the barebones clock to make it your own

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.


## Part F. 
## Make a short video of your modified barebones PiClock

**Take a video of your PiClock.**

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.



