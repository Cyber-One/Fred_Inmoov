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
# 6_Life_Functions/2_Eye_Lids.py                             #
# This file is to Simulate life movements associated with    #
# the eye lids                                               #
#                                                            #
##############################################################
import math
import time
import random

# General eye lid functions
# because there are so many possible configureations, we need to consider a standard set
# of function to implement the eye lids movements.
# Here we define the general ryr lids open and closed as well as half way and wink commands.
# These functions can be called at any time, and won't crash is the feature is not supported.

def UpperEyeLidsOpen():
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(100) # open the right upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(100) # open the left upper eye lid

def UpperEyeLidsMidway(midPos):
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(midPos) # Move to mid pos the right upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(midPos) # close the upper eye lid

def UpperEyeLidsClose():
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(0) # close the right Upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(0) # close the left Upper eye lid

def LowerEyeLidsOpen():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(100) # open the right Lower eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(100) # open the left Lower eye lid

def LowerEyeLidsMidway(midPos):
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(midPos) # Move to mid pos the right upper eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(midPos) # close the upper eye lid

def LowerEyeLidsClose():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(0) # close the right lower eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(0) # close the left lower eye lid

# The wink function only work if the left and right eye lids
# are driven by different servos.
# if for example you are using the Dakota76 Advance eyes, then
# WinkRightEye will blink and WinkLeftEye will have no action
# at all.
def WinkLeftEye():
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(0) # close the left lower eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(0) # close the left Upper eye lid
    time.sleep(0.5)
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(100) # open the left Lower eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(100) # open the left upper eye lid

def WinkRightEye():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(0) # close the Right lower eye lid
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(0) # close the Right Upper eye lid
    time.sleep(0.5)
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(100) # open the Right Lower eye lid
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(100) # open the Right upper eye lid

