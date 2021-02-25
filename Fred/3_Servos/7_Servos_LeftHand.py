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
    LeftThumb.setMinMax(LeftThumbMinPos, LeftThumbMaxPos)
    #LeftThumb.map(0, 100, LeftThumbMinPos, LeftThumbMaxPos)
    LeftThumb.setRest(LeftThumbRestPos)
    LeftThumb.setInverted(False)
    LeftThumb.setSpeed(120)
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
    LeftIndex.setMinMax(LeftIndexMinPos, LeftIndexMaxPos)
    #LeftIndex.map(0, 100, LeftIndexMinPos, LeftIndexMaxPos)
    LeftIndex.setRest(LeftIndexRestPos)
    LeftIndex.setInverted(False)
    LeftIndex.setSpeed(120)
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
    LeftMajor.setMinMax(LeftMajorMinPos, LeftMajorMaxPos)
    #LeftMajor.map(0, 100, LeftMajorMinPos, LeftMajorMaxPos)
    LeftMajor.setRest(LeftMajorRestPos)
    LeftMajor.setInverted(False)
    LeftMajor.setSpeed(120)
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
    LeftRing.setMinMax(LeftRingMinPos, LeftRingMaxPos)
    #LeftRing.map(0, 100, LeftRingMinPos, LeftRingMaxPos)
    LeftRing.setRest(LeftRingRestPos)
    LeftRing.setInverted(False)
    LeftRing.setSpeed(120)
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
    LeftPinky.setMinMax(LeftPinkyMinPos, LeftPinkyMaxPos)
    #LeftPinky.map(0, 100, LeftPinkyMinPos, LeftPinkyMaxPos)
    LeftPinky.setRest(LeftPinkyRestPos)
    RightPinky.setInverted(False)
    LeftPinky.setSpeed(120)
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
    LeftWrist.setMinMax(LeftWristMinPos, LeftWristMaxPos)
    #LeftWrist.map(0, 100, LeftWristMinPos, LeftWristMaxPos)
    LeftWrist.setRest(LeftWristRestPos)
    LeftWrist.setInverted(False)
    LeftWrist.setSpeed(120)
    LeftWrist.setAutoDisable(True)
    LeftWrist.rest()
