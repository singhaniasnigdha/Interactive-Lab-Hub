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

H) [Features for the Final Clock of Pi](#part-h-features-for-the-final-clock-of-pi)

I) [Video of the Final Interactions](#part-i-video-of-the-final-interactions)


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

#### Displaying Statistics (Text) on the MiniPiTFT

The output can be seen in the screen below.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/stats.png" height="360" /></p>

## Part D. Set up the Display Clock

We take inspiration from the code in [stats.py](stats.py) to learn to display text on the MiniPiTFT screen. This is used to display the time on the MiniPiTFT. The source code is available at [display_clock.py](display_clock.py) and the output can be seen in the image below.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/display_clock.png" height="360" /></p>

## Part E. Building a barebones clock

Our modified barebones clock can be found at [barebones_clock.py](barebones_clock.py). This uses the rotary encoder to move the time by 30 minutes. Moving it in the clockwise direction increments the time, while moving it in the anti-clockwise direction makes the time move back. The rotary encoder is connected using I2C.

Additionally, we use an array of images, to depict sunrise and sunset based on the time. These images show up in the MiniPiTFT that is attached to the Raspberry Pi.

Our final setup can be seen in the image below.
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%202/imgs/pi_rotary_encoder.png" height="360" /></p>


## Part F. Short video of the barebones PiClock

The video of the PiClock that uses the rotary encoder can be seen below:

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1614566984/video_to_markdown/images/google-drive--1GTcadkFiFY9N9W-uxGgojbXpPkQuTO_T-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1hbovvlACXsPr-aSLoADX2Of5WrD6OYUR "")

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

## Prep for Part 2. Feedback from Classmates

Shivani Doshi (sgd73) liked the use of the sensor to control time and the auto-changing backgrounds:
> It was nice that you showed the proof of having done each section by including a video, well done! You guys definitely got a lot accomplished for this lab, which is awesome to see. I like that you have that rotary encoder to shift the time and change the background accordingly. The further interactions part was also really interesting, where you're playing with different hours having different significances. All in all, really great work!

Bebei Lu (bl643) liked how detailed the documentation was:
> I love how you recorded every step along the way. You have definitely done a lot for this lab! You made the device truly interactive. With the animated background and time travel, the device responded to user action. This feedback loop is very cool!

Ritika Poddar (rp477) particularly liked the cooking element and viewed our design as a video game:
> I love the use of the rotary encoder on the barebones clock, it is very cool to watch the sun rise up in the image. Your final interactions video is amazing it's almost like you built a whole video game within itself. I like how you utilized so many different interaction elements. My favorite part was the dinner time/ cook food feature :)

## Part H. Features for the Final Clock of Pi
As discussed in [Part G](#part-g-planning-further-interactionsfeatures-for-the-piclock), Sam and I decided to make the device interactive by incorporating activities from everyday life, and using the various sensors with our Raspberry Pi to perform those activities. All our sensors are connected using I2C. Following is a comprehensive coverage of the different interactions available in our version of the Clock of Pi:

### Time Display/Control
__Sensors Used__: Rotary Encoder, MiniPiTFT <br>
__Description__: This component is the same as was used for our barebones clock and shown in [Part F](#part-f-short-video-of-the-barebones-piclock). The rotary encoder was lit up, and the user can move it either clockwise or counter-clockwise, which adds or subtracts 30 minutes from their current day. The time and day of the week are displayed on the MiniPiTFT that is set up on the Pi. We present an image of the mountains on the screen, and highlight the rising and setting of the sun to further emphasize the time of the day.

### Soccer
__Sensors Used__: Joystick, MiniPiTFT <br>
__Description__: At 10am on Sunday morning, the screen informs the user that it is time for Soccer practise. We see a player waiting to kick the ball. The costume of the soccer ball on the joystick informs the user that they should move this to kick the ball. As the user moves the joystick towards the goal, the action is simulated on the screen, and the user kicks a goal! The time on the screen moves to 11am, informing the user that they spent 1 hour during training.

### Cooking Dinner
__Sensors Used__: Green Button, Accelerometer, MiniPiTFT <br>
__Description__: When the User clicks the green button, the device learns that the user is hungry. The screen will display "Dinner Time", after which the user should toss the frying pan which is connected to an accelerometer. The user should perform this activity for a short duration, after which the food is deemed cooked and the User can enjoy their meal.

### Bedtime
__Sensors Used__: Proximity Sensor, MiniPiTFT <br>
__Description__: We model a tiny bed on the breadboard, the sheets of which should cover the proximity sensor when the User sleeps. At 11pm, our user goes to sleep and the sheets cover the proximity sensor. When the sheets are removed, the device learns that it is time to wake up, and the clock shows 6am of the next day.

### Wine-time
__Sensors Used__: Red Button, MiniPiTFT <br>
__Description__: We add wine-time as a fun element in our design. At 5pm on Friday, the MiniPiTFT lights up and displays the message "Wine-Time"! The red button on the breadboard blinks, waiting for the user to click it so as to finish their glass of wine. We use the MiniPiTFT again to show a series of animations where 2 glasses of wine clink together.

## Part I. Video of the Final Interactions
The interactions described above are showcased in the video below:

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1614566585/video_to_markdown/images/google-drive--1Zml_PnKv7Po2L-kpPTjNheOi9eHsNsjS-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1Zml_PnKv7Po2L-kpPTjNheOi9eHsNsjS "")

