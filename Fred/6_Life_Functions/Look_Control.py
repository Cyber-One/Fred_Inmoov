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
    HeadPanTo(NewPan)

def LookHeadTiltTo(LookTilt):
    EyesTiltTo(LookTilt)
    HeadTiltTo(LookTilt)

