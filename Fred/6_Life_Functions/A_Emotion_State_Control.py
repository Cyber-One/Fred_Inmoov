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
# 6_Life_Functions/A_Emotion_State_Control.py                #
# This file is to Simulate life movements associated with    #
# the body of the robot                                      #
#                                                            #
##############################################################
import math
import time
import random

# The transition between emotional states needs to be
# controlled so that during a transition, the correct
# sub-functions can be called at the same time.

