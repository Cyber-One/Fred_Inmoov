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
# 3_Servos_Torso.py                                          #
# This file is to start all the servos used in the Robot     #
#                                                            #
##############################################################
print "Starting the various Servos Services"
##############################################################
#                                                            #
# Servo Torso Group                                          #
#                                                            #
##############################################################
# Refer to the /1_Configuration/5_Servo_Torso_Config.py file
# for an explenation of what these servo are for.

# Load the configuration for the Servos_Head.
execfile(RuningFolder+'/1_Configuration/5_Servo_Torso_Config.py')

# Test to make sure the configured controller is enabled.
if not ((TopStomachAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (TopStomachAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (TopStomachAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (TopStomachAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (TopStomachAttachment == "arduinoNano" and EnableArduinoNano) 
    or (TopStomachAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (TopStomachAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (TopStomachAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableTopStomach = False

if EnableTopStomach == True:
    print "--Top Stomach"
    TopStomach = Runtime.createAndStart("TopStomach", "Servo")
    if TopStomachAttachment == "Head":
        TopStomach.attach(Head, TopStomachPin)
    elif TopStomachAttachment == "Back":
        TopStomach.attach(Back, TopStomachPin)
    elif TopStomachAttachment == "RightArm":
        TopStomach.attach(RightArm, TopStomachPin)
    elif TopStomachAttachment == "LeftArm":
        TopStomach.attach(LeftArm, TopStomachPin)
    elif TopStomachAttachment == "arduinoLeft":
        TopStomach.attach(arduinoLeft, TopStomachPin)
    elif TopStomachAttachment == "arduinoRight":
        TopStomach.attach(arduinoRight, TopStomachPin)
    elif TopStomachAttachment == "arduinoNano":
        TopStomach.attach(arduinoNano, TopStomachPin)
    elif TopStomachAttachment == "arduinoNano2":
        TopStomach.attach(arduinoNano2, TopStomachPin)
    #TopStomach.setMinMax(TopStomachMinPos, TopStomachMaxPos)
    TopStomach.setMinMax(0, 100)
    if TopStomachMinPos < TopStomachMaxPos:
        TopStomach.map(0, 100, TopStomachMinPos, TopStomachMaxPos)
        TopStomach.setInverted(False)
    else:
        TopStomach.map(0, 100, TopStomachMaxPos, TopStomachMinPos)
        TopStomach.setInverted(True)
    TopStomach.setRest(50)
    if MRL == "Nixie":
        TopStomach.setSpeed(TopStomachMaxSpeed)
    else:
        TopStomach.setVelocity(TopStomachMaxSpeed) ## max velocity
    TopStomach.setAutoDisable(True)
    TopStomach.rest()

# Test to make sure the configured controller is enabled.
if not ((MidStomachAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (MidStomachAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (MidStomachAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (MidStomachAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (MidStomachAttachment == "arduinoNano" and EnableArduinoNano) 
    or (MidStomachAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (MidStomachAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (MidStomachAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableMidStomach = False

if EnableMidStomach == True:
    print "--Top Stomach"
    MidStomach = Runtime.createAndStart("MidStomach", "Servo")
    if MidStomachAttachment == "Head":
        MidStomach.attach(Head, MidStomachPin)
    elif MidStomachAttachment == "Back":
        MidStomach.attach(Back, MidStomachPin)
    elif MidStomachAttachment == "RightArm":
        MidStomach.attach(RightArm, MidStomachPin)
    elif MidStomachAttachment == "LeftArm":
        MidStomach.attach(LeftArm, MidStomachPin)
    elif MidStomachAttachment == "arduinoLeft":
        MidStomach.attach(arduinoLeft, MidStomachPin)
    elif MidStomachAttachment == "arduinoRight":
        MidStomach.attach(arduinoRight, MidStomachPin)
    elif MidStomachAttachment == "arduinoNano":
        MidStomach.attach(arduinoNano, MidStomachPin)
    elif MidStomachAttachment == "arduinoNano2":
        MidStomach.attach(arduinoNano2, MidStomachPin)
    #MidStomach.setMinMax(MidStomachMinPos, MidStomachMaxPos)
    MidStomach.setMinMax(0, 100)
    if MidStomachMinPos < MidStomachMaxPos:
        MidStomach.map(0, 100, MidStomachMinPos, MidStomachMaxPos)
        MidStomach.setInverted(False)
    else:
        MidStomach.map(0, 100, MidStomachMaxPos, MidStomachMinPos)
        MidStomach.setInverted(True)
    MidStomach.setRest(50)
    if MRL == "Nixie":
        MidStomach.setSpeed(MidStomachMaxSpeed)
    else:
        MidStomach.setVelocity(MidStomachMaxSpeed) ## max velocity
    MidStomach.setAutoDisable(True)
    MidStomach.rest()

# Test to make sure the configured controller is enabled.
if not ((PitchStomachAttchment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (PitchStomachAttchment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (PitchStomachAttchment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (PitchStomachAttchment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (PitchStomachAttchment == "arduinoNano" and EnableArduinoNano) 
    or (PitchStomachAttchment == "arduinoNano2" and EnableArduinoNano2) 
    or (PitchStomachAttchment == "arduinoLeft" and EnableArduinoLeft) 
    or (PitchStomachAttchment == "arduinoRight" and EnableArduinoRight)):
    EnablePitchStomach = False

if EnablePitchStomach == True:
    print "--Top Stomach"
    PitchStomach = Runtime.createAndStart("PitchStomach", "Servo")
    if PitchStomachAttchment == "Head":
        PitchStomach.attach(Head, PitchStomachPin)
    elif PitchStomachAttchment == "Back":
        PitchStomach.attach(Back, PitchStomachPin)
    elif PitchStomachAttchment == "RightArm":
        PitchStomach.attach(RightArm, PitchStomachPin)
    elif PitchStomachAttchment == "LeftArm":
        PitchStomach.attach(LeftArm, PitchStomachPin)
    elif PitchStomachAttchment == "arduinoLeft":
        PitchStomach.attach(arduinoLeft, PitchStomachPin)
    elif PitchStomachAttchment == "arduinoRight":
        PitchStomach.attach(arduinoRight, PitchStomachPin)
    elif PitchStomachAttchment == "arduinoNano":
        PitchStomach.attach(arduinoNano, PitchStomachPin)
    elif PitchStomachAttchment == "arduinoNano2":
        PitchStomach.attach(arduinoNano2, PitchStomachPin)
    #PitchStomach.setMinMax(PitchStomachMinPos, PitchStomachMaxPos)
    PitchStomach.setMinMax(0, 100)
    if PitchStomachMinPos < PitchStomachMaxPos:
        PitchStomach.map(0, 100, PitchStomachMinPos, PitchStomachMaxPos)
        PitchStomach.setInverted(False)
    else:
        PitchStomach.map(0, 100, PitchStomachMaxPos, PitchStomachMinPos)
        PitchStomach.setInverted(True)
    PitchStomach.setRest(50)
    if MRL == "Nixie":
        PitchStomach.setSpeed(PitchStomachMaxSpeed)
    else:
        PitchStomach.setVelocity(PitchStomachMaxSpeed) ## max velocity
    PitchStomach.setAutoDisable(True)
    PitchStomach.rest()
