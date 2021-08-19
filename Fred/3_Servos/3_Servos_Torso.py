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
EnableTopStomach = TestServoControllerExists(TopStomachAttachment, EnableTopStomach)
if EnableTopStomach == True:
    print "--Top Stomach"
    TopStomach = Runtime.createAndStart("TopStomach", "Servo")
    TopStomach.attach(runtime.getService(TopStomachAttachment), TopStomachPin)
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
EnableMidStomach = TestServoControllerExists(MidStomachAttachment, EnableMidStomach)
if EnableMidStomach == True:
    print "--Top Stomach"
    MidStomach = Runtime.createAndStart("MidStomach", "Servo")
    MidStomach.attach(runtime.getService(MidStomachAttachment), MidStomachPin)
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
EnablePitchStomach = TestServoControllerExists(PitchStomachAttchment, EnablePitchStomach)

if EnablePitchStomach == True:
    print "--Top Stomach"
    PitchStomach = Runtime.createAndStart("PitchStomach", "Servo")
    PitchStomach.attach(runtime.getService(PitchStomachAttchment), PitchStomachPin)
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
