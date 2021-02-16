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
# Gestures.py
# This file perform standard actions such as nodding Yes
# or shaking the head No
#                                                     #
#######################################################
import time
print "Creating the various gestures to make the robot appear alive"

def Yes():
    PanTilt(0, -40, 0)
    time.sleep(0.3)
    PanTilt(0, 30, 0)
    time.sleep(0.3)
    PanTilt(0, -20, 0)
    time.sleep(0.4)
    PanTilt(0, 0, 0)

def No():
    PanTilt(40, 0, 0)
    time.sleep(0.3)
    PanTilt(-40, 0, 0)
    time.sleep(0.3)
    PanTilt(40, 0, 0)
    time.sleep(0.3)
    PanTilt(0, 0, 0)

