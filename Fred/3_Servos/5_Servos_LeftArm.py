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
# 5_Servos_LeftArm.py                                        #
# This file is to start all the servos used in the Robot     #
#                                                            #
##############################################################
print "Starting the various Servos Services"
##############################################################
#                                                            #
# Servo Right Arm Group                                      #
#                                                            #
##############################################################
# Load the configuration for the Servos_Head.
execfile(RuningFolder+'/1_Configuration/7_Servo_LeftArm_Config.py')

if EnableLeftOmoPlate == True:
    print "--Left OmoPlate"
    LeftOmoPlate = Runtime.createAndStart("LeftOmoPlate", "Servo")
    if LeftOmoPlateAttachment == "Head":
        LeftOmoPlate.attach(Head, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "Back":
        LeftOmoPlate.attach(Back, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "RightArm":
        LeftOmoPlate.attach(RightArm, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "LeftArm":
        LeftOmoPlate.attach(LeftArm, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "arduinoLeft":
        LeftOmoPlate.attach(arduinoLeft, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "arduinoRight":
        LeftOmoPlate.attach(arduinoRight, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "arduinoNano":
        LeftOmoPlate.attach(arduinoNano, LeftOmoPlatePin)
    #LeftOmoPlate.setMinMax(LeftOmoPlateMinPos, LeftOmoPlateMaxPos)
    LeftOmoPlate.setMinMax(0, 100)
    if LeftOmoPlateMinPos < LeftOmoPlateMaxPos:
        LeftOmoPlate.map(0, 100, LeftOmoPlateMinPos, LeftOmoPlateMaxPos)
        LeftOmoPlate.setInverted(False)
    else:
        LeftOmoPlate.map(0, 100, LeftOmoPlateMaxPos, LeftOmoPlateMinPos)
        LeftOmoPlate.setInverted(True)
    LeftOmoPlate.setRest(0)
    LeftOmoPlate.setSpeed(LeftOmoPlateMaxSpeed)
    LeftOmoPlate.setAutoDisable(True)
    LeftOmoPlate.rest()

if EnableLeftShoulder == True:
    print "--Left Shoulder"
    LeftShoulder = Runtime.createAndStart("LeftShoulder", "Servo")
    if LeftShoulderAttachment == "Head":
        LeftShoulder.attach(Head, LeftShoulderPin)
    if LeftShoulderAttachment == "Back":
        LeftShoulder.attach(Back, LeftShoulderPin)
    if LeftShoulderAttachment == "RightArm":
        LeftShoulder.attach(RightArm, LeftShoulderPin)
    if LeftShoulderAttachment == "LeftArm":
        LeftShoulder.attach(LeftArm, LeftShoulderPin)
    if LeftShoulderAttachment == "arduinoLeft":
        LeftShoulder.attach(arduinoLeft, LeftShoulderPin)
    if LeftShoulderAttachment == "arduinoRight":
        LeftShoulder.attach(arduinoRight, LeftShoulderPin)
    if LeftShoulderAttachment == "arduinoNano":
        LeftShoulder.attach(arduinoNano, LeftShoulderPin)
    #LeftShoulder.setMinMax(LeftShoulderMinPos, LeftShoulderMaxPos)
    LeftShoulder.setMinMax(0, 100)
    if LeftShoulderMinPos < LeftShoulderMaxPos:
        LeftShoulder.map(0, 100, LeftShoulderMinPos, LeftShoulderMaxPos)
        LeftShoulder.setInverted(False)
    else:
        LeftShoulder.map(0, 100, LeftShoulderMaxPos, LeftShoulderMinPos)
        LeftShoulder.setInverted(True)
    LeftShoulder.setRest(16)
    LeftShoulder.setSpeed(LeftShoulderMaxSpeed)
    LeftShoulder.setAutoDisable(True)
    LeftShoulder.rest()

if EnableLeftRotate == True:
    print "--Left Rotate"
    LeftRotate = Runtime.createAndStart("LeftRotate", "Servo")
    if LeftRotateAttachment == "Head":
        LeftRotate.attach(Head, LeftRotatePin)
    if LeftRotateAttachment == "Back":
        LeftRotate.attach(Back, LeftRotatePin)
    if LeftRotateAttachment == "RightArm":
        LeftRotate.attach(RightArm, LeftRotatePin)
    if LeftRotateAttachment == "LeftArm":
        LeftRotate.attach(LeftArm, LeftRotatePin)
    if LeftRotateAttachment == "arduinoLeft":
        LeftRotate.attach(arduinoLeft, LeftRotatePin)
    if LeftRotateAttachment == "arduinoRight":
        LeftRotate.attach(arduinoRight, LeftRotatePin)
    if LeftRotateAttachment == "arduinoNano":
        LeftRotate.attach(arduinoNano, LeftRotatePin)
    #LeftRotate.setMinMax(LeftRotateMinPos, LeftRotateMaxPos)
    LeftRotate.setMinMax(0, 100)
    if LeftRotateMinPos < LeftRotateMaxPos:
        LeftRotate.map(0, 100, LeftRotateMinPos, LeftRotateMaxPos)
        LeftRotate.setInverted(False)
    else:
        LeftRotate.map(0, 100, LeftRotateMaxPos, LeftRotateMinPos)
        LeftRotate.setInverted(True)
    LeftRotate.setRest(50)
    LeftRotate.setSpeed(LeftRotateMaxSpeed)
    LeftRotate.setAutoDisable(True)
    LeftRotate.rest()

if EnableLeftBicep == True:
    print "--Left Bicep"
    LeftBicep = Runtime.createAndStart("LeftBicep", "Servo")
    if LeftBicepAttachment == "Head":
        LeftBicep.attach(Head, LeftBicepPin)
    if LeftBicepAttachment == "Back":
        LeftBicep.attach(Back, LeftBicepPin)
    if LeftBicepAttachment == "RightArm":
        LeftBicep.attach(RightArm, LeftBicepPin)
    if LeftBicepAttachment == "LeftArm":
        LeftBicep.attach(LeftArm, LeftBicepPin)
    if LeftBicepAttachment == "arduinoLeft":
        LeftBicep.attach(arduinoLeft, LeftBicepPin)
    if LeftBicepAttachment == "arduinoRight":
        LeftBicep.attach(arduinoRight, LeftBicepPin)
    if LeftBicepAttachment == "arduinoNano":
        LeftBicep.attach(arduinoNano, LeftBicepPin)
    #LeftBicep.setMinMax(LeftBicepMinPos, LeftBicepMaxPos)
    LeftBicep.setMinMax(0, 100)
    if LeftBicepMinPos < LeftBicepMaxPos:
        LeftBicep.map(0, 100, LeftBicepMinPos, LeftBicepMaxPos)
        LeftBicep.setInverted(False)
    else:
        LeftBicep.map(0, 100, LeftBicepMaxPos, LeftBicepMinPos)
        LeftBicep.setInverted(True)
    LeftBicep.setRest(10)
    LeftBicep.setSpeed(LeftBicepMaxSpeed)
    LeftBicep.setAutoDisable(True)
    LeftBicep.rest()
