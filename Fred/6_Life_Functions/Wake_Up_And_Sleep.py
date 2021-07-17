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
# 6_Life_Functions/Wake_Up_And_Sleep.py                      #
# We don't want our robot being active all the time, so we   #
# need to put the robot to sleep when it's been idel for a   #
# while and wake it up when an event occurs.                 #
#                                                            #
##############################################################
import math
import time
import random

# If our robot has been sleeping, the eyes should be closed
# So we need to wake it up and at least half open it's eyes. 
# Call the blink to fully open the eyes :-)  The Blink time
# will do this anyway.
# It would also pay to center the eyes as well.
# If the robot was already awak, this method will just reset
# the sleep time to prevent the robot going to sleep for a
# while anyway :-)
def WakeUpEvent():
    global Awake
    if Awake == True:
        if EnableSleepTimer==True:
            SleepTimer.restartClock(True)
    if Awake == False:
        UpperEyeLidsMidway(50)
        LowerEyeLidsMidway(50)
        eyesLR(0)
        eyesUD(0)
        if EnableSleepTimer==True:
            SleepTimer.restartClock(True)
        if EnableBlinking == True:
            BlinkClock.restartClock(True)
#        if EnableRandomEyeMovements == True:
#            MoveEyesTimer.startClock()
        Awake = True
        if not WakeupMessage == "OFF" and not isTalking:
            Mouth.speak(WakeupMessage)

# We might not want our robot to be awake all the time.
# this method will put it to sleep, or at least simulate it.
def GoToSleepEvent(timedata):
    global Awake
    if EnableSleepTimer==True:
        SleepTimer.stopClock()
    Awake = False
    if EnableBlinking == True:
        BlinkClock.stopClock()
    if EnableRandomEyeMovements == True:
        MoveEyesTimer.stopClock()
    UpperEyeLidsClose() # close the upper eye lid
    LowerEyeLidsClose() # close the lower eye lid

# Or robot has two major methods used to wake up the robot and
# to put the robot to sleep.  We will add a number of calls to
# the wakup method, but there is not much that puts the robot
# to sleep.  The SleepTime is one of the service we can use to
# put the robot to sleep.
if EnableSleepTimer==True:
    SleepTimer =Runtime.createAndStart("SleepTimer", "Clock")
    SleepTimer.addListener("pulse", python.name, "GoToSleepEvent")
    SleepTimer.setInterval(TimeToSleep)
    SleepTimer.startClock(False)

# this section disables the sleep timer while the robot is talking.
def StartSpeaking(Text):
    if EnableSleepTimer==True:
        SleepTimer.stopClock()
        if not Awake:
            WakeUpEvent();
    isTalking = True
    
def StopSpeaking(Text):
    if EnableSleepTimer==True:
        SleepTimer.restartClock(True)
    isTalking = False

if (UseMarySpeech or UseEspeak or UseMimicSpeech):
    # Most, if not all the Text To Speech (TTS) services have
    # a few call back methods.  The ones I'm interested in 
    # here are the "startSpeaking" and the "stopSpeaking".
    # To use these call back methods, we need to Subscribe 
    # to the events, this is done using the addListener method.
    if MRL == "Nixie":
        Mouth.addListener("publishStartSpeaking",python.name,"StartSpeaking")
        Mouth.addListener("publishEndSpeaking",python.name,"StopSpeaking")
    else:
        Mouth.addListener("startSpeaking",python.name,"StartSpeaking")
        Mouth.addListener("stopSpeaking",python.name,"StopSpeaking")
