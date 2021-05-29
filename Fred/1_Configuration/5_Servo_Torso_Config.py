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
# 5_Servo_Torso_Config.py                                    #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Servo Head Config"
##############################################################
#                                                            #
# Servo Torso Group                                          #
#                                                            #
##############################################################

# The TopStomach servo allows the robot to roll it's torso
# left or right, it consists of two HS805BB, one with it's 
# electronics removed working as a slave to the other one.
# these drive a pair of pistons to rotate the torso about
# it's top stomach behind the neo pixel ring.
EnableTopStomach = True
TopStomachAttachment = "Back"    # "arduinoLeft"
TopStomachPin = 8                # 27
TopStomachMinPos = 80            # 60
TopStomachMaxPos = 135           # 120
TopStomachMaxSpeed = 120         # -1

# The MidStomach servos, a pair of HS805BB again configured
# as Master Slave, each drive a worm drive to rotate the body.
EnableMidStomach = False
MidStomachAttachment = "Back"    # "arduinoLeft"
MidStomachPin = 9                # 28
MidStomachMinPos = 0             # 60
MidStomachMaxPos = 180           # 120
MidStomachMaxSpeed = 120         # -1

# Not in the official list of parts, some builders have added
# the ability to pitch the body back and forward above the
# MidStomach rotator.
EnablePitchStomach = False
PitchStomachAttchment = "Back"    # Not Present
PitchStomachPin = 10              # 
PitchStomachMinPos = 0            # 
PitchStomachMaxPos = 180          # 
PitchStomachMaxSpeed = 120        # 

