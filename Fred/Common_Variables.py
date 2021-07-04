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
# Common_Variables.py                                        #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Common Variables"
##############################################################
#                                                            #
# System wide global variable creation                       #
#                                                            #
##############################################################

# when the sleep timer is enabled, this allows the program to
# know when the robot is sleeping and when it's awake.
Awake = True                

# to help with some life functions, we turn on this value while
# our robot is busy talking.
isTalking = False

# This is a global direction for looking with the range
# -50 - +50 the position of 0 is centred with reference
# to the lower stomach of the standard Inmoov build.
# the full range of motion of the -50 - +50 or 100 units
# includes all 3 of the servos for Pan, (Eyes-X,
# Neck-Yaw and Lower-Stomach) and the 2 servos for the
# Tilt, (Eyes-Y and Neck-Pitch)
# These variables are used for the microgesture controllers
# positioning system.
LookPositionPan = 0
LookPositionTilt = 0

# To simplify the head movements, we need to keep track of
# where the head is pointed, for that we use following variables
EyesPanPos = 0
EyesTiltPos = 0

# To simplify the head movements, we need to keep track of
# where the head is pointed, for that we use following variables
HeadPanPos = 0
HeadTiltPos = 0
HeadRollPos = 0

# To simplify the torso movements, we need to keep track of
# where the torso is pointed, for that we use following variables
TorsoPanPos = 0
TorsoTiltPos = 0
TorsoRollPos = 0

# When using the PIR Sensor this value gets turned on while it
# is sensing movement.
PIRstate = False

# when using a pair of Ultrasonic sensors, we are best to test
# one side then the other, not the two together.
LastPingLeft = False

# These are the last values recorded with the Ultrasonic sensors
LastLeftPing = 0
LastRightPing = 0

# This is used to detect when the NeoPixel mode is being changed
# and allow appropriot actions to be taken.
LastStomachNeoPixelMode = 0
LastHeadNeoPixelMode = 0
