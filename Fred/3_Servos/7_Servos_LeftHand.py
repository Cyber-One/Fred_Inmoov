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
# 7_Servos_LeftHand.py                                          #
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
execfile(RuningFolder+'/1_Configuration/9_Servo_LeftHand_Config.py')

#################################################################
# Servo for the Left Thumb, Min is the hand fully Open.         #
#################################################################
EnableLeftThumb = TestServoControllerExists(LeftThumbAttachment, EnableLeftThumb)
if EnableLeftThumb == True:
    print "--Left Thumb"
    LeftThumb = Runtime.createAndStart("LeftThumb", "Servo")
    LeftThumb.attach(runtime.getService(LeftThumbAttachment), LeftThumbPin)
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

#################################################################
# Servo for the Left Index Finger, Min is the hand fully Open.  #
#################################################################
EnableLeftIndex = TestServoControllerExists(LeftIndexAttachment, EnableLeftIndex)
if EnableLeftIndex == True:
    print "--Left Index"
    LeftIndex = Runtime.createAndStart("LeftIndex", "Servo")
    LeftIndex.attach(runtime.getService(LeftIndexAttachment), LeftIndexPin)
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

#################################################################
# Servo for the Left Middle Finger, Min is the hand fully Open. #
#################################################################
EnableLeftMajor = TestServoControllerExists(LeftMajorAttachment, EnableLeftMajor)
if EnableLeftMajor == True:
    print "--Left Major"
    LeftMajor = Runtime.createAndStart("LeftMajor", "Servo")
    LeftMajor.attach(runtime.getService(LeftMajorAttachment), LeftMajorPin)
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

#################################################################
# Servo for the Left Ring Fingure, Min is the hand fully Open.  #
#################################################################
EnableLeftRing = TestServoControllerExists(LeftRingAttachment, EnableLeftRing)
if EnableLeftRing == True:
    print "--Left Ring"
    LeftRing = Runtime.createAndStart("LeftRing", "Servo")
    LeftRing.attach(runtime.getService(LeftRingAttachment), LeftRingPin)
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

#################################################################
# Servo for the Left Little Fingure, Min is the hand fully Open.#
#################################################################
EnableLeftPinky = TestServoControllerExists(LeftPinkyAttachment, EnableLeftPinky)
if EnableLeftPinky == True:
    print "--Left Pinky"
    LeftPinky = Runtime.createAndStart("LeftPinky", "Servo")
    LeftPinky.attach(runtime.getService(LeftPinkyAttachment), LeftPinkyPin)
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

#################################################################
# Servo for the Left Wrist.                                     #
#################################################################
EnableLeftWrist = TestServoControllerExists(LeftWristAttachment, EnableLeftWrist)
if EnableLeftWrist == True:
    print "--Left Wrist"
    LeftWrist = Runtime.createAndStart("LeftWrist", "Servo")
    LeftWrist.attach(runtime.getService(LeftWristAttachment), LeftWristPin)
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
