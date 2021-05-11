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

if EnableTopStomach == True:
    print "--Top Stomach"
    TopStomach = Runtime.createAndStart("TopStomach", "Servo")
    if TopStomachAttachment == "Head":
        TopStomach.attach(Head, TopStomachPin)
    if TopStomachAttachment == "Back":
        TopStomach.attach(Back, TopStomachPin)
    if TopStomachAttachment == "RightArm":
        TopStomach.attach(RightArm, TopStomachPin)
    if TopStomachAttachment == "LeftArm":
        TopStomach.attach(LeftArm, TopStomachPin)
    if TopStomachAttachment == "arduinoLeft":
        TopStomach.attach(arduinoLeft, TopStomachPin)
    if TopStomachAttachment == "arduinoRight":
        TopStomach.attach(arduinoRight, TopStomachPin)
    if TopStomachAttachment == "arduinoNano":
        TopStomach.attach(arduinoNano, TopStomachPin)
    #TopStomach.setMinMax(TopStomachMinPos, TopStomachMaxPos)
    TopStomach.setMinMax(0, 100)
    if TopStomachMinPos < TopStomachMaxPos:
        TopStomach.map(0, 100, TopStomachMinPos, TopStomachMaxPos)
        TopStomach.setInverted(False)
    else:
        TopStomach.map(0, 100, TopStomachMaxPos, TopStomachMinPos)
        TopStomach.setInverted(True)
    TopStomach.setRest(TopStomachRestPos)
    if MRL == "Nixie":
        TopStomach.setSpeed(TopStomachMaxSpeed)
    else:
        TopStomach.setVelocity(TopStomachMaxSpeed) ## max velocity
    TopStomach.setAutoDisable(True)
    TopStomach.rest()

if EnableMidStomach == True:
    print "--Top Stomach"
    MidStomach = Runtime.createAndStart("MidStomach", "Servo")
    if MidStomachAttachment == "Head":
        MidStomach.attach(Head, MidStomachPin)
    if MidStomachAttachment == "Back":
        MidStomach.attach(Back, MidStomachPin)
    if MidStomachAttachment == "RightArm":
        MidStomach.attach(RightArm, MidStomachPin)
    if MidStomachAttachment == "LeftArm":
        MidStomach.attach(LeftArm, MidStomachPin)
    if MidStomachAttachment == "arduinoLeft":
        MidStomach.attach(arduinoLeft, MidStomachPin)
    if MidStomachAttachment == "arduinoRight":
        MidStomach.attach(arduinoRight, MidStomachPin)
    if MidStomachAttachment == "arduinoNano":
        MidStomach.attach(arduinoNano, MidStomachPin)
    #MidStomach.setMinMax(MidStomachMinPos, MidStomachMaxPos)
    MidStomach.setMinMax(0, 100)
    if MidStomachMinPos < MidStomachMaxPos:
        MidStomach.map(0, 100, MidStomachMinPos, MidStomachMaxPos)
        MidStomach.setInverted(False)
    else:
        MidStomach.map(0, 100, MidStomachMaxPos, MidStomachMinPos)
        MidStomach.setInverted(True)
    MidStomach.setRest(MidStomachRestPos)
    if MRL == "Nixie":
        MidStomach.setSpeed(MidStomachMaxSpeed)
    else:
        MidStomach.setVelocity(MidStomachMaxSpeed) ## max velocity
    MidStomach.setAutoDisable(True)
    MidStomach.rest()

if EnablePitchStomach == True:
    print "--Top Stomach"
    PitchStomach = Runtime.createAndStart("PitchStomach", "Servo")
    if PitchStomachAttchment == "Head":
        PitchStomach.attach(Head, PitchStomachPin)
    if PitchStomachAttchment == "Back":
        PitchStomach.attach(Back, PitchStomachPin)
    if PitchStomachAttchment == "RightArm":
        PitchStomach.attach(RightArm, PitchStomachPin)
    if PitchStomachAttchment == "LeftArm":
        PitchStomach.attach(LeftArm, PitchStomachPin)
    if PitchStomachAttchment == "arduinoLeft":
        PitchStomach.attach(arduinoLeft, PitchStomachPin)
    if PitchStomachAttchment == "arduinoRight":
        PitchStomach.attach(arduinoRight, PitchStomachPin)
    if PitchStomachAttchment == "arduinoNano":
        PitchStomach.attach(arduinoNano, PitchStomachPin)
    #PitchStomach.setMinMax(PitchStomachMinPos, PitchStomachMaxPos)
    PitchStomach.setMinMax(0, 100)
    if PitchStomachMinPos < PitchStomachMaxPos:
        PitchStomach.map(0, 100, PitchStomachMinPos, PitchStomachMaxPos)
        PitchStomach.setInverted(False)
    else:
        PitchStomach.map(0, 100, PitchStomachMaxPos, PitchStomachMinPos)
        PitchStomach.setInverted(True)
    PitchStomach.setRest(PitchStomachRestPos)
    if MRL == "Nixie":
        PitchStomach.setSpeed(PitchStomachMaxSpeed)
    else:
        PitchStomach.setVelocity(PitchStomachMaxSpeed) ## max velocity
    PitchStomach.setAutoDisable(True)
    PitchStomach.rest()
