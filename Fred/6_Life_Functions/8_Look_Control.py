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
# 6_Life_Functions/Look_Control.py                           #
# This file is to Simulate life movements associated with    #
# looking about using the eyes, neck and torso movements     #
#                                                            #
##############################################################
import math
import time

# When you look at or track an object, your eyes first start
# to turn in that direction, followed by the head if the
# direction is over about 50% of the range your eye balls can
# turn.  This is to reduce the strain on your eye muscles.
# to make the robot appear to be more life like, we need to
# simulate the same movements.  This then makes it easier for
# tracking functions as these just call the torso look and can
# get the full range of eye, head and torso tracking from one
# set of controls.

# LookHeadPanTo(LookPan) will rotate both the neck and the
# eyeballs by the same percentage amount to the LookPan value.
# A value of 0.0 will center both the eye balls and the head.
def LookHeadPanTo(LookPan):
    EyesPanTo(LookPan)
    HeadPanTo(LookPan)

def LookHeadTiltTo(LookTilt):
    EyesTiltTo(LookTilt)
    HeadTiltTo(LookTilt)

# So looking at my particular build, the head has about
# 160 - 170 degrees of rotation.
# This results in the head auto centering regardless of what
# the RestPos is as I'm not calling that method anyway.
# I'm using 50 for the center as the input map on the servo
# is 0-100
# The eye ball has a rotational range of between 40 and 60
# Keep in mind my servo output config is currently in the
# rage 0 - 180 that means with the head movement combined
# with the Eye movement we get between 200 and 230 of rotation
# That means when I do a LookHeadPan(+10), with the Head at
# 0 pos, which translates to 50% and the eye balls at 70 pos,
# I can scale the input to move the eye balls to move to say
# to 75 pos and try and move the head to 3.125 to get the
# total desired movement.

def LookHeadPan(LookPan):
    global HeadPanPos
    global EyesPanPos
    global LookPositionPan
    if LookPan > 0:
        if (EyesPanPos + LookPan) > 25:
            HeadPanPos = HeadPanPos + (((EyesPanPos + LookPan) - 25) * 0.625)
            EyesPanPos = 25
        else:
            EyesPanPos = EyesPanPos + LookPan
    else:
        if (EyesPanPos + LookPan) < -25:
            HeadPanPos = HeadPanPos + (((EyesPanPos + LookPan) + 25) * 0.625)
            EyesPanPos = -25
        else:
            EyesPanPos = EyesPanPos + LookPan
    if HeadPanPos > 50:
        HeadPanPos = 50
    if HeadPanPos < -50:
        HeadPanPos = -50
    #print "LookHeadPan( ", HeadPanPos, ", ", EyesPanPos, ", ", LookPan, ")"
    EyesPanTo(EyesPanPos)
    HeadPanTo(HeadPanPos)

def LookHeadTilt(LookTilt):
    global HeadTiltPos
    global LookPositionTilt
    if LookTilt > 0:
        if (HeadTiltPos + LookTilt) > 25:
            LookPositionTilt = LookPositionTilt + (((HeadTiltPos + LookTilt) - 25) * 0.625)
            HeadTiltPos = 25
        else:
            HeadTiltPos = HeadTiltPos + LookTilt
    else:
        if (HeadTiltPos + LookTilt) < -25:
            LookPositionTilt = LookPositionTilt + (((HeadTiltPos + LookTilt) + 25) * 0.625)
            HeadTiltPos = -25
        else:
            HeadTiltPos = HeadTiltPos + LookTilt
    if LookPositionTilt > 50:
        LookPositionTilt = 50
    if LookPositionTilt < -50:
        LookPositionTilt = -50
    EyesTiltTo(HeadTiltPos)
    HeadTiltTo(LookPositionTilt)


