# You're a wizard, Snigdha

<p align="center"><img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400"></p>

In this lab, we practice wizarding an interactive device. We focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. 

## Text to Speech and Speech to Text

In the home directory of the Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

These examples can be executed by typing 
`./espeakdeom.sh`.

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Audio files can also be played directly with `aplay filename`.

The home directory on the Pi also contains `speech2text` folder. We explore the different shell/python scripts, especially `test_words.py`, to understand how the vocabulary of the system is defined. `./vosk_demo_mic.sh` shows how this tool can be used.

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab, it may be useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()

## Demo

The [demo directory](./demo) contains an example wizard of oz project that can be used as a template. It shows how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. The controller can be used to control what the Pi says.

## DeepSpeech

There is an included [dspeech](.dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. 


# Lab 3 Part 2

## Prep for Part 2

The overarching idea of this project is inspired fromm a Harry Potter-themed Escape Room. The users are expected to complete 5 tasks, which range from logic puzzles to simple Harry Potter trivia. 

The theme of the game is preparing a student to begin lessons at Hogwarts. To do so, they must:
1. Visit Diagon Alley
1. Purchase a Wand from Ollivanders
1. Get aboard the Hogwarts Express and buy some Berti Botts Every-Flavour Beans
1. Practise their spells
1. Pick a house

To make audio the predominant mode of communication, the Raspberry Pi will speak with the user, and ask them to reply with their answers. 

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%203/imgs/sketch.png" height="360" /></p>

Some additional sensors are added to make the device more interactive and fun to play.

## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*

## Prototype your system
For this demo, we use: 
* Raspberry Pi, 
* MiniPiTFT Display
* a speaker/aux cable 
* USB microphone
* Rotary Encoder
* Red LED Button
* Green LED Button

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
*your answer here*

### What worked well about the controller and what didn't?

*your answer here*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

*your answer here*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

*your answer here*

