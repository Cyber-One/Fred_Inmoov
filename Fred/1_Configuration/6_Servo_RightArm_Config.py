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
# This is where the configuration settings for the Right     #
# Arm Servos are located.                                    #
#                                                            #
##############################################################
print "Creating the Servo Right Arm Config"

# The Right OmoPlate lifts the arm at the shoulder out away
# from the body, this servo is located into the torso cavity
# and drives a rotary Piston setup in the Official InMoov Build.
EnableRightOmoPlate = False
RightOmoPlateAttachment = "Back"# "arduionRight"
RightOmoPlatePin = 1            # 11
RightOmoPlateMinPos = 0         # 10
RightOmoPlateMaxPos = 180       # 80
RightOmoPlateMaxSpeed = 120     # 

# The right shoulder is a worm drive setup the pitches the
# right arm up in a forward direction.
EnableRightShoulder = False
RightShoulderAttachment="Back"  # "arduionRight"
RightShoulderPin = 2            # 10
RightShoulderMinPos = 0         # 0
RightShoulderMaxPos = 180       # 180
RightShoulderMaxSpeed = 120     # 

# This servo is located near the shoulder servo and rotates
# the arm
EnableRightRotate = False
RightRotateAttachment = "Back"  # "arduionRight"
RightRotatePin = 3              # 9
RightRotateMinPos = 0           # 40
RightRotateMaxPin = 180         # 180
RightRotateMaxSpeed = 120       # 

# This servo is located in the bicep and operates the elbow.
EnableRightBicep = False
RightBicepAttachment ="RightArm"# "arduioRight"
RightBicepPin = 1               # 8
RightBicepMinPos = 0            # 0
RightBicepMaxPos = 180          # 90
RightBicepMaxSpeed = 120        # 
