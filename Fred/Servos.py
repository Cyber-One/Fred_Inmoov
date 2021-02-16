#######################################################
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
# HeadServos.py
# This file is to start all the servos 
# used in the head
#                                                     #
#######################################################
print "Starting the various Servos Services"

print "-Head Group"
print "--Right Eye X axis"
# Change the names of the servos and the pin numbers to your usage
RightEyeLR = Runtime.createAndStart("RightEyeLR", "Servo")
# attach it to the Head Adafruit 16 channel PWM Servo board - pin 15
RightEyeLR.attach(Head,15)
# If were were using one of the Arduino's then you would use the following line
#RightEyeLR.attach(arduinoLeft,22)  
# Refer to http://inmoov.fr/default-hardware-map/ for the Nervo board connections
# Next lets set the various limits and mappings.
RightEyeLR.setMinMax(0,180)
RightEyeLR.map(0,180,1,180)
RightEyeLR.setRest(90)
RightEyeLR.setInverted(False)
RightEyeLR.setVelocity(60)
RightEyeLR.setAutoDisable(True)
RightEyeLR.rest()

print "--Right Eye Y axis"
RightEyeUD = Runtime.createAndStart("RightEyeUD", "Servo")
# attach it to the pwm board - pin 14
RightEyeUD.attach(Head,14)
RightEyeUD.setMinMax(0,180)
RightEyeUD.map(0,180,1,180)
RightEyeUD.setRest(90)
RightEyeUD.setInverted(False)
RightEyeUD.setVelocity(120)
RightEyeUD.setAutoDisable(True)
RightEyeUD.rest()


print "--Left Eye X axis"
LeftEyeLR = Runtime.createAndStart("LefttEyeLR", "Servo")
# attach it to the pwm board - pin 13
LeftEyeLR.attach(Head,13)
LeftEyeLR.setMinMax(0,180)
LeftEyeLR.map(0,180,1,180)
LeftEyeLR.setRest(90)
LeftEyeLR.setInverted(False)
LeftEyeLR.setVelocity(120)
LeftEyeLR.setAutoDisable(True)
LeftEyeLR.rest()


print "--Left Eye Y axis"
LeftEyeUD = Runtime.createAndStart("LeftEyeUD", "Servo")
# attach it to the pwm board - pin 12
LeftEyeUD.attach(Head,12)
LeftEyeUD.setMinMax(0,180)
LeftEyeUD.map(0,180,1,180)
LeftEyeUD.setRest(90)
LeftEyeUD.setInverted(False)
LeftEyeUD.setVelocity(60)
LeftEyeUD.setAutoDisable(True)
LeftEyeUD.rest()


print "--Upper Eyelids"
UpperEyeLid = Runtime.createAndStart("UpperEyeLid", "Servo")
# attach it to the pwm board - pin 11
UpperEyeLid.attach(Head,11)
UpperEyeLid.setMinMax(45,180)
UpperEyeLid.map(0,180,45,180)
UpperEyeLid.setRest(45)
UpperEyeLid.setInverted(False)
UpperEyeLid.setVelocity(-1)
UpperEyeLid.setAutoDisable(False)
# UpperEyeLid.rest()


print "--Lower Eyelids"
LowerEyeLid = Runtime.createAndStart("LowerEyeLid", "Servo")
# attach it to the pwm board - pin 10
LowerEyeLid.attach(Head,10)
LowerEyeLid.setMinMax(0,120)
LowerEyeLid.map(0,180,0,120)
LowerEyeLid.setRest(30)
LowerEyeLid.setInverted(False)
LowerEyeLid.setVelocity(-1)
LowerEyeLid.setAutoDisable(False)
# LowerEyeLid.rest()


print "--The Jaw"
Jaw = Runtime.createAndStart("Jaw", "Servo")
# attach it to the pwm board - pin 9
Jaw.attach(Head,9)
Jaw.setMinMax(0,180)
Jaw.map(0,180,1,180)
Jaw.setRest(90)
Jaw.setInverted(False)
Jaw.setVelocity(-1)
Jaw.setAutoDisable(True)
#Jaw.rest()


print "Head Yaw"
HeadYaw = Runtime.createAndStart("HeadYaw", "Servo")
# attach it to the pwm board - pin 8
HeadYaw.attach(Head,8)
HeadYaw.setMinMax(0,180)
HeadYaw.map(0,180,1,180)
HeadYaw.setRest(90)
HeadYaw.setInverted(False)
HeadYaw.setVelocity(120)
HeadYaw.setAutoDisable(True)
HeadYaw.rest()

#######################################################
#                                                     #
# Now lets define the servos attached to the back.    #
#                                                     #
#######################################################
print "-Back Servo Group"

print "--Head Pitch"
HeadPitch = Runtime.createAndStart("HeadPitch", "Servo")
# attach it to the pwm board - pin 7
HeadPitch.attach(Back,7)
HeadPitch.setMinMax(0,180)
HeadPitch.map(0,180,1,180)
HeadPitch.setRest(90)
HeadPitch.setInverted(False)
HeadPitch.setVelocity(120)
HeadPitch.setAutoDisable(True)
HeadPitch.rest()

print "--Head Roll"
HeadRoll = Runtime.createAndStart("HeadRoll", "Servo")
# attach it to the pwm board - pin 6
HeadRoll.attach(Back,6)
HeadRoll.setMinMax(0,180)
HeadRoll.map(0,180,1,180)
HeadRoll.setRest(90)
HeadRoll.setInverted(False)
HeadRoll.setVelocity(120)
HeadRoll.setAutoDisable(True)
HeadRoll.rest()

