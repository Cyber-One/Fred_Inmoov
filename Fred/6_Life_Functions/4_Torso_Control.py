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
# 6_Life_Functions/4_Torso_Control.py                        #
# This file is to Simulate life movements associated with    #
# the body of the robot                                      #
#                                                            #
##############################################################
import math
import time
import random

# There are are two servos in the standard build of the
# Inmoov robot, the upper set of servos for the side to side
# tilt and the mid stomach rotation servos.
# However there have been two other builds I have seen that
# introduced a pitch movement.
# Bob Houston replace the upper stomach tilt system with a
# large ball joint, retaining the two side servos and adding
# two servos at the back for the pitch back and forward motion.
# Bartoz removed the two side servos and added a simple pivot
# at the front where the the certer bearing mount connected to
# the top of the mid stomach rotator.  He then placed two
# independant servos at the back on each side. Running both
# servos forward would tilt the torso forward, while running
# each of the servos in oposite directions caused the torso to
# tilt sideways.  You might say the control was either direct
# or differential.

# This function assumes that 0, 0, 0 is facing straight ahead with tilt and roll level.
def TorsoPanTilt(Pan, Tilt, Roll):
    print "TorsoPanTilt( ", Pan, ", ", Tilt, ", ", Roll, ")"
    PanTo = 50 + Pan
    print "Panning Torso To ", PanTo
    if EnableMidStomach == True:
        MidStomach.moveTo(PanTo)
    if TorsoType and EnablePitchStomach:
        Print "Still working on this :-)"
    else:
        if EnableTopStomach:
            RollTo = 50 + Roll
            TopStomach.moveTo(RollTo)
        if EnablePitchStomach:
            TiltTo = 50 + Tilt
            PitchStomach.moveTo(TiltTo)
    print "TorsoPanTilt finished"
