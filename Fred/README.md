# Fred Inmoov V5.0 program

Unlike earlier version of Fred's program, this one has split the program up into different sections to make it easier to find parts.
It may yet be broken up into more modular files.
Breaking the project up into a smaller files makes it easier to find and debug issue.
It also helps with designing new features.

Where possible, lots of comment have been placed in the code to help NOOB's learn how MyRobotLab services work and how this section is supposed to work. :-)
It can be advantagous when your trying to use service if you can look up and see how it's ment to be called as well.

<b>Start.py </b>
General start point and is responsible for starting the Graphical User Interface (GUI) and calling all the other sub files required to start up the system.

<b>1_Configuration/</b>
This Folder is where the various configuration files are stored for Fred.
If you are using these scripts for your robot, then this is where you change the config to suit your build.
I've tried to add notes as to what each of the setting do.

<b>Controller.py </b>
This is where the top level controllers are created such as the RasPi service, the Arduino services and the PCA9685 services.

<b>3_Servos/</b>
Because there are so many servos used in an Inmoov build and a modified one like Fred use even more, the servos service creation is broken into multiple files.
I've tried to group servos by physical area of operation, not controller or location of the servo.
For example, the Neck group contains the head Roll, Pitch and Yaw servos, the Roll and Pitch are located below the neck while the Yaw is located in the head. 

<b>IO.py</b>
This is for miscilanous IO devices like the PIR sensor and the Ultrasonic range finders.

<b>Speech.py</br>
This is where the Text To Speech and Speech recognition services are created.

<b>Life.py</b>
This set of routines control the simulation of being alive like the blinking of the eye lids and random movements that simulate a living being.

<b>Gestures.py</b>
Any scripts of movements such as shaking the head as a no, or nodding the head as a yes, that may be called by the ProgramAB are scripted here.

<b>Brain.py</b>
This is where the simulated AI lives. :-)
For now, this is ProgramAB, a program that runs Artificial Inteligents Markup Language (AIML) files commonly refered to as Alice Bot.
