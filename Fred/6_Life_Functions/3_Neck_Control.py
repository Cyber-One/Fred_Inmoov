##############################################################
#                                                            #
# Program Code for Fred Inmoov                               #
# Of the Cyber_One YouTube Channel                           #
# https://www.youtube.com/cyber_one                          #
#                                                            #
# This is version 5                                          #
# Divided up into sub programs                               #
# Coded for the Nixie Version of MyRobotLab.                 #
#                                                            #
# Running on MyRobotLab (MRL) http://myrobotlab.org/         #
# Fred in a modified Inmmov robot, you can find all the      #
# origonal files on the Inmoov web site. http://inmoov.fr/   #
#                                                            #
# 6_Life_Functions/3_Neck_Control.py                         #
# This file is to Simulate life movements associated with    #
# the Neck                                                   #
#                                                            #
##############################################################
import math
import time

# Pan and Tilt are the common methods of controlling a camera.
# normally, you would have a rotating base and the place a tilt mechinism on the pan base.
# we have a Pitch and Roll with the Yaw on top of that.
# When we look up at 20 and then turn the head 90 to the left,
# the head will end up with a tilt of 0 but the head will roll 20
# to overcome this we need a Pan and Tilt translation.
# This function assumes that 0, 0, 0 is facing straight ahead with tilt and roll level.
def HeadPanTilt(Pan, Tilt, Roll):
    print "PanTilt( ", Pan, ", ", Tilt, ", ", Roll, ")"
    PanTo = Pan + 50.0
    print "Panning To ", PanTo
    if EnableHeadYaw == True:
        HeadYaw.moveTo(PanTo)
    PanRadians = math.radians(Pan)
    print "Thats ", PanRadians, "Radians"
    if EnableHeadPitch == True:
        HeadPitch.moveTo(50+(Tilt*math.cos(PanRadians) + Roll*math.sin(PanRadians)))
    if EnableHeadRoll == True:
        HeadRoll.moveTo(50+(Tilt*math.sin(PanRadians) + Roll*math.cos(PanRadians)))
    print "PanTilt finished"

# This group of methods allow you to control one virtual axis
# at a time, you pass the new value and it grabs the last
# known positions of the other axis.
def HeadPanTo(NewPan):
    global HeadPanPos
    global HeadTiltPos
    global HeadRollPos
    HeadPanPos = NewPan
    if HeadPanPos < -50: 
        HeadPanPos = -50
    if HeadPanPos > 50: 
        HeadPanPos = 50
    HeadPanTilt(HeadPanTilt, HeadTiltPos, HeadRollPos)

def HeadTiltTo(NewTilt):
    global HeadPanPos
    global HeadTiltPos
    global HeadRollPos
    HeadTiltPos = NewTilt
    if HeadTiltPos < -50: 
        HeadTiltPos = -50
    if HeadTiltPos > 50: 
        HeadTiltPos = 50
    HeadPanTilt(HeadPanTilt, HeadTiltPos, HeadRollPos)

def HeadRollTo(NewRoll):
    global HeadPanPos
    global HeadTiltPos
    global HeadRollPos
    HeadRollPos = NewRoll
    if HeadRollPos < -50: 
        HeadRollPos = -50
    if HeadRollPos > 50: 
        HeadRollPos = 50
    HeadPanTilt(HeadPanTilt, HeadTiltPos, HeadRollPos)

# This group of Methods will add a value to the current
# virtual axis one at a time.  The other values are grabbed
# from memory
def HeadPan(NewPan):
    global HeadPanPos
    global HeadTiltPos
    global HeadRollPos
    HeadPanPos = HeadPanPos + NewPan
    if HeadPanPos < -50: 
        HeadPanPos = -50
    if HeadPanPos > 50: 
        HeadPanPos = 50
    HeadPanTilt(HeadPanTilt, HeadTiltPos, HeadRollPos)

def HeadTilt(NewTilt):
    global HeadPanPos
    global HeadTiltPos
    global HeadRollPos
    HeadTiltPos = HeadTiltPos + NewTilt
    if HeadTiltPos < -50: 
        HeadTiltPos = -50
    if HeadTiltPos > 50: 
        HeadTiltPos = 50
    HeadPanTilt(HeadPanTilt, HeadTiltPos, HeadRollPos)

def HeadRoll(NewRoll):
    global HeadPanPos
    global HeadTiltPos
    global HeadRollPos
    HeadRollPos = HeadRollPos + NewRoll
    if HeadRollPos < -50: 
        HeadRollPos = -50
    if HeadRollPos > 50: 
        HeadRollPos = 50
    HeadPanTilt(HeadPanTilt, HeadTiltPos, HeadRollPos)
