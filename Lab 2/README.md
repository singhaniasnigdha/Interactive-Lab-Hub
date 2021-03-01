# The Clock of Pi

Does it feel like time is moving strangely during the pandemic?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

### Acknowledgements
Sam Lee (snl48) and I worked together for this lab. We iteratively built on what we wanted as the final product and executed it together.

### Raspberry Pi and Other Inventory
The inventory available for this lab is compiled at [Inventory List](partslist.md).

## Overview
Activities for this assignment are:

A) [Connect to your Pi](#part-a-connecting-to-raspberry-pi)  

B) [Command Line Clock](#part-b-command-line-clock) 

C) [Set up RGB display](#part-c-set-up-rgb-display)

D) [Try out clock_display_demo](#part-d-set-up-the-display-clock) 

E) [Building a barebones clock](#part-e-building-a-barebones-clock)

F) [Short video of the barebones PiClock](#part-f-short-video-of-the-barebones-piclock)

G) [Planning further interactions/features for the PiClock](#part-g-planning-further-interactionsfeatures-for-the-piclock)

## Part A. Connecting to Raspberry Pi

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

## Part B. Command Line Clock

We run the example [cli_clock.py](cli_clock.py) to test our device. 
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py 
02/24/2021 11:20:49
```

The time appears as output on the terminal, which is updated every second. The screenshot below shows the result from running this script.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/cli_clock.gif" height="360" /></p>


## Part C. Set up RGB Display
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

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/screen_test.gif" height="480" /></p>

#### Displaying an image

[image.py](image.py) contains an example of how to display an image of the Cornell Tech logo on the screen. 

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/cornell_tech_image.png" width="360"></p>

We experiment with this script to learn how to use the buttons. The updated code is present in [image_change.py](image_change.py) which shows different images based on which button the MiniPiTFT is pressed. For Button A, it shows the Cornell Tech Logo, and when Button B is pressed it shows "Wine Time". The display will show a white screen when both buttons are pressed together. The result can be seen in the GIF below.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/image_change.gif" height="360" /></p>

## Part D. Set up the Display Clock

In `screen_clock.py`. Show the time by filling in the while loop. You can use the code in `cli_clock.py` and `stats.py` to figure this out.


## Part E. Building a barebones clock

Our modified barebones clock can be found at [barebones_clock.py](barebones_clock.py). This uses the rotary encoder to move the time by 30 minutes. Moving it in the clockwise direction increments the time, while moving it in the anti-clockwise direction makes the time move back. The rotary encoder is connected using I2C.

Additionally, we use an array of images, to depict sunrise and sunset based on the time. These images show up in the MiniPiTFT that is attached to the Raspberry Pi.

Our final setup can be seen in the image below.
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/pi_rotary_encoder.png" height="360" /></p>


## Part F. Short video of the barebones PiClock

The video of the PiClock that uses the rotary encoder can be seen below:

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1614566984/video_to_markdown/images/google-drive--1GTcadkFiFY9N9W-uxGgojbXpPkQuTO_T-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1GTcadkFiFY9N9W-uxGgojbXpPkQuTO_T "")

## Part G. Planning further interactions/features for the PiClock

We want to make the PiClock representative of an individual's everyday life. We want the user to be in control of their time (and thus wish to continue using the rotary encoder to allow the user to increment/decrement their time). In addition, they perform activities at regular intervals. Some activities we brainstormed include:
* Sleeping
* Cooking
* Playing a sport
* Working

We explored the use cases of different sensors we had, and matched them to these activities. We decided with the following:
* Make a costume for a bed. Use a blanket to cover the proximity sensor to raise a signal when the person is sleeping. When the person wakes up, it's morning and the time moves forward.
* We plan to use the accelerometer or the capacitive touch sensor to raise a signal when the user moves his/her pan. 
* We want to make a sport for the user with the joystick. We decided to build a costume for the joystick and the user can use it to direct a soccer goal.

These are summarised in the image below:
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/future_interactions.png" height="360" /></p>

## Part 2

## Video of the final interactions
[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1614566585/video_to_markdown/images/google-drive--1Zml_PnKv7Po2L-kpPTjNheOi9eHsNsjS-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1Zml_PnKv7Po2L-kpPTjNheOi9eHsNsjS "")

