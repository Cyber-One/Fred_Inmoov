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
    RightThumb.setMinMax(RightThumbMinPos, RightThumbMaxPos)
    #RightThumb.map(0, 100, RightThumbMinPos, RightThumbMaxPos)
    RightThumb.setRest(RightThumbRestPos)
    RightThumb.setInverted(False)
    RightThumb.setSpeed(120)
    RightThumb.setAutoDisable(True)
    RightThumb.rest()

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
    RightIndex.setMinMax(RightIndexMinPos, RightIndexMaxPos)
    #RightIndex.map(0, 100, RightIndexMinPos, RightIndexMaxPos)
    RightIndex.setRest(RightIndexRestPos)
    RightIndex.setInverted(False)
    RightIndex.setSpeed(120)
    RightIndex.setAutoDisable(True)
    RightIndex.rest()

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
    RightMajor.setMinMax(RightMajorMinPos, RightMajorMaxPos)
    #RightMajor.map(0, 100, RightMajorMinPos, RightMajorMaxPos)
    RightMajor.setRest(RightMajorRestPos)
    RightMajor.setInverted(False)
    RightMajor.setSpeed(120)
    RightMajor.setAutoDisable(True)
    RightMajor.rest()

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
    RightRing.setMinMax(RightRingMinPos, RightRingMaxPos)
    #RightRing.map(0, 100, RightRingMinPos, RightRingMaxPos)
    RightRing.setRest(RightRingRestPos)
    RightRing.setInverted(False)
    RightRing.setSpeed(120)
    RightRing.setAutoDisable(True)
    RightRing.rest()

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
    RightPinky.setMinMax(RightPinkyMinPos, RightPinkyMaxPos)
    #RightPinky.map(0, 100, RightPinkyMinPos, RightPinkyMaxPos)
    RightPinky.setRest(RightPinkyRestPos)
    RightPinky.setInverted(False)
    RightPinky.setSpeed(120)
    RightPinky.setAutoDisable(True)
    RightPinky.rest()

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
    RightWrist.setMinMax(RightWristMinPos, RightWristMaxPos)
    #RightWrist.map(0, 100, RightWristMinPos, RightWristMaxPos)
    RightWrist.setRest(RightWristRestPos)
    RightWrist.setInverted(False)
    RightWrist.setSpeed(120)
    RightWrist.setAutoDisable(True)
    RightWrist.rest()
