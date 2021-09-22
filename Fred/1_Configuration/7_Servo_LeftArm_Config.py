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
# This is where the configuration settings for the Left      #
# Arm Servos are located.                                    #
#                                                            #
##############################################################
print "Creating the Servo Left Arm Config"

# The Left OmoPlate lifts the arm at the shoulder out away
# from the body, this servo is located into the torso cavity
# and drives a rotary Piston setup in the Official InMoov Build.
EnableLeftOmoPlate = True
LeftOmoPlateAttachment = "Back" # "arduioLeft"
LeftOmoPlatePin = 15            # 11
LeftOmoPlateMinPos = 60         # 10
LeftOmoPlateMaxPos = 123        # 80
LeftOmoPlateMaxSpeed = 120      # 

# The left shoulder is a worm drive setup the pitches the
# left arm up in a forward direction.
EnableLeftShoulder = True
LeftShoulderAttachment = "Back" # "arduioLeft"
LeftShoulderPin = 14            # 10
LeftShoulderMinPos = 70         # 0
LeftShoulderMaxPos = 180        # 180
LeftShoulderMaxSpeed = 120      # 

# This servo is located near the shoulder servo and rotates
# the arm
EnableLeftRotate = True
LeftRotateAttachment = "Back"   # "arduioLeft"
LeftRotatePin = 13              # 9
LeftRotateMinPos = 16           # 40
LeftRotateMaxPos = 180          # 180
LeftRotateMaxSpeed = 120        # 

# This servo is located in the bicep and operates the elbow.
EnableLeftBicep = False
LeftBicepAttachment = "LeftArm" # "arduioLeft"
LeftBicepPin = 1                # 8
LeftBicepMinPos = 0             # 0
LeftBicepMaxPos = 180           # 90
LeftBicepMaxSpeed = 120         # 
