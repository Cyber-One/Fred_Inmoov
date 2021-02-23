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
# 7.Servo_LeftArm_Config.py                                  #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Servo Head Config"
##############################################################
#                                                            #
# Servo Left Arm Group                                       #
#                                                            #
##############################################################

EnableLeftOmoPlate = False
LeftOmoPlateAttachment = "Back" # "arduioLeft"
LeftOmoPlatePin = 15            # 11
LeftOmoPlateMinPos = 0          # 10
LeftOmoPlateMaxPos = 180        # 80
LeftOmoPlateRestPos = 90        # 10

EnableLeftShoulder = False
LeftShoulderAttachment = "Back" # "arduioLeft"
LeftShoulderPin = 14            # 10
LeftShoulderMinPos = 0          # 0
LeftShoulderMaxPos = 180        # 180
LeftShoulderRestPos = 90        # 30

EnableLeftRotate = False
LeftRotateAttachment = "Back"   # "arduioLeft"
LeftRotatePin = 13              # 9
LeftRotateMinPos = 0            # 40
LeftRotateMaxPin = 180          # 180
LeftRotateRestPOs = 90          # 90

EnableLeftBicep = False
LeftBicepAttachment = "LeftArm" # "arduioLeft"
LeftBicepPin = 1                # 8
LeftBicepMinPos = 0             # 0
LeftBicepMaxPos = 180           # 90
LeftBicepRestPos = 90           # 0
