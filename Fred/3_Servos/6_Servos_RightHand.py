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
# 6_Servos_RightHand.py                                         #
# This file is to start all the servos used in the Robot        #
#                                                               #
#################################################################
print "Starting the various Servos Services"

#################################################################
#                                                               #
# Servo Right Hand Group                                        #
#                                                               #
#################################################################
# Load the configuration for the Servos_Head.                   #
#################################################################
execfile(RuningFolder+'/1_Configuration/8_Servo_RightHand_Config.py')

#################################################################
# Servo for the Right Thumb, Min is the hand fully Open.        #
#################################################################
EnableRightThumb = TestServoControllerExists(RightThumbAttachment, EnableRightThumb)
if EnableRightThumb == True:
    print "--Right Thumb"
    RightThumb = Runtime.createAndStart("RightThumb", "Servo")
    RightThumb.attach(runtime.getService(), RightThumbPin)
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

#################################################################
# Servo for the Right Index finger, Min is the hand fully Open. #
#################################################################
EnableRightIndex = TestServoControllerExists(RightIndexAttachment, EnableRightIndex)
if EnableRightIndex == True:
    print "--Right Index"
    RightIndex = Runtime.createAndStart("RightIndex", "Servo")
    RightIndex.attach(runtime.getService(RightIndexAttachment), RightIndexPin)
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

#################################################################
# Servo for the Right Middle finger, Min is the hand fully Open.#
#################################################################
EnableRightMajor = TestServoControllerExists(RightMajorAttachment, EnableRightMajor)
if EnableRightMajor == True:
    print "--Right Major"
    RightMajor = Runtime.createAndStart("RightMajor", "Servo")
    RightMajor.attach(runtime.getService(RightMajorAttachment), RightMajorPin)
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

#################################################################
# Servo for the Right Ring Finger, Min is the hand fully Open.  #
#################################################################
EnableRightRing = TestServoControllerExists(RightRingAttachment, EnableRightRing)
if EnableRightRing == True:
    print "--Right Ring"
    RightRing = Runtime.createAndStart("RightRing", "Servo")
    RightRing.attach(runtime.getService(RightRingAttachment), RightRingPin)
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

#################################################################
# Servo for the Right Little Finger, Min is the hand fully Open.#
#################################################################
EnableRightPinky = TestServoControllerExists(RightPinkyAttachment, EnableRightPinky)
if EnableRightPinky == True:
    print "--Right Pinky"
    RightPinky = Runtime.createAndStart("RightPinky", "Servo")
    RightPinky.attach(runtime.getService(RightPinkyAttachment), RightPinkyPin)
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

#################################################################
# Servo for the Right Wrist.                                    #
#################################################################
EnableRightWrist = TestServoControllerExists(RightWristAttachment, EnableRightWrist)
if EnableRightWrist == True:
    print "--Right Wrist"
    RightWrist = Runtime.createAndStart("RightWrist", "Servo")
    RightWrist.attach(runtime.getService(RightWristAttachment), RightWristPin)
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
