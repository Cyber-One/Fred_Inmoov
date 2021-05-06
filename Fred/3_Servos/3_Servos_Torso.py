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

if EnableRollStomach == True:
    print "--Top Stomach"
    RollStomach = Runtime.createAndStart("RollStomach", "Servo")
    if RollStomachAttchment == "Head":
        RollStomach.attach(Head, RollStomachPin)
    if RollStomachAttchment == "Back":
        RollStomach.attach(Back, RollStomachPin)
    if RollStomachAttchment == "RightArm":
        RollStomach.attach(RightArm, RollStomachPin)
    if RollStomachAttchment == "LeftArm":
        RollStomach.attach(LeftArm, RollStomachPin)
    if RollStomachAttchment == "arduinoLeft":
        RollStomach.attach(arduinoLeft, RollStomachPin)
    if RollStomachAttchment == "arduinoRight":
        RollStomach.attach(arduinoRight, RollStomachPin)
    if RollStomachAttchment == "arduinoNano":
        RollStomach.attach(arduinoNano, RollStomachPin)
    #RollStomach.setMinMax(RollStomachMinPos, RollStomachMaxPos)
    RollStomach.setMinMax(0, 100)
    if RollStomachMinPos < RollStomachMaxPos:
        RollStomach.map(0, 100, RollStomachMinPos, RollStomachMaxPos)
        RollStomach.setInverted(False)
    else:
        RollStomach.map(0, 100, RollStomachMaxPos, RollStomachMinPos)
        RollStomach.setInverted(True)
    RollStomach.setRest(RollStomachRestPos)
    if MRL == "Nixie":
        RollStomach.setSpeed(RollStomachMaxSpeed)
    else:
        RollStomach.setVelocity(RollStomachMaxSpeed) ## max velocity
    RollStomach.setAutoDisable(True)
    RollStomach.rest()
