########################################
#
# Program Code for Fred Inmoov
# Of the Cyber_One YouTube Channel
# https://www.youtube.com/cyber_one
#
# This is version 5
# Divided up into sub programs
#
# Running on MyRobotLab (MRL) http://myrobotlab.org/
# Fred in a modified Inmmov robot, you can find all the
# origonal files on the Inmoov web site. http://inmoov.fr/ 
#
# Controllers.py
# This file isto start any major controllers 
# we might need.
#
########################################
print "Starting the various Controllers"

# Start the Raspberry Pi service.
# The core of the Fred Inmoov build is the Raspberry Pi 4 (Raspi4) Single Board Computer (SBC)
# This small low cost computer is not powerful enough to run everything, but there is no reason 
# why we can't have more than one Raspi4 installed in Fred.
# The first one is installed in the top of the head, but we can add one or two more in the
# back at a later date and split the processing up.
# The Raspi4 has two I2C ports built in, Port 0 is used for the microSD card, 
# while Port 1 is available for us to use.
raspi = Runtime.createAndStart("raspi","RasPi")

# Start the Arduino Nano connected using /dev/ttyUSB0
# In the Fred build, I'm using an Arduino Nano for the two Ultrasonic Sensors and the PIR sensor.
# The Arduino also has an I2C Port 0 is we need to use it.
arduinoNano = Runtime.start("arduinoNano","Arduino")
arduinoNano.setBoardNano()
arduinoNano.connect("/dev/ttyUSB0")

# If you were to run the two Arduino Mega 2560 as used in a standard build,
# this is also where you would start the services.
# Again each of the Arduino Mega 2560 have an I2C Port 0.
# To use these remove the # from in front of the lines needed.
# Also make sure the USB port is listed correctly and the MRL_COMM is
# installed on each arduino that you have installed

## For the Left Arduino Mega 2560
#arduinoLeft = Runtime.start("arduinoLeft","Arduino")
#arduinoLeft.setBoardMega()
#arduinoLeft.connect("/dev/ttyUSB1")

## For the Right Arduino Mega 2560
#arduinoRight = Runtime.start("arduinoRight","Arduino")
#arduinoRight.setBoardMega()
#arduinoRight.connect("/dev/ttyUSB2")

######################################################################
# The next level of controllers that can be used are attached to the
# I2C bus of either the Raspi4 or the Aurduinos.
######################################################################

# Our servo controllers in Fred are the Adafruit 16 channel PWM Servo drivers
# With four of these installed we will need to create four separate service, one for each
# Next we need to attach the servo drivers to the Raspi4.
# There are three parameters we need to set,
#
# The first parameter is the service we want to attach it to, normally either the RasPi or one of the Arduinos
# in our case it will be the Raspi4.
#
# The second parameter is the bus, This is normally 1 for the RasPi or 0 for an Arduino.
#
# Each servo driver has a unique address that is hard coded by means of a set of jumpers 
# on the controller boards, This is our Third parameter, There are seven jumpers that form
# a binary number that is added to 0x40. Note the 0x indicates the number is in hexadecimal format
# that is base 16 and has values in the range 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
# 0x40 is equal to 64 in decimal, the seven jumpers will give up to 128 possible address
# Just be aware of any other I2C devices you have on the bus and what their address are, 
# some device can not be changed or have a very limited number of selectable addresses.

Head = Runtime.createAndStart("Head","Adafruit16CServoDriver")
Head.attach("raspi","1","0x40")

#Back = Runtime.createAndStart("Back", "Adafruit16CServoDriver")
#Back.attach("raspi","1","0x41")

#RightArm = Runtime.createAndStart("RightArm", "Adafruit16CServoDriver")
#RightArm.attach("raspi","1","0x42")

#LeftArm = Runtime.createAndStart("LeftArm", "Adafruit16CServoDriver")
#LeftArm.attach("raspi","1","0x43")

