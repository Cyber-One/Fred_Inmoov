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
# 4_Servos_RightArm.py                                          #
# This file is to start all the servos used in the Robots       #
# Right Arm.                                                    #
#                                                               #
#################################################################
print "Starting the Right Arm Servos Services"

#################################################################
# Refer to /1_Configuration/6_Servo_RightArm_Config.py for      #
# more information on what these servos are for.                #
#                                                               #
# Load the configuration for the Servos_Head.                   #
#################################################################
execfile(RuningFolder+'/1_Configuration/6_Servo_RightArm_Config.py')

#################################################################
# This servo lifts the arm sideway from the body.               #
#################################################################
EnableRightOmoPlate = TestServoControllerExists(RightOmoPlateAttachment, EnableRightOmoPlate)
if EnableRightOmoPlate == True:
    print "--Right OmoPlate"
    RightOmoPlate = Runtime.createAndStart("RightOmoPlate", "Servo")
    RightOmoPlate.attach(runtime.getService(RightOmoPlateAttachment), RightOmoPlatePin)
    RightOmoPlate.setMinMax(0, 100)
    if RightOmoPlateMinPos < RightOmoPlateMaxPos:
        RightOmoPlate.map(0, 100, RightOmoPlateMinPos, RightOmoPlateMaxPos)
        RightOmoPlate.setInverted(False)
    else:
        RightOmoPlate.map(0, 100, RightOmoPlateMaxPos, RightOmoPlateMinPos)
        RightOmoPlate.setInverted(True)
    RightOmoPlate.setRest(0)
    if MRL == "Nixie":
        RightOmoPlate.setSpeed(RightOmoPlateMaxSpeed)
    else:
        RightOmoPlate.setVelocity(RightOmoPlateMaxSpeed) ## max velocity
    RightOmoPlate.setAutoDisable(True)
    RightOmoPlate.rest()

#################################################################
# This servo rotates the arm at the shoulder back and forwards. #
#################################################################
EnableRightShoulder = TestServoControllerExists(RightShoulderAttachment, EnableRightShoulder)
if EnableRightShoulder == True:
    print "--Right Shoulder"
    RightShoulder = Runtime.createAndStart("RightShoulder", "Servo")
    RightShoulder.attach(runtime.getService(RightShoulderAttachment), RightShoulderPin)
    RightShoulder.setMinMax(0, 100)
    if RightShoulderMinPos < RightShoulderMaxPos:
        RightShoulder.map(0, 100, RightShoulderMinPos, RightShoulderMaxPos)
        RightShoulder.setInverted(False)
    else:
        RightShoulder.map(0, 100, RightShoulderMaxPos, RightShoulderMinPos)
        RightShoulder.setInverted(True)
    RightShoulder.setRest(16)
    if MRL == "Nixie":
        RightShoulder.setSpeed(RightShoulderMaxSpeed)
    else:
        RightShoulder.setVelocity(RightShoulderMaxSpeed) ## max velocity
    RightShoulder.setAutoDisable(True)
    RightShoulder.rest()

#################################################################
# This servo rotates the bicep changing the angle the elbow     #
# rotates.                                                      #
#################################################################
EnableRightRotate = TestServoControllerExists(RightRotateAttachment, EnableRightRotate)
if EnableRightRotate == True:
    print "--Right Rotate"
    RightRotate = Runtime.createAndStart("RightRotate", "Servo")
    RightRotate.attach(runtime.getService(RightRotateAttachment), RightRotatePin)
    RightRotate.setMinMax(0, 100)
    if RightRotateMinPos < RightRotateMaxPos:
        RightRotate.map(0, 100, RightRotateMinPos, RightRotateMaxPos)
        RightRotate.setInverted(False)
    else:
        RightRotate.map(0, 100, RightRotateMaxPos, RightRotateMinPos)
        RightRotate.setInverted(True)
    RightRotate.setRest(50)
    if MRL == "Nixie":
        RightRotate.setSpeed(50)
    else:
        RightRotate.setVelocity(RightRotateMaxSpeed) ## max velocity
    RightRotate.setAutoDisable(True)
    RightRotate.rest()

#################################################################
# This servo bends the and straightens the elbow joint.         #
#################################################################
EnableRightBicep = TestServoControllerExists(RightBicepAttachment, EnableRightBicep)
if EnableRightBicep == True:
    print "--Right Bicep"
    RightBicep = Runtime.createAndStart("RightBicep", "Servo")
    RightBicep.attach(runtime.getService(RightBicepAttachment), RightBicepPin)
    RightBicep.setMinMax(0, 100)
    if RightBicepMinPos < RightBicepMaxPos:
        RightBicep.map(0, 100, RightBicepMinPos, RightBicepMaxPos)
        RightBicep.setInverted(False)
    else:
        RightBicep.map(0, 100, RightBicepMaxPos, RightBicepMinPos)
        RightBicep.setInverted(True)
    RightBicep.setRest(10)
    if MRL == "Nixie":
        RightBicep.setSpeed(RightBicepMaxSpeed)
    else:
        RightBicep.setVelocity(RightBicepMaxSpeed) ## max velocity
    RightBicep.setAutoDisable(True)
    RightBicep.rest()
