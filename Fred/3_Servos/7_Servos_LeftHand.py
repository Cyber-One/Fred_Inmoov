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
# 7_Servos_LeftHand.py                                       #
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
execfile(RuningFolder+'/1_Configuration/9_Servo_LeftHand_Config.py')

if EnableLeftThumb == True:
    print "--Left Thumb"
    LeftThumb = Runtime.createAndStart("LeftThumb", "Servo")
    if LeftThumbAttachment == "Head":
        LeftThumb.attach(Head, LeftThumbPin)
    if LeftThumbAttachment == "Back":
        LeftThumb.attach(Back, LeftThumbPin)
    if LeftThumbAttachment == "RightArm":
        LeftThumb.attach(RightArm, LeftThumbPin)
    if LeftThumbAttachment == "LeftArm":
        LeftThumb.attach(LeftArm, LeftThumbPin)
    if LeftThumbAttachment == "arduinoLeft":
        LeftThumb.attach(arduinoLeft, LeftThumbPin)
    if LeftThumbAttachment == "arduinoRight":
        LeftThumb.attach(arduinoRight, LeftThumbPin)
    if LeftThumbAttachment == "arduinoNano":
        LeftThumb.attach(arduinoNano, LeftThumbPin)
    #LeftThumb.setMinMax(LeftThumbMinPos, LeftThumbMaxPos)
    LeftThumb.setMinMax(0, 100)
    if LeftThumbMinPos < LeftThumbMaxPos:
        LeftThumb.map(0, 100, LeftThumbMinPos, LeftThumbMaxPos)
        LeftThumb.setInverted(False)
    else:
        LeftThumb.map(0, 100, LeftThumbMaxPos, LeftThumbMinPos)
        LeftThumb.setInverted(True)
    LeftThumb.setRest(10)
    if MRL == "Nixie":
        LeftThumb.setSpeed(LeftThumbMaxSpeed)
    else:
        LeftThumb.setVelocity(LeftThumbMaxSpeed)
    LeftThumb.setAutoDisable(True)
    LeftThumb.rest()

if EnableLeftIndex == True:
    print "--Left Index"
    LeftIndex = Runtime.createAndStart("LeftIndex", "Servo")
    if LeftIndexAttachment == "Head":
        LeftIndex.attach(Head, LeftIndexPin)
    if LeftIndexAttachment == "Back":
        LeftIndex.attach(Back, LeftIndexPin)
    if LeftIndexAttachment == "RightArm":
        LeftIndex.attach(RightArm, LeftIndexPin)
    if LeftIndexAttachment == "LeftArm":
        LeftIndex.attach(LeftArm, LeftIndexPin)
    if LeftIndexAttachment == "arduinoLeft":
        LeftIndex.attach(arduinoLeft, LeftIndexPin)
    if LeftIndexAttachment == "arduinoRight":
        LeftIndex.attach(arduinoRight, LeftIndexPin)
    if LeftIndexAttachment == "arduinoNano":
        LeftIndex.attach(arduinoNano, LeftIndexPin)
    #LeftIndex.setMinMax(LeftIndexMinPos, LeftIndexMaxPos)
    LeftIndex.setMinMax(0, 100)
    if LeftIndexMinPos < LeftIndexMaxPos:
        LeftIndex.map(0, 100, LeftIndexMinPos, LeftIndexMaxPos)
        LeftIndex.setInverted(False)
    else:
        LeftIndex.map(0, 100, LeftIndexMaxPos, LeftIndexMinPos)
        LeftIndex.setInverted(True)
    LeftIndex.setRest(10)
    if MRL == "Nixie":
        LeftIndex.setSpeed(LeftIndexMaxSpeed)
    else:
        LeftIndex.setVelocity(LeftIndexMaxSpeed)
    LeftIndex.setAutoDisable(True)
    LeftIndex.rest()

if EnableLeftMajor == True:
    print "--Left Major"
    LeftMajor = Runtime.createAndStart("LeftMajor", "Servo")
    if LeftMajorAttachment == "Head":
        LeftMajor.attach(Head, LeftMajorPin)
    if LeftMajorAttachment == "Back":
        LeftMajor.attach(Back, LeftMajorPin)
    if LeftMajorAttachment == "RightArm":
        LeftMajor.attach(RightArm, LeftMajorPin)
    if LeftMajorAttachment == "LeftArm":
        LeftMajor.attach(LeftArm, LeftMajorPin)
    if LeftMajorAttachment == "arduinoLeft":
        LeftMajor.attach(arduinoLeft, LeftMajorPin)
    if LeftMajorAttachment == "arduinoRight":
        LeftMajor.attach(arduinoRight, LeftMajorPin)
    if LeftMajorAttachment == "arduinoNano":
        LeftMajor.attach(arduinoNano, LeftMajorPin)
    #LeftMajor.setMinMax(LeftMajorMinPos, LeftMajorMaxPos)
    LeftMajor.setMinMax(0, 100)
    if LeftMajorMinPos < LeftMajorMaxPos:
        LeftMajor.map(0, 100, LeftMajorMinPos, LeftMajorMaxPos)
        LeftMajor.setInverted(False)
    else:
        LeftMajor.map(0, 100, LeftMajorMinPos, LeftMajorMaxPos)
        LeftMajor.setInverted(True)
    LeftMajor.setRest(10)
    if MRL == "Nixie":
        LeftMajor.setSpeed(LeftMajorMaxSpeed)
    else:
        LeftMajor.setVelocity(LeftMajorMaxSpeed)
    LeftMajor.setAutoDisable(True)
    LeftMajor.rest()

if EnableLeftRing == True:
    print "--Left Ring"
    LeftRing = Runtime.createAndStart("LeftRing", "Servo")
    if LeftRingAttachment == "Head":
        LeftRing.attach(Head, LeftRingPin)
    if LeftRingAttachment == "Back":
        LeftRing.attach(Back, LeftRingPin)
    if LeftRingAttachment == "RightArm":
        LeftRing.attach(RightArm, LeftRingPin)
    if LeftRingAttachment == "LeftArm":
        LeftRing.attach(LeftArm, LeftRingPin)
    if LeftRingAttachment == "arduinoLeft":
        LeftRing.attach(arduinoLeft, LeftRingPin)
    if LeftRingAttachment == "arduinoRight":
        LeftRing.attach(arduinoRight, LeftRingPin)
    if LeftRingAttachment == "arduinoNano":
        LeftRing.attach(arduinoNano, LeftRingPin)
    #LeftRing.setMinMax(LeftRingMinPos, LeftRingMaxPos)
    LeftRing.setMinMax(0, 100)
    if LeftRingMinPos < LeftRingMaxPos:
        LeftRing.map(0, 100, LeftRingMinPos, LeftRingMaxPos)
        LeftRing.setInverted(False)
    else:
        LeftRing.map(0, 100, LeftRingMinPos, LeftRingMaxPos)
        LeftRing.setInverted(True)
    LeftRing.setRest(10)
    if MRL == "Nixie":
        LeftRing.setSpeed(LeftRingMaxSpeed)
    else:
        LeftRing.setVelocity(LeftRingMaxSpeed)
    LeftRing.setAutoDisable(True)
    LeftRing.rest()

if EnableLeftPinky == True:
    print "--Left Pinky"
    LeftPinky = Runtime.createAndStart("LeftPinky", "Servo")
    if LeftPinkyAttachment == "Head":
        LeftPinky.attach(Head, LeftPinkyPin)
    if LeftPinkyAttachment == "Back":
        LeftPinky.attach(Back, LeftPinkyPin)
    if LeftPinkyAttachment == "RightArm":
        LeftPinky.attach(RightArm, LeftPinkyPin)
    if LeftPinkyAttachment == "LeftArm":
        LeftPinky.attach(LeftArm, LeftPinkyPin)
    if LeftPinkyAttachment == "arduinoLeft":
        LeftPinky.attach(arduinoLeft, LeftPinkyPin)
    if LeftPinkyAttachment == "arduinoRight":
        LeftPinky.attach(arduinoRight, LeftPinkyPin)
    if LeftPinkyAttachment == "arduinoNano":
        LeftPinky.attach(arduinoNano, LeftPinkyPin)
    #LeftPinky.setMinMax(LeftPinkyMinPos, LeftPinkyMaxPos)
    LeftPinky.setMinMax(0, 100)
    if LeftPinkyMinPos < LeftPinkyMaxPos:
        LeftPinky.map(0, 100, LeftPinkyMinPos, LeftPinkyMaxPos)
        RightPinky.setInverted(False)
    else:
        LeftPinky.map(0, 100, LeftPinkyMinPos, LeftPinkyMaxPos)
        RightPinky.setInverted(True)
    LeftPinky.setRest(10)
    if MRL == "Nixie":
        LeftPinky.setSpeed(LeftPinkyMaxSpeed)
    else:
        LeftPinky.setVelocity(LeftPinkyMaxSpeed)
    LeftPinky.setAutoDisable(True)
    LeftPinky.rest()

if EnableLeftWrist == True:
    print "--Left Wrist"
    LeftWrist = Runtime.createAndStart("LeftWrist", "Servo")
    if LeftWristAttachment == "Head":
        LeftWrist.attach(Head, LeftWristPin)
    if LeftWristAttachment == "Back":
        LeftWrist.attach(Back, LeftWristPin)
    if LeftWristAttachment == "RightArm":
        LeftWrist.attach(RightArm, LeftWristPin)
    if LeftWristAttachment == "LeftArm":
        LeftWrist.attach(LeftArm, LeftWristPin)
    if LeftWristAttachment == "arduinoLeft":
        LeftWrist.attach(arduinoLeft, LeftWristPin)
    if LeftWristAttachment == "arduinoRight":
        LeftWrist.attach(arduinoRight, LeftWristPin)
    if LeftWristAttachment == "arduinoNano":
        LeftWrist.attach(arduinoNano, LeftWristPin)
    #LeftWrist.setMinMax(LeftWristMinPos, LeftWristMaxPos)
    LeftWrist.setMinMax(0, 100)
    if LeftWristMinPos < LeftWristMaxPos:
        LeftWrist.map(0, 100, LeftWristMinPos, LeftWristMaxPos)
        LeftWrist.setInverted(False)
    else:
        LeftWrist.map(0, 100, LeftWristMinPos, LeftWristMaxPos)
        LeftWrist.setInverted(True)
    LeftWrist.setRest(10)
    if MRL == "Nixie":
        LeftWrist.setSpeed(LeftWristMaxSpeed)
    else:
        LeftWrist.setVelocity(LeftWristMaxSpeed)
    LeftWrist.setAutoDisable(True)
    LeftWrist.rest()
