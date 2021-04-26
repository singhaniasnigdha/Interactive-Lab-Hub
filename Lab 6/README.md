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

<!-- TODO: For example, if you made a remote controlled banana piano, explain why anyone would want such a thing. -->

The idea is to provide the thrill of a game in physical form, rather than relying on a screen that automates all user input and feedback.

<!-- Add storyboard -->

This application has 2 components -- the Leader and the Player. The leader chooses a word, which the player should guess. If the player can guess the word, both win, otherwise both lose. The code can be found on [hangman_leader.py](./hangman_leader.py) and [hangman_player.py](./hangman_player.py).

### The Architecture

We create 2 topics for the leader and player to communicate on: `IDD/hangman_leader` and `IDD/hangman_player`.

<!-- Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music? -->

Several sensors are used by the leader and the player. These are:

**The Leader** <br>
* Mini PiTFT Display
* OLED Display
* Rotary Encoder
* Red LED Button
* Green LED Button

**The Player** <br>
* Mini PiTFT Display
* OLED Display
* 2x Capacitive Touch Sensors

<!-- Add architecture -->

Both the leader and player provide inputs, and receive outputs. The workflow can be described as below:

<!-- Add workflow image -->

### Prototype

The different stages of the hangman game that appear on the Mini PiTFT are shown in the image below. These are difficult to capture on film because of the brightness.
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/stages.png" height="320" /></p>

To begin the game, the leader uses the rotary encoder to set the length of word that the player should guess:
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/set_word_len.gif" height="320" /></p>

This information is relayed to the player using MQTT in the format: `{word},{hangman_status},{is_correct_guess},{is_start_of_game}`. The word is composed of spaces, and only filled when characters are correctly guessed. The message sent in the stage above is `_ _ _, 0, None, True`. The OLED screen is updated accordingly.

The player will use their keyboard to select a letter which they believe is present in the word selected by the leader. Their setup is as shown below:
<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/player_device.png" height="320" /></p>

<!-- Do think about the user interface: if someone encountered these bananas, would they know how to interact with them? Should they know what to expect? -->

### Interaction Video

<!-- It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location. -->


### Reflections