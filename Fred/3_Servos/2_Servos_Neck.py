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
# 2_Servos_Neck.py                                           #
# This file is to start all the servos used in the Robot     #
#                                                            #
##############################################################
print "Starting the various Servos Services"
##############################################################
#                                                            #
# Servo Neck Group                                           #
#                                                            #
##############################################################
# Refer to the /1_Configuration/4_Servo_Neck_Config.py for
# more information on what each of these servos are for.

# Load the configuration for the Servos_Head.
execfile(RuningFolder+'/1_Configuration/4_Servo_Neck_Config.py')

# Test to make sure the configured controller is enabled.
if not ((HeadYawAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (HeadYawAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (HeadYawAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (HeadYawAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (HeadYawAttachment == "arduinoNano" and EnableArduinoNano) 
    or (HeadYawAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (HeadYawAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableHeadYaw = False

if EnableHeadYaw == True:
    print "Head Yaw"
    HeadYaw = Runtime.createAndStart("HeadYaw", "Servo")
    if HeadYawAttachment == "Head":
        HeadYaw.attach(Head, HeadYawPin)
    if HeadYawAttachment == "Back":
        HeadYaw.attach(Back, HeadYawPin)
    if HeadYawAttachment == "RightArm":
        HeadYaw.attach(RightArm, HeadYawPin)
    if HeadYawAttachment == "LeftArm":
        HeadYaw.attach(LeftArm, HeadYawPin)
    if HeadYawAttachment == "arduinoLeft":
        HeadYaw.attach(arduinoLeft, HeadYawPin)
    if HeadYawAttachment == "arduinoRight":
        HeadYaw.attach(arduinoRight, HeadYawPin)
    if HeadYawAttachment == "arduinoNano":
        HeadYaw.attach(arduinoNano, HeadYawPin)
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

# Test to make sure the configured controller is enabled.
if not ((HeadPitchAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (HeadPitchAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (HeadPitchAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (HeadPitchAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (HeadPitchAttachment == "arduinoNano" and EnableArduinoNano) 
    or (HeadPitchAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (HeadPitchAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableHeadPitch = False

if EnableHeadPitch == True:
    print "--Head Pitch"
    HeadPitch = Runtime.createAndStart("HeadPitch", "Servo")
    if HeadPitchAttachment == "Head":
        HeadPitch.attach(Head, HeadPitchPin)
    if HeadPitchAttachment == "Back":
        HeadPitch.attach(Back, HeadPitchPin)
    if HeadPitchAttachment == "RightArm":
        HeadPitch.attach(RightArm, HeadPitchPin)
    if HeadPitchAttachment == "LeftArm":
        HeadPitch.attach(LeftArm, HeadPitchPin)
    if HeadPitchAttachment == "arduinoLeft":
        HeadPitch.attach(arduinoLeft, HeadPitchPin)
    if HeadPitchAttachment == "arduinoRight":
        HeadPitch.attach(arduinoRight, HeadPitchPin)
    if HeadPitchAttachment == "arduinoNano":
        HeadPitch.attach(arduinoNano, HeadPitchPin)
    #HeadPitch.setMinMax(HeadPitchMinPos, HeadPitchMaxPos)
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

# Test to make sure the configured controller is enabled.
if not ((HeadRollAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (HeadRollAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (HeadRollAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (HeadRollAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (HeadRollAttachment == "arduinoNano" and EnableArduinoNano) 
    or (HeadRollAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (HeadRollAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableHeadRoll = False

if EnableHeadRoll == True:
    print "--Head Roll"
    HeadRoll = Runtime.createAndStart("HeadRoll", "Servo")
    if HeadRollAttachment == "Head":
        HeadRoll.attach(Head, HeadRollPin)
    if HeadRollAttachment == "Back":
        HeadRoll.attach(Back, HeadRollPin)
    if HeadRollAttachment == "RightArm":
        HeadRoll.attach(RightArm, HeadRollPin)
    if HeadRollAttachment == "LeftArm":
        HeadRoll.attach(LeftArm, HeadRollPin)
    if HeadRollAttachment == "arduinoLeft":
        HeadRoll.attach(arduinoLeft, HeadRollPin)
    if HeadRollAttachment == "arduinoRight":
        HeadRoll.attach(arduinoRight, HeadRollPin)
    if HeadRollAttachment == "arduinoNano":
        HeadRoll.attach(arduinoNano, HeadRollPin)
    #HeadRoll.setMinMax(HeadRollMinPos, HeadRollMaxPos)
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
