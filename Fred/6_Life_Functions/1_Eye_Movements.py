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
# 6_Life_Functions/1_Eye_Movements.py                        #
# This file is to Simulate life movements associated with    #
# the eye balls.                                             #
#                                                            #
##############################################################
import math
import time
import random

# To make is a bit easier to control, we define functions to
# move the two eyes togeter.
# if you have only the one servo for each of these axis, then
# don't worry, this code will ignore the one you don't have
# without crashing
# Like the Pan, Tilt and Roll, we will use 0 as the center
# position and negative number will look down or left.
def eyesLR(eyesLRpos):
    if EnableRightEyeX == True:
        RightEyeLR.moveTo(50+eyesLRpos)
    if EnableLeftEyeX == True:
        LeftEyeLR.moveTo(50+eyesLRpos)

def eyesUD(eyesUDpos):
    if EnableRightEyeY == True:
        RightEyeUD.moveTo(50+eyesUDpos)
    if EnableLeftEyeY == True:
        LeftEyeUD.moveTo(50+eyesUDpos)

# We want the robot to appear to be more alive, and nothing
# speaks to being alive more than small random movements.
def MoveEyes(timedata):
    MoveEyesTimer.setInterval(random.randint(1000,2000))
    if Awake:
        #need to look at speed settings
        eyesLR(random.uniform(-20,20))
        eyesUD(random.uniform(-20,20))

def MoveEyesStart():
    if isTalking:
        MoveEyesTimer.stopClock()

def MoveEyesStop():
    eyesLR(0)
    eyesUD(0)

# The Clock service in MyRobotLab is designed to provide a
# repetative pulse type output each time the preset time
# has elapsed.  This is done 
if EnableRandomEyeMovements == True:
    MoveEyesTimer = Runtime.createAndStart("MoveEyesTimer","Clock")
    MoveEyesTimer.setInterval(random.randint(1000,2000))
    MoveEyesTimer.addListener("pulse", python.name, "MoveEyes")
    MoveEyesTimer.addListener("clockStarted", python.name, "MoveEyesStart")  
    MoveEyesTimer.addListener("clockStopped", python.name, "MoveEyesStop")

