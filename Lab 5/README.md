# Observant Systems

For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi. The **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


### Readings

1. [OpenCV](https://opencv.org/about/).
1. [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play with different sense-making algorithms](#part-a-play-with-different-sense-making-algorithms)

B) [Constructing a simple interaction](#part-b-constructing-a-simple-interaction)

C) [Testing the interaction prototype](#part-c-testing-the-interaction-prototype)

D) [Characterize your Observant system](#part-d-characterize-your-observant-system)

---

### Part A. Sense-making using the Accelerometer

The MPU-6050 combines a 3-axis accelerometer and 3-axis gyroscope and can be used for motion detection. By running a Fast Fourier Transform over the IMU data stream, a simple activity classifier between walking, running, and standing is created.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo.

### Part B. Sense-making using the Pi-Camera
The RaspberryPi Camera V2 is setup using the instructions available on [the Pi hut](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera). 

Google's [Teachable Machines](https://teachablemachine.withgoogle.com/train) is used to build a simple classification model that can detect people wearing masks, versus those who are not. This [classification model](https://github.com/singhaniasnigdha/Interactive-Lab-Hub/tree/Spring2021/Lab%205/models/mask-nomask-random.zip) is then saved on the Raspberry Pi and run using the Pi Camera.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%205/imgs/teachable-machines.png" height="320" /></p>

Our classifier has 3 classes - masked faces, faces without masks and random unrelated images. The dataset for masked and unmasked faces used to train this model can be found [here](https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/). For the "others" category, 600 random pictures were collected without faces, so that the model does not misclassify or send an alert when a face is not in the frame.

The teachable machines model is tested using a webcam on an individual who was not part of the training data. The model performs reasonably well (screenshots below).

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%205/imgs/teachable-machine-result.png" height="320" /></p>

The inspiration for this idea was taken from Sam's Lab 4 where she built the [The Honest Mirror](https://github.com/snlee159/Interactive-Lab-Hub/tree/Spring2021/Lab%204), where wizarding was used to remind the user to wear a mask. Here, we leverage the power of machine learning and the Pi Camera to detect if an individual is wearing a mask. The interaction can be depicted using the storyboard below.

<p align="center"><img src="https://github.com/singhaniasnigdha/Interactive-Lab-Hub/blob/Spring2021/Lab%205/imgs/storyboard.png" height="480" /></p>

### Part C. Testing the interaction prototype

The real-time classifier was tested on different individuals in a public setting, and the recording can be seen below:

<!-- ## TODO -- ADD VIDEO -->

__Uncertainties/Errors reported__: While the model performs reasonably well in the usual setting, it is not very robust and can be tricked. Following are some images which were misclassified when the user covers their nose and mouth using objects other than a mask:

<!-- ## TODO -- ADD ERRORS -->

The errors are usually reported when a individual not wearing a mask is reported as wearing one. No other incorrect results are obtained. Further, given the nature of the task, other errors can be discounted for, as the primary objective is to ensure that every individual in a public setting is wearing a mask.

__Impact of a Misclassification__: As shown in the storyboard, this device can be used at the entrance of lecture halls, shopping malls, subway stations and other public buildings. If a misclassification occurs, it might put other individuals at the same location at risk of contamination, if the individual who is not wearing a mask is infected with a virus. It, however, should be noted that there are no current measures in place to check if all individuals are complying with the regulations. Employing manual labour puts these individuals at risk as they have to interact with many people every day. Automating this process is the best alternative in this case. 

One technique which can be adopted to prevent the system from getting tricked is to make the device small and concealed, such that it cannot be detected easily. Individuals will not be able to locate the devices and hence unable to trick it by temporarily covering their faces.

__Optimizations to reduce misclassification__: It can be said that the model is more accurate at detecting if the nose and mouth are covered, rather than covered with a mask. Perhaps, it would be useful to include these false positives in one of the other classes, to improve the results of the algorithm.

### Part D. Characterizing the Observant system

* What can you use `Mask-Up` for? <br>
The device will be particularly useful in the current scenario, where all public spaces are frantic to open up but do not have the means to ensure that everyone is following the mandated protocols. Using this device at the entrace of any public building will be an effective way to keep a check on the behaviour of the crowd.

* What is a good environment for `Mask-Up`? <br>
This device is an electronic. As such it would be required that it be kept away from water and inflammable areas. To effectively capture good-quality images which are easy to classify, the device will be more useful away from direct light, as that will result in a glare on the images. 

* What is a bad environment for `Mask-Up`? <br>
The device will be ineffective when it faces light as good quality images will not be captured. This might produce wrong results. The positioning of the camera is also crucial, as the face should be clearly in frame to get the most accurate outcomes.

* When will `Mask-Up` break? When it breaks how will `Mask-Up` break?<br>
While the algorithm performs well generally, it might product false negatives if the user tries to trick the process. The algorithm is looking for a covered mouth and nose, so if the user uses their hands or (even better) their mobile phone to conceal a part of their face, the device will not work correctly. The result will be a false-negative, classifying that the individual is wearing a mask while they are not.

* What are other properties/behaviors of `Mask-Up`? <br>


* How does `Mask-Up` feel? <br>