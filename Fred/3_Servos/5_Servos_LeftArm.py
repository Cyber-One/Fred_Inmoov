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
# 5_Servos_LeftArm.py                                           #
# This file is to start all the servos used in the Robot        #
#                                                               #
#################################################################
print "Starting the various Servos Services"

#################################################################
#                                                               #
# Servo Right Arm Group                                         #
#                                                               #
#################################################################
# Load the configuration for the Servos_Head.                   #
#################################################################
execfile(RuningFolder+'/1_Configuration/7_Servo_LeftArm_Config.py')

#################################################################
# This servo lifts the arm sideway from the body.               #
#################################################################
EnableLeftOmoPlate = TestServoControllerExists(LeftOmoPlateAttachment, EnableLeftOmoPlate)
if EnableLeftOmoPlate == True:
    print "--Left OmoPlate"
    LeftOmoPlate = Runtime.createAndStart("LeftOmoPlate", "Servo")
    LeftOmoPlate.attach(runtime.getService(LeftOmoPlateAttachment), LeftOmoPlatePin)
    LeftOmoPlate.setMinMax(0, 100)
    if LeftOmoPlateMinPos < LeftOmoPlateMaxPos:
        LeftOmoPlate.map(0, 100, LeftOmoPlateMinPos, LeftOmoPlateMaxPos)
        LeftOmoPlate.setInverted(False)
    else:
        LeftOmoPlate.map(0, 100, LeftOmoPlateMaxPos, LeftOmoPlateMinPos)
        LeftOmoPlate.setInverted(True)
    LeftOmoPlate.setRest(0)
    if MRL == "Nixie":
        LeftOmoPlate.setSpeed(LeftOmoPlateMaxSpeed)
    else:
        LeftOmoPlate.setVelocity(LeftOmoPlateMaxSpeed)
    LeftOmoPlate.setAutoDisable(True)
    LeftOmoPlate.rest()

#################################################################
# This servo rotates the arm at the shoulder back and forwards. #
#################################################################
EnableLeftShoulder = TestServoControllerExists(LeftShoulderAttachment, EnableLeftShoulder)
if EnableLeftShoulder == True:
    print "--Left Shoulder"
    LeftShoulder = Runtime.createAndStart("LeftShoulder", "Servo")
    LeftShoulder.attach(runtime.getService(LeftShoulderAttachment), LeftShoulderPin)
    LeftShoulder.setMinMax(0, 100)
    if LeftShoulderMinPos < LeftShoulderMaxPos:
        LeftShoulder.map(0, 100, LeftShoulderMinPos, LeftShoulderMaxPos)
        LeftShoulder.setInverted(False)
    else:
        LeftShoulder.map(0, 100, LeftShoulderMaxPos, LeftShoulderMinPos)
        LeftShoulder.setInverted(True)
    LeftShoulder.setRest(16)
    if MRL == "Nixie":
        LeftShoulder.setSpeed(LeftShoulderMaxSpeed)
    else:
        LeftShoulder.setVelocity(LeftShoulderMaxSpeed)
    LeftShoulder.setAutoDisable(True)
    LeftShoulder.rest()

#################################################################
# This servo rotates the bicep changing the angle the elbow     #
# rotates.                                                      #
#################################################################
EnableLeftRotate = TestServoControllerExists(LeftRotateAttachment, EnableLeftRotate)

if EnableLeftRotate == True:
    print "--Left Rotate"
    LeftRotate = Runtime.createAndStart("LeftRotate", "Servo")
    LeftRotate.attach(runtime.getService(LeftRotateAttachment), LeftRotatePin)
    LeftRotate.setMinMax(0, 100)
    if LeftRotateMinPos < LeftRotateMaxPos:
        LeftRotate.map(0, 100, LeftRotateMinPos, LeftRotateMaxPos)
        LeftRotate.setInverted(False)
    else:
        LeftRotate.map(0, 100, LeftRotateMaxPos, LeftRotateMinPos)
        LeftRotate.setInverted(True)
    LeftRotate.setRest(50)
    if MRL == "Nixie":
        LeftRotate.setSpeed(LeftRotateMaxSpeed)
    else:
        LeftRotate.setVelocity(LeftRotateMaxSpeed)
    LeftRotate.setAutoDisable(True)
    LeftRotate.rest()

#################################################################
# This servo bends the and straightens the elbow joint.         #
#################################################################
EnableLeftBicep = TestServoControllerExists(LeftBicepAttachment, EnableLeftBicep)

if EnableLeftBicep == True:
    print "--Left Bicep"
    LeftBicep = Runtime.createAndStart("LeftBicep", "Servo")
    LeftBicep.attach(runtime.getService(LeftBicepAttachment), LeftBicepPin)
    LeftBicep.setMinMax(0, 100)
    if LeftBicepMinPos < LeftBicepMaxPos:
        LeftBicep.map(0, 100, LeftBicepMinPos, LeftBicepMaxPos)
        LeftBicep.setInverted(False)
    else:
        LeftBicep.map(0, 100, LeftBicepMaxPos, LeftBicepMinPos)
        LeftBicep.setInverted(True)
    LeftBicep.setRest(10)
    if MRL == "Nixie":
        LeftBicep.setSpeed(LeftBicepMaxSpeed)
    else:
        LeftBicep.setVelocity(LeftBicepMaxSpeed)
    LeftBicep.setAutoDisable(True)
    LeftBicep.rest()
