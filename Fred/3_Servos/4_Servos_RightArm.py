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
# 4_Servos_RightArm.py                                       #
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
execfile(RuningFolder+'/1_Configuration/6_Servo_RightArm_Config.py')

if EnableRightOmoPlate == True:
    print "--Right OmoPlate"
    RightOmoPlate = Runtime.createAndStart("RightOmoPlate", "Servo")
    if RightOmoPlateAttachment == "Head":
        RightOmoPlate.attach(Head, RightOmoPlatePin)
    if RightOmoPlateAttachment == "Back":
        RightOmoPlate.attach(Back, RightOmoPlatePin)
    if RightOmoPlateAttachment == "RightArm":
        RightOmoPlate.attach(RightArm, RightOmoPlatePin)
    if RightOmoPlateAttachment == "LeftArm":
        RightOmoPlate.attach(LeftArm, RightOmoPlatePin)
    if RightOmoPlateAttachment == "arduinoLeft":
        RightOmoPlate.attach(arduinoLeft, RightOmoPlatePin)
    if RightOmoPlateAttachment == "arduinoRight":
        RightOmoPlate.attach(arduinoRight, RightOmoPlatePin)
    if RightOmoPlateAttachment == "arduinoNano":
        RightOmoPlate.attach(arduinoNano, RightOmoPlatePin)
    RightOmoPlate.setMinMax(RightOmoPlateMinPos, RightOmoPlateMaxPos)
    #RightOmoPlate.map(0, 100, RightOmoPlateMinPos, RightOmoPlateMaxPos)
    RightOmoPlate.setRest(RightOmoPlateRestPos)
    RightOmoPlate.setInverted(False)
    RightOmoPlate.setSpeed(120)
    RightOmoPlate.setAutoDisable(True)
    RightOmoPlate.rest()

if EnableRightShoulder == True:
    print "--Right Shoulder"
    RightShoulder = Runtime.createAndStart("RightShoulder", "Servo")
    if RightShoulderAttachment == "Head":
        RightShoulder.attach(Head, RightShoulderPin)
    if RightShoulderAttachment == "Back":
        RightShoulder.attach(Back, RightShoulderPin)
    if RightShoulderAttachment == "RightArm":
        RightShoulder.attach(RightArm, RightShoulderPin)
    if RightShoulderAttachment == "LeftArm":
        RightShoulder.attach(LeftArm, RightShoulderPin)
    if RightShoulderAttachment == "arduinoLeft":
        RightShoulder.attach(arduinoLeft, RightShoulderPin)
    if RightShoulderAttachment == "arduinoRight":
        RightShoulder.attach(arduinoRight, RightShoulderPin)
    if RightShoulderAttachment == "arduinoNano":
        RightShoulder.attach(arduinoNano, RightShoulderPin)
    RightShoulder.setMinMax(RightShoulderMinPos, RightShoulderMaxPos)
    #RightShoulder.map(0, 100, RightShoulderMinPos, RightShoulderMaxPos)
    RightShoulder.setRest(RightShoulderRestPos)
    RightShoulder.setInverted(False)
    RightShoulder.setSpeed(120)
    RightShoulder.setAutoDisable(True)
    RightShoulder.rest()

if EnableRightRotate == True:
    print "--Right Rotate"
    RightRotate = Runtime.createAndStart("RightRotate", "Servo")
    if RightRotateAttachment == "Head":
        RightRotate.attach(Head, RightRotatePin)
    if RightRotateAttachment == "Back":
        RightRotate.attach(Back, RightRotatePin)
    if RightRotateAttachment == "RightArm":
        RightRotate.attach(RightArm, RightRotatePin)
    if RightRotateAttachment == "LeftArm":
        RightRotate.attach(LeftArm, RightRotatePin)
    if RightRotateAttachment == "arduinoLeft":
        RightRotate.attach(arduinoLeft, RightRotatePin)
    if RightRotateAttachment == "arduinoRight":
        RightRotate.attach(arduinoRight, RightRotatePin)
    if RightRotateAttachment == "arduinoNano":
        RightRotate.attach(arduinoNano, RightRotatePin)
    RightRotate.setMinMax(RightRotateMinPos, RightRotateMaxPos)
    #RightRotate.map(0, 100, RightRotateMinPos, RightRotateMaxPos)
    RightRotate.setRest(RightRotateRestPos)
    RightRotate.setInverted(False)
    RightRotate.setSpeed(120)
    RightRotate.setAutoDisable(True)
    RightRotate.rest()

if EnableRightBicep == True:
    print "--Right Bicep"
    RightBicep = Runtime.createAndStart("RightBicep", "Servo")
    if RightBicepAttachment == "Head":
        RightBicep.attach(Head, RightBicepPin)
    if RightBicepAttachment == "Back":
        RightBicep.attach(Back, RightBicepPin)
    if RightBicepAttachment == "RightArm":
        RightBicep.attach(RightArm, RightBicepPin)
    if RightBicepAttachment == "LeftArm":
        RightBicep.attach(LeftArm, RightBicepPin)
    if RightBicepAttachment == "arduinoLeft":
        RightBicep.attach(arduinoLeft, RightBicepPin)
    if RightBicepAttachment == "arduinoRight":
        RightBicep.attach(arduinoRight, RightBicepPin)
    if RightBicepAttachment == "arduinoNano":
        RightBicep.attach(arduinoNano, RightBicepPin)
    RightBicep.setMinMax(RightBicepMinPos, RightBicepMaxPos)
    #RightBicep.map(0, 100, RightBicepMinPos, RightBicepMaxPos)
    RightBicep.setRest(RightBicepRestPos)
    RightBicep.setInverted(False)
    RightBicep.setSpeed(120)
    RightBicep.setAutoDisable(True)
    RightBicep.rest()
