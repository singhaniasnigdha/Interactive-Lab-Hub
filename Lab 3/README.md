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

The overarching idea of this game is inspired fromm a Harry Potter-themed Escape Room. The users are expected to complete 5 tasks, which range from logic puzzles to simple Harry Potter trivia. 

The theme of the game is preparing a student to begin lessons at Hogwarts. To do so, they must:
1. Visit Diagon Alley
1. Purchase a Wand from Ollivanders
1. Get aboard the Hogwarts Express and buy some Berti Botts Every-Flavour Beans
1. Practise their spells
1. Pick a house

To make audio the predominant mode of communication, the Raspberry Pi will speak with the user and ask questions, to which the user replies. 

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%203/imgs/sketch.png" height="360" /></p>

Some additional sensors are added to make the device more interactive and fun to play.

## Share your idea sketches with Zoom Room mates and get feedback

I walked through my plan with Hortense Gimonet and Anam Tahir during our breakout session. They were quite interested to see what riddles/puzzles will be used.

I introduced the proposal to Shivani Doshi and Ritika Poddar, who thought the theme and story line of incorporating Hogwarts was engaging. They are excited to see the final product. Shivani also suggested that I  use more sensors to make the device interesting.

## Prototyping the System
For this demo, we use: 
* Raspberry Pi, 
* MiniPiTFT Display
* a speaker/aux cable 
* USB microphone
* Rotary Encoder
* Red LED Button
* Green LED Button

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%203/imgs/schematic.png" height="420" /></p>

The code for this system can be found at [harrypotter.py](harrypotter.py). This is a 5-step game to prepare the player before they embark their magical journey at Hogwarts. The MiniPiTFT is used to show images relevant to the task at hand. We connect all sensors using I2C, as shown in the image above.

As the game has a fixed sequence, this strategy is used to queue images and texts for speech translation. Based on which stage the user is currently at, images and prompts are shown. This can be achieved using simple `if` conditional statements.

### Components used for Interactions ###

__Text to Speech__: Communicating through voice is the primary sensing modality in this game and `GoogleTTS` is used for TTS translation. `espeak` was also experimented with but the voice was too unpleasant. A speaker/wired headphones are connected to the 4-pole stereo audio port.
```
def speak(command):
    subprocess.run(["sh", "GoogleTTS_demo.sh", command])
    time.sleep(0.5)
```
The device asks the user several questions, responds when they have the wrong answer, and congratulates them when they are correct. It guides the user through the puzzle.

__Mini PiTFT__: The PiTFT Display is used to display many nostalgic images from the Harry Potter universe, which compliments the questions being asked. For several tasks, the user is required to refer to the screen to make a decision. Some pictures of the display are shown below: 
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%203/imgs/screens.png" height="360" /></p>

__LED Buttons__: The Red and Green LED buttons are used to get user input at some stages. The Red button should be pressed when the user wants the system to repeat the instructions, and Green when they are ready to give out an answer. The button blinks when the user has the option of pressing them, and is otherwise turned off.

__Rotary Encoder__: As the last task, the user has to pick their house. The symbols of the 4 houses - Gryffindor, Hufflepuff, Ravenclaw and Slytherin - appear on the screen, and the user should use the rotary encoder to select which house they want to belong to. Moving the wheel moves between choices, and pressing the wheel confirms the selected choice. The GIF below showcases this interaction.
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%203/imgs/rotary_encoder.gif" height="360" /></p>

__The Controller__: A simple user input from the terminal is used to control the flow of the game. This is because the microphone used for this assignment is not powerful enough to perfectly translate what the users are saying. To avoid encounters where 1) the system misunderstands the user 2) the user says something unknown, we keep the system simple and respond in 1 of 2 ways, as specified in the code.


### The Game ### 
There are 7 scenes and 5 tasks the user will witness. The first scene reads out the acceptance letter to Hogwarts. The user is asked if they are ready to begin, and expects a response. The next scene shows Diagon Alley, where the user should solve a brick wall puzzle to enter the Alley. This is a reference to the movie where Hagrid knows which bricks to tap in order to open up the wall, while Harry looks at him with disbelief. In our version, the user is asked to follow a series of instructions to learn which brick to tap.

The third scene takes us to Ollivanders, where the user should identify 3 personal traits to help Ollivander pick a suitable wand. After all the shopping from Diagon Alley, the next scene takes place on Hogwarts Express, when the player is hungry. They need to buy Bertie Bott's Every-Flavour Beans, but need to pick unique flavours to clear the round. Now at Hogwarts, the fifth scene asks the user to open their suitcase using a magic spell. 

In the sixth scene, the user is at The Great Hall, and has to be sorted into their house! But the sorting hat is not safe to use (with the pandemic, and all!). So the user must pick a house of their own choosing, as long as they can identify the colors used to represent it! This brings us to the end of the game, and the seventh scene thanks the user for participating.

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1616383029/video_to_markdown/images/google-drive--19yOeTlyNIUetqK_j5zS16LM2EOm35oFr-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/19yOeTlyNIUetqK_j5zS16LM2EOm35oFr/view?usp=sharing "")

### Problems Encountered
I attempted speech recognition with the microphone, but could not get deepspeech to be very accurate and consistent with the translated text. My accent also seemed to be one of the primary hiccups, as a result of which I had to resort to Wizarding using terminal input. 

## Testing the System
We had at least two people interact with this system and review the interactions and setup.

### What worked well about the system and what didn't?

The concept of Harry Potter worked well, as some people were excited to see what the device could do. Use of rotary encoder to select the House based on the display (MiniPiTFT) was well received.

One disadvantage of the system was the voice output. It was not very clear, and could not convey messages with a certain emotion (such as excitement, or disappointment). It would have been interesting to use the voice from one of the Harry Potter characters (maybe, Professor McGonagall).

### What worked well about the controller and what didn't?

The Controller used for this experiment is user input based on 1's and 0's. Every action has 2 paths, the decision of which depends on what is entered into the terminal by the person controlling the interaction. This makes the interaction swift, and follows a fixed expected pattern. The Controller was also useful because the STT was not reliable - different accents and words from the Harry Potter world were not detected well.

The fixed pattern, however, is also a downside for this setup. The system is limited to only 2 responses per question. It cannot help the user if they have any questions.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

Some observations that were made during user interactions where:
* The system was unable to answer queries so having support would be useful in a more autonomous version.
* If building an autonomous system, we could have more conditional branches as opposed to 2 used in this simple version.
* The users knew the device was rigged because it could understand all their commands perfectly. It is interesting to note that users expected the device to misunderstand.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

As the questions are open-ended, we would require to collect answers from multiple people to build an effective autonomous system. We can add Hogwarts terminology to the vocabulary so that the system is better equipped to translate speech to text.

As the game focuses on Harry Potter and the wizarding world, it would be interesting to use more spells and capture hand gestures to also quiz individuals on wand movements. By taking note of pauses, we could also interpret if the user wants support and provide hints accordingly.
