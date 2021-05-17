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
# 9_Servo_LeftHand_Config.py                                 #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Servo LeftHand Config"
##############################################################
#                                                            #
# Servo Left Hand Group                                      #
#                                                            #
##############################################################

EnableLeftThumb = False
LeftThumbAttachment = "LeftArm" # "arduioLeft"
LeftThumbPin = 2                # 2
LeftThumbMinPos = 0             # 0
LeftThumbMaxPos = 180           # 180
LeftThumbMaxSpeed = 120         # 

EnableLeftIndex = False
LeftIndexAttachment = "LeftArm" # "arduioLeft"
LeftIndexPin = 2                # 3
LeftIndexMinPos = 0             # 0
LeftIndexMaxPos = 180           # 180
LeftIndexMaxSpeed = 120         # 

EnableLeftMajor = False
LeftMajorAttachment = "LeftArm" # "arduioLeft"
LeftMajorPin = 2                # 4
LeftMajorMinPos = 0             # 0
LeftMajorMaxPos = 180           # 180
LeftMajorMaxSpeed = 120         # 

EnableLeftRing = False
LeftRingAttachment = "LeftArm"  # "arduioLeft"
LeftRingPin = 2                 # 5
LeftRingMinPos = 0              # 0
LeftRingMaxPos = 180            # 180
LeftRingMaxSpeed = 120          # 

EnableLeftPinky = False
LeftPinkyAttachment = "LeftArm" # "arduioLeft"
LeftPinkyPin = 2                # 6
LeftPinkyMinPos = 0             # 0
LeftPinkyMaxPos = 180           # 180
LeftPinkyMaxSpeed = 120         # 

EnableLeftWrist = False
LeftWristAttachment = "LeftArm" # "arduioLeft"
LeftWristPin = 2                # 7
LeftWristMinPos = 0             # 0
LeftWristMaxPos = 180           # 180
LeftWristMaxSpeed = 120         # 
