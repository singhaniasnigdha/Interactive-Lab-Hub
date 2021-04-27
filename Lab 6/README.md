# m[Q](https://en.wikipedia.org/wiki/QAnon)tt[Anon](https://en.wikipedia.org/wiki/QAnon): Where We Go One, We Go All

This lab introduces the concepts of distributed interaction.

### Requirements
1. Install [MQTT Explorer](http://mqtt-explorer.com/)
1. Readings 
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of Internet of Things (IoT) devices. 

### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`
* **Client** - A device that subscribes or publishes information on the network
* **Topic** - The location data gets published to. These are hierarchical with subtopics. If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. Subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on that topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe
* **Publish** - This is a way of sending messages to a topic. You can publish to topics you don't subscribe to. Just remember on our broker you are limited to subtopics of `IDD`

Setting up a broker isn't much work but for the purposes of this class you should all use the broker we've set up for you. 

### MQTT Explorer

Debugging and visualizing what's happening on your MQTT broker can be helpful. [MQTT Explorer](http://mqtt-explorer.com/) is used to connect to the IDD broker set up for this class. The connections can be established using the parameters below:

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/mqtt_explorer.png" height="320" /></p>

### Send and Receive 

[sender.py](./sender.py) and and [reader.py](./reader.py) present the basics of using the mqtt in python. Before any files are executed, install the packages using `pip install -r requirements.txt`

## The MQTT Hangman

[Sam Lee (snl48)](https://github.com/snlee159/Interactive-Lab-Hub/tree/Spring2021/Lab%206) and I worked together to build this distributed application. We wanted to celebrate a childhood game player on pen/paper without providing a mobile app-like interface. Following section document our version of the MQTT [Hangman](https://en.wikipedia.org/wiki/Hangman_(game))!

### The Design

The idea is to provide the thrill of a game in physical form, rather than relying on a screen that automates all user input and feedback.

<!-- Add storyboard -->

This application has 2 components -- the Leader and the Player. The leader chooses a word, which the player should guess. If the player can guess the word, both win, otherwise both lose. The code can be found on [hangman_leader.py](./hangman_leader.py) and [hangman_player.py](./hangman_player.py).

### The Architecture

We create 2 topics for the leader and player to communicate on: `IDD/hangman_leader` and `IDD/hangman_player`.

Several sensors are used by the leader and the player. The sensors and relevant functionality for the leader and player can be described as:
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/component_diagram.png" height="360" /></p>

Both the leader and player provide inputs, and receive outputs. The workflow and communication can be summarized as below:
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/flow_diagram.png" height="360" /></p>

### Prototype

The different stages of the hangman game that appear on the Mini PiTFT are shown in the image below. These are difficult to capture on film because of the brightness.
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/stages.png" height="160" /></p>

To begin the game, the leader uses the rotary encoder to set the length of word that the player should guess:
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/set_word_len.gif" height="420" /></p>

This information is relayed to the player using MQTT in the format: `{word},{hangman_status},{is_correct_guess},{is_start_of_game}`. The word is composed of spaces, and only filled when characters are correctly guessed. The message sent in the stage above is `_ _ _, 0, None, True`. The OLED screen is updated accordingly.

The player will use their keyboard to select a letter which they believe is present in the word selected by the leader. Their setup is as shown below and they select a letter by turning the letter down. Every letter is connected to a node on the capacitive touch sensor. (NOTE: We are constrained by 24 available nodes in Capacitive Sensor, as the Raspberry Pi can at most connect to 2 such sensors, each providing us with 12 nodes. To accomodate this, we skip connections to letters X and Z.)
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/player_device.png" height="320" /></p>

We choose this design as it helps the user keep track of which letters they have already selected, to ensure they do not repeat the same wrong letter multiple times. Let's say the player chooses letter 'B'. This will show up on the leader's OLED screen and the red and green LEDs will begin flashing.
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/selected_b.gif" height="420" /></p>

The leader should then decide if the selected character is correct or not. If the selected character is the correct choice, they press the Green LED. Next, they use the rotary encoder to selected which blank space this letter should fill. A rectangle appears over the current position in the word to guide the user. This message is transmitted to the player as: `B _ _, 0, True, False`.
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/correct_char.gif" height="420" /></p>

Suppose the leader believes that the selected letter is incorrect. They press the red LED. In this case, the message would be `_ _ _, 1, False, False`. As one wrong move has been made, the head of the hangman appears on the PiTFT display.
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/wrong_char.gif" height="420" /></p>

### Interaction Video

Sam and I recorded the final interaction video on Zoom. The display screen could not be captured well, and hence some subtitles have been added to aid understanding.

<!-- It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location. -->


### Reflections

Some things that we appreciate about this project are:
* Learning about MQTT and expanding the scope of the project to incorporate multiple Raspberry Pis. We enjoyed brainstorming and developing this idea.
* Increasing the complexity of the deliverable as compared to our past projects.

Some aspects which we thought could be added/improved were:
* Making the use of the rotary encoder to start the game more intuitive. We change the color of the encoder from blue to red, but this might not be sufficient to draw the user's attention and guide them through the process.
* Handling duplicate characters. For example: `APPLE` has 2 P's, which the leader cannot handle currently. With the limited number of buttons we were constrained on how we could use them to fill multiple gaps on one player input.
* Account for more than 1 player. Our code does not handle situations where multiple character inputs are sent without response, or inputs from multiple players. It would be exciting to see how this can be expanded to involve more than 1 player (in addition to the leader).