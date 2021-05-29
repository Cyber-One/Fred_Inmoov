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
# 6_Servos_RightHand.py                                      #
# This file is to start all the servos used in the Robot     #
#                                                            #
##############################################################
print "Starting the various Servos Services"
##############################################################
#                                                            #
# Servo Right Hand Group                                     #
#                                                            #
##############################################################
# Load the configuration for the Servos_Head.
execfile(RuningFolder+'/1_Configuration/8_Servo_RightHand_Config.py')

# Test to make sure the configured controller is enabled.
if not ((RightThumbAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (RightThumbAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (RightThumbAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (RightThumbAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (RightThumbAttachment == "arduinoNano" and EnableArduinoNano) 
    or (RightThumbAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (RightThumbAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightThumb = False

if EnableRightThumb == True:
    print "--Right Thumb"
    RightThumb = Runtime.createAndStart("RightThumb", "Servo")
    if RightThumbAttachment == "Head":
        RightThumb.attach(Head, RightThumbPin)
    if RightThumbAttachment == "Back":
        RightThumb.attach(Back, RightThumbPin)
    if RightThumbAttachment == "RightArm":
        RightThumb.attach(RightArm, RightThumbPin)
    if RightThumbAttachment == "LeftArm":
        RightThumb.attach(LeftArm, RightThumbPin)
    if RightThumbAttachment == "arduinoLeft":
        RightThumb.attach(arduinoLeft, RightThumbPin)
    if RightThumbAttachment == "arduinoRight":
        RightThumb.attach(arduinoRight, RightThumbPin)
    if RightThumbAttachment == "arduinoNano":
        RightThumb.attach(arduinoNano, RightThumbPin)
    #RightThumb.setMinMax(RightThumbMinPos, RightThumbMaxPos)
    RightThumb.setMinMax(0, 100)
    if RightThumbMinPos < RightThumbMaxPos:
        RightThumb.map(0, 100, RightThumbMinPos, RightThumbMaxPos)
        RightThumb.setInverted(False)
    else:
        RightThumb.map(0, 100, RightThumbMaxPos, RightThumbMinPos)
        RightThumb.setInverted(True)
    RightThumb.setRest(10)
    if MRL == "Nixie":
        RightThumb.setSpeed(RightThumbMaxSpeed)
    else:
        RightThumb.setVelocity(RightThumbMaxSpeed)
    RightThumb.setAutoDisable(True)
    RightThumb.rest()

# Test to make sure the configured controller is enabled.
if not ((RightIndexAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (RightIndexAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (RightIndexAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (RightIndexAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (RightIndexAttachment == "arduinoNano" and EnableArduinoNano) 
    or (RightIndexAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (RightIndexAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightIndex = False

if EnableRightIndex == True:
    print "--Right Index"
    RightIndex = Runtime.createAndStart("RightIndex", "Servo")
    if RightIndexAttachment == "Head":
        RightIndex.attach(Head, RightIndexPin)
    if RightIndexAttachment == "Back":
        RightIndex.attach(Back, RightIndexPin)
    if RightIndexAttachment == "RightArm":
        RightIndex.attach(RightArm, RightIndexPin)
    if RightIndexAttachment == "LeftArm":
        RightIndex.attach(LeftArm, RightIndexPin)
    if RightIndexAttachment == "arduinoLeft":
        RightIndex.attach(arduinoLeft, RightIndexPin)
    if RightIndexAttachment == "arduinoRight":
        RightIndex.attach(arduinoRight, RightIndexPin)
    if RightIndexAttachment == "arduinoNano":
        RightIndex.attach(arduinoNano, RightIndexPin)
    #RightIndex.setMinMax(RightIndexMinPos, RightIndexMaxPos)
    RightIndex.setMinMax(0, 100)
    if RightIndexMinPos < RightIndexMaxPos:
        RightIndex.map(0, 100, RightIndexMinPos, RightIndexMaxPos)
        RightIndex.setInverted(False)
    else:
        RightIndex.map(0, 100, RightIndexMaxPos, RightIndexMinPos)
        RightIndex.setInverted(True)
    RightIndex.setRest(10)
    if MRL == "Nixie":
        RightIndex.setSpeed(RightIndexMaxSpeed)
    else:
        RightIndex.setVelocity(RightIndexMaxSpeed)
    RightIndex.setAutoDisable(True)
    RightIndex.rest()

# Test to make sure the configured controller is enabled.
if not ((RightMajorAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (RightMajorAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (RightMajorAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (RightMajorAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (RightMajorAttachment == "arduinoNano" and EnableArduinoNano) 
    or (RightMajorAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (RightMajorAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightMajor = False

if EnableRightMajor == True:
    print "--Right Major"
    RightMajor = Runtime.createAndStart("RightMajor", "Servo")
    if RightMajorAttachment == "Head":
        RightMajor.attach(Head, RightMajorPin)
    if RightMajorAttachment == "Back":
        RightMajor.attach(Back, RightMajorPin)
    if RightMajorAttachment == "RightArm":
        RightMajor.attach(RightArm, RightMajorPin)
    if RightMajorAttachment == "LeftArm":
        RightMajor.attach(LeftArm, RightMajorPin)
    if RightMajorAttachment == "arduinoLeft":
        RightMajor.attach(arduinoLeft, RightMajorPin)
    if RightMajorAttachment == "arduinoRight":
        RightMajor.attach(arduinoRight, RightMajorPin)
    if RightMajorAttachment == "arduinoNano":
        RightMajor.attach(arduinoNano, RightMajorPin)
    #RightMajor.setMinMax(RightMajorMinPos, RightMajorMaxPos)
    RightMajor.setMinMax(0, 100)
    if RightMajorMinPos < RightMajorMaxPos:
        RightMajor.map(0, 100, RightMajorMinPos, RightMajorMaxPos)
        RightMajor.setInverted(False)
    else:
        RightMajor.map(0, 100, RightMajorMaxPos, RightMajorMinPos)
        RightMajor.setInverted(True)
    RightMajor.setRest(10)
    if MRL == "Nixie":
        RightMajor.setSpeed(RightMajorMaxSpeed)
    else:
        RightMajor.setVelocity(RightMajorMaxSpeed)
    RightMajor.setAutoDisable(True)
    RightMajor.rest()

# Test to make sure the configured controller is enabled.
if not ((RightRingAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (RightRingAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (RightRingAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (RightRingAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (RightRingAttachment == "arduinoNano" and EnableArduinoNano) 
    or (RightRingAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (RightRingAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightRing = False

if EnableRightRing == True:
    print "--Right Ring"
    RightRing = Runtime.createAndStart("RightRing", "Servo")
    if RightRingAttachment == "Head":
        RightRing.attach(Head, RightRingPin)
    if RightRingAttachment == "Back":
        RightRing.attach(Back, RightRingPin)
    if RightRingAttachment == "RightArm":
        RightRing.attach(RightArm, RightRingPin)
    if RightRingAttachment == "LeftArm":
        RightRing.attach(LeftArm, RightRingPin)
    if RightRingAttachment == "arduinoLeft":
        RightRing.attach(arduinoLeft, RightRingPin)
    if RightRingAttachment == "arduinoRight":
        RightRing.attach(arduinoRight, RightRingPin)
    if RightRingAttachment == "arduinoNano":
        RightRing.attach(arduinoNano, RightRingPin)
    #RightRing.setMinMax(RightRingMinPos, RightRingMaxPos)
    RightRing.setMinMax(0, 100)
    if RightRingMinPos < RightRingMaxPos:
        RightRing.map(0, 100, RightRingMinPos, RightRingMaxPos)
        RightRing.setInverted(False)
    else:
        RightRing.map(0, 100, RightRingMaxPos, RightRingMinPos)
        RightRing.setInverted(True)
    RightRing.setRest(10)
    if MRL == "Nixie":
        RightRing.setSpeed(RightRingMaxSpeed)
    else:
        RightRing.setVelocity(RightRingMaxSpeed)
    RightRing.setAutoDisable(True)
    RightRing.rest()

# Test to make sure the configured controller is enabled.
if not ((RightPinkyAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (RightPinkyAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (RightPinkyAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (RightPinkyAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (RightPinkyAttachment == "arduinoNano" and EnableArduinoNano) 
    or (RightPinkyAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (RightPinkyAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightPinky = False

if EnableRightPinky == True:
    print "--Right Pinky"
    RightPinky = Runtime.createAndStart("RightPinky", "Servo")
    if RightPinkyAttachment == "Head":
        RightPinky.attach(Head, RightPinkyPin)
    if RightPinkyAttachment == "Back":
        RightPinky.attach(Back, RightPinkyPin)
    if RightPinkyAttachment == "RightArm":
        RightPinky.attach(RightArm, RightPinkyPin)
    if RightPinkyAttachment == "LeftArm":
        RightPinky.attach(LeftArm, RightPinkyPin)
    if RightPinkyAttachment == "arduinoLeft":
        RightPinky.attach(arduinoLeft, RightPinkyPin)
    if RightPinkyAttachment == "arduinoRight":
        RightPinky.attach(arduinoRight, RightPinkyPin)
    if RightPinkyAttachment == "arduinoNano":
        RightPinky.attach(arduinoNano, RightPinkyPin)
    #RightPinky.setMinMax(RightPinkyMinPos, RightPinkyMaxPos)
    RightPinky.setMinMax(0, 100)
    if RightPinkyMinPos < RightPinkyMaxPos:
        RightPinky.map(0, 100, RightPinkyMinPos, RightPinkyMaxPos)
        RightPinky.setInverted(False)
    else:
        RightPinky.map(0, 100, RightPinkyMaxPos, RightPinkyMinPos)
        RightPinky.setInverted(True)
    RightPinky.setRest(RightPinkyRestPos)
    if MRL == "Nixie":
        RightPinky.setSpeed(RightPinkyMaxSpeed)
    else:
        RightPinky.setVelocity(RightPinkyMaxSpeed)
    RightPinky.setAutoDisable(True)
    RightPinky.rest()

# Test to make sure the configured controller is enabled.
if not ((RightWristAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (RightWristAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (RightWristAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (RightWristAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (RightWristAttachment == "arduinoNano" and EnableArduinoNano) 
    or (RightWristAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (RightWristAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightWrist = False

if EnableRightWrist == True:
    print "--Right Wrist"
    RightWrist = Runtime.createAndStart("RightWrist", "Servo")
    if RightWristAttachment == "Head":
        RightWrist.attach(Head, RightWristPin)
    if RightWristAttachment == "Back":
        RightWrist.attach(Back, RightWristPin)
    if RightWristAttachment == "RightArm":
        RightWrist.attach(RightArm, RightWristPin)
    if RightWristAttachment == "LeftArm":
        RightWrist.attach(LeftArm, RightWristPin)
    if RightWristAttachment == "arduinoLeft":
        RightWrist.attach(arduinoLeft, RightWristPin)
    if RightWristAttachment == "arduinoRight":
        RightWrist.attach(arduinoRight, RightWristPin)
    if RightWristAttachment == "arduinoNano":
        RightWrist.attach(arduinoNano, RightWristPin)
    #RightWrist.setMinMax(RightWristMinPos, RightWristMaxPos)
    RightWrist.setMinMax(0, 100)
    if RightWristMinPos < RightWristMaxPos:
        RightWrist.map(0, 100, RightWristMinPos, RightWristMaxPos)
        RightWrist.setInverted(False)
    else:
        RightWrist.map(0, 100, RightWristMaxPos, RightWristMinPos)
        RightWrist.setInverted(True)
    RightWrist.setRest(RightWristRestPos)
    if MRL == "Nixie":
        RightWrist.setSpeed(RightWristMaxSpeed)
    else:
        RightWrist.setVelocity(RightWristMaxSpeed)
    RightWrist.setAutoDisable(True)
    RightWrist.rest()
