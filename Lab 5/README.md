# Observant Systems

For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi. The **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.


### Readings

1. [OpenCV](https://opencv.org/about/).
1. [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Qwiic Red LED Button

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Constructing a simple interaction](#part-a-constructing-a-simple-interaction)

B) [Paper Display](#part-b-paper-display)

C) [Characterize your Observant system](#part-c-characterize-your-observant-system)

D) [Testing the interaction prototype](#part-d-testing-the-interaction-prototype)

E) [Reflections](#part-e-reflections)
---

### Part A. Sense-making using the Pi-Camera
The RaspberryPi Camera V2 is setup using the instructions available on [the Pi hut](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera). 

Google's [Teachable Machines](https://teachablemachine.withgoogle.com/train) is used to build a simple classification model that can detect people wearing masks, versus those who are not. This [classification model](https://github.com/singhaniasnigdha/Interactive-Lab-Hub/tree/Spring2021/Lab%205/models/mask-nomask-random.zip) is then saved on the Raspberry Pi and run using the Pi Camera.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%205/imgs/teachable-machines.png" height="320" /></p>

Our classifier has 3 classes - masked faces, faces without masks and random unrelated images. The dataset for masked and unmasked faces used to train this model can be found [here](https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/). For the "others" category, 600 random pictures were collected without faces, so that the model does not misclassify or send an alert when a face is not in the frame.

The teachable machines model is tested using a webcam on an individual who was not part of the training data. The model performs reasonably well (screenshots below).

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%205/imgs/teachable-machine-result.png" height="320" /></p>

The inspiration for this idea was taken from Sam's Lab 4 where she built the [The Honest Mirror](https://github.com/snlee159/Interactive-Lab-Hub/tree/Spring2021/Lab%204), where wizarding was used to remind the user to wear a mask. Here, we leverage the power of machine learning and the Pi Camera to detect if an individual is wearing a mask. The interaction can be depicted using the storyboard below.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%205/imgs/storyboard.png" height="480" /></p>

### Part B. Paper Display

The Raspberry Pi is encased in a cardboard box, with outlets to allow for easy power source and speaker connections. The Pi Camera and red LED are placed outside the box to allow the device to capture images. Qwiic cables are used to connect the LED. The Pi Camera should be placed at an angle to allow an appropriate field of vision. 

<!-- ## TODO -- ADD IMAGE -->

**Choice of Material**: Cardboard is used to build the prototype for this device because it is inexpensive, versatile and can be cut, folded, and shaped with at-home equipment. By using an Olfa knife, it is easy to make a box out of a small sheet of cardboard, which is good enough to contain the Raspberry Pi, the Pi Camera, and any additional sensors.

**Other Alternatives**:  As devices of this kind are usually made of metal or plaastic, they were considered to build the prototype. Plastic Sheets were discarded because they are not environment friendly, while cardboard is bio-degradable and easily available at everyone's houses. Metal sheets are also not particularly friendly to the environment, but they are extremely complicated to cut, mold and shape.

### Part C. Characterizing the Observant system

* What can you use `Mask-Up` for? <br>
The device will be particularly useful in the current scenario, where all public spaces are frantic to open up but do not have the means to ensure that everyone is following the mandated protocols. Using this device at the entrace of any public building will be an effective way to keep a check on the behaviour of the crowd.

* What are other properties/behaviors of `Mask-Up`? <br>
`Mask-Up` uses the Camera to detect faces in its field of vision. These extracted faces can be used for additional processing. A red-LED blinks when the camera detects an individual without a mask to alert the group that safety protocols are being breached. The fear of raising alerts might help enforce the mask requirements, which people might otherwise ignore.

* What is a good environment for `Mask-Up`? <br>
This device is electronic, and is required to be kept away from water and inflammable areas. To effectively capture good-quality images which are easy to classify, the device will be more useful away from direct light, as that will result in a glare on the images. 

* What is a bad environment for `Mask-Up`? <br>
The device will be ineffective when it faces light as good quality images will not be captured. This might produce wrong results. The positioning of the camera is also crucial, as the face should be clearly in frame to get the most accurate outcomes.

* When will `Mask-Up` break? When it breaks how will `Mask-Up` break? <br>
While the algorithm performs well generally, it might product false negatives if the user tries to trick the process. The algorithm is looking for a covered mouth and nose, so if the user uses their hands or (even better) their mobile phone to conceal a part of their face, the device will not work correctly. The result will be a false-negative, classifying that the individual is wearing a mask while they are not.

* How does `Mask-Up` feel? <br>
The device feels sturdy as it is encased in a hard box. The limited visible hardware gives the appearance that the device is safe to use. It should, however, be noted that the device is not to be touched by the participants. It should ideally be placed at a distance where it can have a clear view of all individuals entering a public space without them having to force an interaction with it.

### Part D. Testing the interaction prototype

To allow for multiple faces to be detected and classified using this device, we integrated the Teachable Machines model with an OpenCV face-detection algorithm. An example of the OpenCV face detection algorithm can be seen below:

<!-- ## TODO -- ADD face detection gif -->

Once the faces are identified using Computer Vision, they are classified as either "Masked" or "No Mask" using the Teachable Machines Classifier explained in [Part A](#part-a-constructing-a-simple-interaction). The code can be found in [detect-faces.py](https://github.com/singhaniasnigdha/Interactive-Lab-Hub/tree/Spring2021/Lab%205/detect_faces.py).  Using the face detection algorithm prior to the classification drastically improves the accuracy of the model, as the model otherwise struggled to accurately recognise faces.

The real-time classifier was tested on different individuals in a public setting, and the recording can be seen below:

<!-- ## TODO -- ADD VIDEO -->

__Uncertainties/Errors reported__: While the model performs reasonably well in the usual setting, it is not very robust and can be tricked. Following are some images which were misclassified when the user covers their nose and mouth using objects other than a mask:

<!-- ## TODO -- ADD ERRORS -->

The errors are usually reported when a individual not wearing a mask is reported as wearing one. No other incorrect results are obtained. Further, given the nature of the task, other errors can be discounted for, as the primary objective is to ensure that every individual in a public setting is wearing a mask.

__Impact of a Misclassification__: As shown in the storyboard, this device can be used at the entrance of lecture halls, shopping malls, subway stations and other public buildings. If a misclassification occurs, it might put other individuals at the same location at risk of contamination, if the individual who is not wearing a mask is infected with a virus. It, however, should be noted that there are no current measures in place to check if all individuals are complying with the regulations. Employing manual labour puts these individuals at risk as they have to interact with many people every day. Automating this process is the best alternative in this case. 

One technique which can be adopted to prevent the system from getting tricked is to make the device small and concealed, such that it cannot be detected easily. Individuals will not be able to locate the devices and hence unable to trick it by temporarily covering their faces.

__Optimizations to reduce misclassification__: It can be said that the model is more accurate at detecting if the nose and mouth are covered, rather than covered with a mask. Perhaps, it would be useful to include these false positives in one of the other classes, to improve the results of the algorithm.


### Part E. Reflections

This assignment emphasizes on the value of Observant Systems, where interactions are not explicitly required but the system learns and interprets activities around it in meaningful ways. 

Parts of the assignment I am excited about:
* It was interesting to learn about OpenCV and I am happy to be able to integrate it with Teachable Machines to provide a more refined output.
* The prototype attempts to find a solution to a current problem.

Segments that can be improved include:
* Algorithm accuracy - It is not difficult to trick the algorithm into believing that an individual is wearing a mask. They can do so by placing their hands on their face to cover their nose or mouth. This also, sometimes, tends to misguide the OpenCV face-detection algorithm, which is unable to detect a face when the nose and mouth are covered. As such, I believe there is potential to improve on these aspects.
* Steady Outputs - The device continually attempts to find faces and predict the classification. The continuous processing results in outputs that might sometimes be difficult to interpret as they change very quickly. Having a timeout to make the next prediction was experimented with, but was not promising.