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

# To make is a bit easier to control, we define functions to
# move the two eyes together.
# if you have only the one servo for each of these axis, then
# don't worry, this code will ignore the one you don't have
# without crashing
# We will use 0 as the center position, negative number will
# look down or left.
# because we use the range 0:100 across all our servos, we
# know that adding 50 to a -50:50 will result in an
# output 0:100.
# EyeCrossAmount
def eyesLR(eyesLRpos):
    if EnableRightEyeX and EnableLeftEyeX:
        RightEyeLR.moveTo(50+eyesLRpos-EyeCrossAmount)
        LeftEyeLR.moveTo(50+eyesLRpos+EyeCrossAmount)
    else:
        if EnableRightEyeX:
            RightEyeLR.moveTo(50+eyesLRpos)
        if EnableLeftEyeX:
            LeftEyeLR.moveTo(50+eyesLRpos)

def EyesSetEyesCrossHome():
    EyeCrossAmount = DefaultEyeCrossAmount

def EyesSetEyesCross(Amount):
    EyeCrossAmount = Amount
    if EyeCrossAmount > 50:
        EyeCrossAmount = 50
    if EyeCrossAmount < DefaultEyeCrossAmount:
        EyeCrossAmount = DefaultEyeCrossAmount

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


# Eye lids can be used to convey a number of emotional states,
# Interest, confusion, anger and surprise just to name a few.
# There will need to be a fair amount of fine tuning here.

# General eye lid functions
# because there are so many possible configureations, we need to consider a standard set
# of function to implement the eye lids movements.
# Here we define the general eye lids open and closed as well as half way and wink commands.
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

# The normal position of the eye lids is not all the way open,
# but open enough to see the pupil, or let the camera see out.
# The amount the eye lids are open can be used to convey a
# degree of emotion.  The catch is, this position is relative
# to the eye ball which is a moving target.



