Unlike earlier version of Fred's program, this one has split the program up into different sections to make it easier to find parts.
It may yet get broken up more.

Where possible, lots of comment have been placed in the code to help NOOB's learn how MyRobotLab services work. :-)

<b>Start.py </b>
General start point and is responsible for calling all the other sub files.

<b>Controller.py </b>
This is where the top level controllers are created such as the RasPi service, the Arduino services and the PCA9685 services.

<b>Servos.py</b>
Currently, not too many of the servos are defined, but as more are defined, this file may need to be split into smaller groups.

<b>Life.py</b>
This set of routines control the simulation of being alive like the blinking of the eyes ect.

<b>Gestures.py</b>
Any scripts of movements such as shaking the head as a no, or nodding the head as a yes as scripted here.

<b>Brain.py</b>
This is where the simulated AI lives. :-)
