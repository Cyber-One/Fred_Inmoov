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
# 8_Servo_RightHand_Config.py                                #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Servo Head Config"
##############################################################
#                                                            #
# Servo Right Hand Group                                     #
#                                                            #
##############################################################

EnableRightThumb = False
RightThumbAttachment ="RightArm"# "arduioRight"
RightThumbPin = 2               # 2
RightThumbMinPos = 0            # 0
RightThumbMaxPos = 180          # 180
RightThumbMaxSpeed = 120        # 

EnableRightIndex = False
RightIndexAttachment ="RightArm"# "arduioRight"
RightIndexPin = 2               # 3
RightIndexMinPos = 0            # 0
RightIndexMaxPos = 180          # 180
RightIndexMaxSpeed = 120        # 

EnableRightMajor = False
RightMajorAttachment ="RightArm"# "arduioRight"
RightMajorPin = 2               # 4
RightMajorMinPos = 0            # 0
RightMajorMaxPos = 180          # 180
RightMajorMaxSpeed = 120        # 

EnableRightRing = False
RightRingAttachment = "RightArm"# "arduioRight"
RightRingPin = 2                # 5
RightRingMinPos = 0             # 0
RightRingMaxPos = 180           # 180
RightRingMaxSpeed = 120         # 

EnableRightPinky = False
RightPinkyAttachment ="RightArm"# "arduioRight"
RightPinkyPin = 2               # 6
RightPinkyMinPos = 0            # 0
RightPinkyMaxPos = 180          # 180
RightPinkyMaxSpeed = 120        # 

EnableRightWrist = False
RightWristAttachment ="RightArm"# "arduioRight"
RightWristPin = 2               # 7
RightWristMinPos = 0            # 0
RightWristMaxPos = 180          # 180
RightWristMaxSpeed = 120        # 
