#################################################################
#                                                               #
# Program Code for Fred Inmoov                                  #
# Of the Cyber_One YouTube Channel                              #
# https://www.youtube.com/cyber_one                             #
#                                                               #
# This is version 5                                             #
# Divided up into sub programs                                  #
# Coded for the Nixie Version of MyRobotLab.                    #
#                                                               #
# Running on MyRobotLab (MRL) http://myrobotlab.org/            #
# Fred in a modified Inmmov robot, you can find all the         #
# origonal files on the Inmoov web site. http://inmoov.fr/      #
#                                                               #
# 2_Servos_Neck.py                                              #
# This file is to start all the servos used in the Robot        #
#                                                               #
#################################################################

print "Starting the various Servos Services"
#################################################################
#                                                               #
# Servo Neck Group                                              #
#                                                               #
#################################################################
# Refer to the /1_Configuration/4_Servo_Neck_Config.py for      #
# more information on what each of these servos are for.        #
# Load the configuration for the Servos_Head.                   #
#################################################################
execfile(RuningFolder+'/1_Configuration/4_Servo_Neck_Config.py')

#################################################################
# Head Yaw allows the head to turn left and right.              #
#################################################################
EnableHeadYaw = TestServoControllerExists(HeadYawAttachment, EnableHeadYaw)
if EnableHeadYaw == True:
    print "Head Yaw"
    HeadYaw = Runtime.createAndStart("HeadYaw", "Servo")
    HeadYaw.attach(runtime.getService(HeadYawAttachment), HeadYawPin)
    #HeadYaw.setMinMax(HeadYawMinPos, HeadYawMaxPos)
    HeadYaw.setMinMax(0, 100)
    # This next if statement is looking for an inverted servo
    if HeadYawMinPos < HeadYawMaxPos:
        HeadYaw.map(0, 100, HeadYawMinPos, HeadYawMaxPos)
        HeadYaw.setInverted(False)
    else:
        HeadYaw.map(0, 100, HeadYawMaxPos, HeadYawMinPos)
        HeadYaw.setInverted(True)
    HeadYaw.setRest(50)
    if MRL == "Nixie":
        HeadYaw.setSpeed(HeadYawMaxSpeed)
    else:
        HeadYaw.setVelocity(HeadYawMaxSpeed) ## max velocity
    HeadYaw.setAutoDisable(True)
    HeadYaw.rest()

#################################################################
# Head Pitch allows the head to turn up and down.               #
#################################################################
EnableHeadPitch = TestServoControllerExists(HeadPitchAttachment, EnableHeadPitch)
if EnableHeadPitch == True:
    print "--Head Pitch"
    HeadPitch = Runtime.createAndStart("HeadPitch", "Servo")
    HeadPitch.attach(runtime.getService(HeadPitchAttachment), HeadPitchPin)
    HeadPitch.setMinMax(0, 100)
    if HeadPitchMinPos < HeadPitchMaxPos:
        HeadPitch.map(0, 100, HeadPitchMinPos, HeadPitchMaxPos)
        HeadPitch.setInverted(False)
    else:
        HeadPitch.map(0, 100, HeadPitchMinPos, HeadPitchMaxPos)
        HeadPitch.setInverted(True)
    HeadPitch.setRest(50)
    if MRL == "Nixie":
        HeadPitch.setSpeed(HeadPitchMaxSpeed)
    else:
        HeadPitch.setVelocity(HeadPitchMaxSpeed) ## max velocity
    HeadPitch.setAutoDisable(True)
    HeadPitch.rest()

#################################################################
# Head Roll allows the head to roll from left to right.         #
#################################################################
EnableHeadRoll = TestServoControllerExists(HeadRollAttachment, EnableHeadRoll)
if EnableHeadRoll == True:
    print "--Head Roll"
    HeadRoll = Runtime.createAndStart("HeadRoll", "Servo")
    HeadRoll.attach(runtime.getService(HeadRollAttachment), HeadRollPin)
    HeadRoll.setMinMax(0, 100)
    if HeadRollMinPos < HeadRollMaxPos:
        HeadRoll.map(0, 100, HeadRollMinPos, HeadRollMaxPos)
        HeadRoll.setInverted(False)
    else:
        HeadRoll.map(0, 100, HeadRollMaxPos, HeadRollMinPos)
        HeadRoll.setInverted(False)
    HeadRoll.setRest(50)
    if MRL == "Nixie":
        HeadRoll.setSpeed(HeadRollMaxSpeed)
    else:
        HeadRoll.setVelocity(HeadRollMaxSpeed) ## max velocity
    HeadRoll.setAutoDisable(True)
    HeadRoll.rest()
