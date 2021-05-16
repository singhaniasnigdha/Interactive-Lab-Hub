# Final Project

In this assignment, a combination of sensors are used to build a fully functioning and well-designed interactive tool that could be used at all homes. This is the **The Little Dipper** (inspired from the Constellation)!

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs_readme/ursaminor.jpg" height="360" /></p>

## The Little Dipper

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs_readme/little-dipper.png" height="360" /></p>

### Rationale

Little Dipper prepares a perfect cup of tea, as you get ready/are engaged in other things every morning. You won't have to worry about over-extracting your tea anymore. In fact, after caliberating it well, the strength of your tea will be the same every single day!

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs_readme/storyboard.png" height="420" /></p>

### Components used for Interactions

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs_readme/schematic.png" height="420" /></p>

__Rotary Encoder__: The first step to begin the process requires the user to select how long they want the device to dip their tea bag. This is done using the rotary encoder, where they twist the wheel to select between 1-5 minutes. The default dipping time is set to 3 minutes. The GIF below showcases this interaction.
<!-- TODO: Add GIF -->

__LED Buttons__: The Green and Red LED buttons are used to get user input to start and abruptly stop the tea dipper, respectively. After the user sets the dipping time using the Rotary Encoder, the Green LED blinks, drawing the user's attention to the button, and asking them to press the button to start the dipping process. The dipper will begin the process and continue dipping the user's tea-bag for the specified duration. Here, the Red LED button can be pressed if he wants to interrupt the process, and terminate it before stopping time. 

LEDs always blink if the user has the option of using them, and are turned off when not in use.

__Servo Motor__: A servo motor is used to perform the dipping action. The tea-bag is placed on the hook and its position is controlled by the Raspberry Pi. This is a new sensor that was experimented with for this assignment. It was exciting to learn how to solder wires to make this operational (all other sensors could be connected using Qwiic cables).
<!-- TODO Add picture -->

The green, orange and brown wires connect to 3.3V, GPIO and GND, respectively.


__Mini PiTFT__: The PiTFT Display shows the welcome screen as well all feedback throughout the set up of the Little Dipper. Instructions such as 'Press the Red Button to Stop' as well as assisting the user while selecting the duration of dipping are done using this device. The colored display makes it a preferred choice over the OLED Display. However, this screen lacks flexibility, as it requires to alwaays be placed on the Pi (limiting the design).

<!-- <p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%203/imgs/screens.png" height="360" /></p> -->


__Text to Speech__: Voice is used to draw the user's attention when the tea is ready but they are not close to the device. [`GoogleTTS`](GoogleTTS_demo.sh) is used for because this TTS is clearer as compared to others available. A speaker is connected to the 4-pole stereo audio port.
```
def speak(command):
    subprocess.run(["sh", "GoogleTTS_demo.sh", command])
    time.sleep(0.5)
```

### Paper Display

The Raspberry Pi is encased in a cardboard box, with outlets to allow for easy power source and speaker connections. The sensors are placed outside the box to allow the user to operate them. Qwiic cables are used to connect the LEDs, rotary encoder and Mini PiTFT. Servo motors are connected to the Pi by soldering the wires to the TFT inputs. 

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs_readme/paper-display.png" height="420" /></p>

**Choice of Material**: Cardboard is used to build the prototype for this device because it is inexpensive, versatile and can be cut, folded, and shaped with at-home equipment. By using an Olfa knife, it is easy to make a box out of a small sheet of cardboard, which is good enough to contain the Raspberry Pi, the servo motor, and any additional sensors.

**Other Alternatives**:  As devices of this kind are usually made of metal or plastic, they were considered to build the prototype. Plastic Sheets were discarded because they are not environment friendly, while cardboard is bio-degradable and easily available at everyone's houses. Metal sheets are also not particularly friendly to the environment, but they are extremely complicated to cut, mold and shape.


### Running the script

To run the script on your device, Python3 should be available. Clone the repository and create a virtual environment. Download all requirements and run the `tea-dipper.py`

```
pip install -r requirements.txt
python tea-dipper.py
```


### Interaction Video

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1621183450/video_to_markdown/images/google-drive--1RZlSrD-6ynQ_WNaj6Y96DU8G5RMVBl1p-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1RZlSrD-6ynQ_WNaj6Y96DU8G5RMVBl1p/view?usp=sharing "")


### Reflections

Some aspects of the project I enjoyed were:
* Learning how to use the servo motors and soldering wires.
* Coming up with an idea and a prototype that I would use everyday.

Some aspects which would be exciting to add are:
* Setting up a camera which can learn which tea is being dipped and set different default dipping times per tea.
* Experimenting with Laser Cutting or more complex display methods.
* It would also be exciting to use MQTT to allow the user to connect to the device using their mobile phones.
