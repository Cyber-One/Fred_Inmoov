# Fred_Inmoov

Fred is a modified InMoov Robot.
You can find the videos showing his contruction here:
https://youtube.com/playlist?list=PLgXTfFM40HqEbnFfhaLPmLv_RS1ZRCilI

In the Official build of InMoov, 
there are two Arduino Mega 2560's located on his back with the I/O distributed using the Nervo Boards available from the online shop in the Inmoov website.
There was also a 8" Lenovo Windows based tablet that running the Java based MyRobotLab that remotely operated the two Arduino Mega 2560's

Because I like to be different, I used PCA9685 I2C 16 channel PWM driver boards based on the Adafruit servo driver breakout board.
4 of these in various places throughout the robot provide the servo control while reducing the nuber of wires running about the robot.

In version 4 of the script, we now add in the PIR and Ultrasonic sensors, to interface these, we are using an Arduino Nano.
This version is not being updated anymore and may in the future be removed, Look into the sub directory Fred for the current Version.

In version 5, I split the single script up into a number of files and expanded on the comments to help better explain what is happening.

If you have any questions regarding any of the files here, drop into my Discord and ask your questions, hopefully I will be able to answer the questions of implement changes if needed. :-)

At the time of writing, the OS for the system is MyRobotLab.
http://myrobotlab.org/
You can download the latest development version from there or talk to the developers of this platform there as well.

