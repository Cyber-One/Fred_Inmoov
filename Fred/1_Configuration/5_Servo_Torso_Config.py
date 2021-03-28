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

EnableTopStomach = False
TopStomachAttachment = "Back"    # "arduinoLeft"
TopStomachPin = 8               # 27
TopStomachMinPos = 0            # 60
TopStomachMaxPos = 180          # 120
TopStomachRestPos = 90          # 90

EnableMidStomach = False
MidStomachAttchment = "Back"    # "arduinoLeft"
MidStomachPin = 9               # 28
MidStomachMinPos = 0            # 60
MidStomachMaxPos = 180          # 120
MidStomachRestPos = 90          # 90

EnableRollStomach = False
RollStomachAttchment = "Back"    # Not Present
RollStomachPin = 10              # 
RollStomachMinPos = 0            # 
RollStomachMaxPos = 180          # 
RollStomachRestPos = 90          # 

