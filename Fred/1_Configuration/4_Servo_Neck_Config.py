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
# 4_Servo_Neck_Config.py                                     #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Servo Neck Config"
##############################################################
#                                                            #
# Servo Neck Group                                           #
#                                                            #
##############################################################

EnableHeadYaw = False
HeadYawAttachment = "Head"      # "arduinoLeft"
HeadYawPin = 8                  # 13
HeadYawMinPos = 0               # 30
HeadYawMaxPos = 180             # 150
HeadYawRestPos = 90             # 90

EnableHeadPitch = False
HeadPitchAttachment = "Back"    # "arduinoLeft"
HeadPitchPin = 7                # 12
HeadPitchMinPos = 0             # 20
HeadPitchMaxPos = 180           # 160
HeadPitchRestPos = 90           # 90

EnableHeadRoll = False
HeadRollAttachment = "Back"     # "arduinoRight"
HeadRollPin = 6                 # 13
HeadRollMinPos = 0              # 60
HeadRollMaxPos = 180            # 130
HeadRollRestPos = 90            # 90

