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
# 6_Servo_RightArm_Config.py                                 #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Servo Right Arm Config"
##############################################################
#                                                            #
# Servo Right Arm Group                                      #
#                                                            #
##############################################################

EnableRightOmoPlate = False
RightOmoPlateAttachment = "Back"# "arduionRight"
RightOmoPlatePin = 1            # 11
RightOmoPlateMinPos = 0         # 10
RightOmoPlateMaxPos = 180       # 80
RightOmoPlateRestPos = 90       # 10

EnableRightShoulder = False
RightShoulderAttachment="Back"  # "arduionRight"
RightShoulderPin = 2            # 10
RightShoulderMinPos = 0         # 0
RightShoulderMaxPos = 180       # 180
RightShoulderRestPos = 90       # 30

EnableRightRotate = False
RightRotateAttachment = "Back"  # "arduionRight"
RightRotatePin = 3              # 9
RightRotateMinPos = 0           # 40
RightRotateMaxPin = 180         # 180
RightRotateRestPOs = 90         # 90

EnableRightBicep = False
RightBicepAttachment ="RightArm"# "arduioRight"
RightBicepPin = 1               # 8
RightBicepMinPos = 0            # 0
RightBicepMaxPos = 180          # 90
RightBicepRestPos = 90          # 0
