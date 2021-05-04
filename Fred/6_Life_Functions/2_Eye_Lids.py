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
# 6_Life_Functions/2_Eye_Lids.py                             #
# This file is to Simulate life movements associated with    #
# the eye lids                                               #
#                                                            #
##############################################################
import math
import time
import random

# General eye lid functions
# because there are so many possible configureations, we need to consider a standard set
# of function to implement the eye lids movements.
# Here we define the general ryr lids open and closed as well as half way and wink commands.
# These functions can be called at any time, and won't crash is the feature is not supported.

def UpperEyeLidsOpen():
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(100) # open the right upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(100) # open the left upper eye lid

def UpperEyeLidsMidway(midPos):
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(midPos) # Move to mid pos the right upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(midPos) # close the upper eye lid

def UpperEyeLidsClose():
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(0) # close the right Upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(0) # close the left Upper eye lid

def LowerEyeLidsOpen():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(100) # open the right Lower eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(100) # open the left Lower eye lid

def LowerEyeLidsMidway(midPos):
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(midPos) # Move to mid pos the right upper eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(midPos) # close the upper eye lid

def LowerEyeLidsClose():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(0) # close the right lower eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(0) # close the left lower eye lid

def WinkLeftEye():
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(0) # close the left lower eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(0) # close the left Upper eye lid
    time.sleep(0.5)
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(100) # open the left Lower eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(100) # open the left upper eye lid

def WinkRightEye():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(0) # close the Right lower eye lid
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(0) # close the Right Upper eye lid
    time.sleep(0.5)
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(100) # open the Right Lower eye lid
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(100) # open the Right upper eye lid

# Routines to create the blinking motion
# we use the Clock service to provide a regular event that calls the blink procedure.
# one of the things we do within the blink routine is to change the blink interval to a random number between 5 and 10 seconds.
# future enhancements may include shifting the random range based on the current light levels and the average light levels,
# blink more often when the light levels increase until an average value has been reached.
print "-Eye blinking"

# We need a function that does the blink when the timer expires
# or if we want to simulate a blink for some reason.
# timedata is not used but is required by the timer service.
def blink(timedata):
    UpperEyeLidsClose() # close the upper eye lid
    LowerEyeLidsClose() # close the lower eye lid
    time.sleep(0.5)
    UpperEyeLidsOpen() # Open the upper eye lid
    LowerEyeLidsOpen() # Open the lower eye lid
    if EnableBlinking == True:
        BlinkInterval = random.randint(5000, 10000) # But this random one is more life like.
        print "BlinkInterval of ", BlinkInterval, " miliseconds"
        BlinkClock.setInterval(BlinkInterval) # Set a new random time for the next blink

# To make the robot appear alive, we create the blink timer
# which in turn calls the blink method.
if EnableBlinking == True:
    # For the Blink to work, we need a timer to control the interval between blinks
    BlinkClock = Runtime.createAndStart("BlinkClock", "Clock")
    # the addListener() call will run the python routine "blink" whenever the pulse event occurs.
    BlinkClock.addListener("pulse", python.name, "blink")
    # Initially, we will set the blink interval at 10 seconds.
    BlinkClock.setInterval(10000)
    # Then we start the clock running.
    print "--Start Blink Clock"
    BlinkClock.startClock()

# If our robot has been sleeping, the eyes should be closed
# So we need to wake it up and at least half open it's eyes. 
# Call the blink to fully open the eyes :-)
# It would also pay to center the eyes as well.
def WakeUpEvent():
    global Awake
    print "Wake Up Event Occured"
    if Awake == True:
        print "Keep Awake"
        if EnableSleepTimer==True:
            SleepTimer.restartClock(True)
    if Awake == False:
        print "Waking Up"
        UpperEyeLidsMidway(50)
        LowerEyeLidsMidway(50)
        eyesLR(0)
        eyesUD(0)
        if EnableSleepTimer==True:
            SleepTimer.restartClock(True)
        if EnableBlinking == True:
            BlinkClock.restartClock(True)
        if EnableRandomEyeMovements == True:
            MoveEyesTimer.startClock()
        Awake = True
        if not WakeupMessage == "OFF":
            Mouth.speak(WakeupMessage)
        print "Fully Awake"

# We might not want our robot to be awake all the time.
# this method will put it to sleep, or at least simulate it.
def GoToSleepEvent(timedata):
    global Awake
    print "Going to Sleep"
    if EnableSleepTimer==True:
        SleepTimer.stopClock()
    Awake = False
    if EnableBlinking == True:
        BlinkClock.stopClock()
    if EnableRandomEyeMovements == True:
        MoveEyesTimer.stopClock()
    UpperEyeLidsClose() # close the upper eye lid
    LowerEyeLidsClose() # close the lower eye lid
    print "Sleeping"

def StartSpeaking(Text):
    if EnableSleepTimer==True:
        SleepTimer.stopClock()
        isTalking = True

def StopSpeaking(Text):
    if EnableSleepTimer==True:
        if EnableSleepTimer==True:
            SleepTimer.restartClock(True)
        isTalking = False

if (UseMarySpeech or UseEspeak or UseMimicSpeech):
    Mouth.addListener("startSpeaking",python.name,"StartSpeaking")
    Mouth.addListener("stopSpeaking",python.name,"StopSpeaking")
