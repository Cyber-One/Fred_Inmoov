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

# This method mostly makes sure you dont exceed the valid range.
def EyesPanTo(NewPan):
    global EyesPanPos
    global EyesTiltPos
    EyesPanPos = NewPan
    if EyesPanPos < -50: 
        EyesPanPos = -50
    if EyesPanPos > 50: 
        EyesPanPos = 50
    eyesLR(EyesPanPos)
    eyesUD(EyesTiltPos)

# This method mostly makes sure you dont exceed the valid range.
def EyesTiltTo(NewTilt):
    global EyesPanPos
    global EyesTiltPos
    EyesTiltPos = NewTilt
    if EyesTiltPos < -50: 
        EyesTiltPos = -50
    if EyesTiltPos > 50: 
        EyesTiltPos = 50
    eyesLR(EyesPanPos)
    eyesUD(EyesTiltPos)

# This group of Methods will add a value to the current
# virtual axis one at a time.  The other values are grabbed
# from memory
def EyesPan(NewPan):
    global EyesPanPos
    global EyesTiltPos
    EyesPanPos = EyesPanPos + NewPan
    if EyesPanPos < -50: 
        EyesPanPos = -50
    if EyesPanPos > 50: 
        EyesPanPos = 50
    eyesLR(EyesPanPos)
    eyesUD(EyesTiltPos)

def EyesTilt(NewTilt):
    global EyesPanPos
    global EyesTiltPos
    EyesTiltPos = EyesTiltPos + NewTilt
    if EyesTiltPos < -50: 
        EyesTiltPos = -50
    if EyesTiltPos > 50: 
        EyesTiltPos = 50
    eyesLR(EyesPanPos)
    eyesUD(EyesTiltPos)


