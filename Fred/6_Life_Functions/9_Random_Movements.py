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
# 6_Life_Functions/9_Random_Movements.py                     #
# This file is to Simulate life movements associated with    #
# the body of the robot                                      #
#                                                            #
##############################################################
import math
import time
import random

# We want the robot to appear to be more alive, and nothing
# speaks to being alive more than small random movements.
def MoveEyes(timedata):
    MoveEyesTimer.setInterval(random.randint(RandEyeMovementsMinTime,RandEyeMovementsMaxTime))
    if Awake:
        #need to look at speed settings
        LookHeadPan(random.uniform(-RandEyeMovementsMaxRot,RandEyeMovementsMaxRot))
        #eyesUD(random.uniform(-10,10))

def MoveEyesStart():
    if isTalking:
        MoveEyesTimer.stopClock()

def MoveEyesStop():
    LookHeadPanTo(0)    # Look front and center
    LookHeadTiltTo(0)

# The Clock service in MyRobotLab is designed to provide a
# repetative pulse type output each time the preset time
# has elapsed.  This is done using a timer to trigger the
# random amount of movement at a random time interval.
if EnableRandomEyeMovements == True:
    MoveEyesTimer = Runtime.createAndStart("MoveEyesTimer","Clock")
    MoveEyesTimer.setInterval(random.randint(RandEyeMovementsMinTime,RandEyeMovementsMaxTime))
    MoveEyesTimer.addListener("pulse", python.name, "MoveEyes")
    if MRL == "Nixie":
        MoveEyesTimer.addListener("publishClockStarted", python.name, "MoveEyesStart")  
        MoveEyesTimer.addListener("publishClockStopped", python.name, "MoveEyesStop")
    else:
        MoveEyesTimer.addListener("clockStarted", python.name, "MoveEyesStart")  
        MoveEyesTimer.addListener("clockStopped", python.name, "MoveEyesStop")

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

def startBlink()
        UpperEyeLidsMidway(50)
        LowerEyeLidsMidway(50)

def stopBlink()
    UpperEyeLidsClose() # close the upper eye lid
    LowerEyeLidsClose() # close the lower eye lid

# To make the robot appear alive, we create the blink timer
# which in turn calls the blink method.
if EnableBlinking == True:
    # For the Blink to work, we need a timer to control the interval between blinks
    BlinkClock = Runtime.createAndStart("BlinkClock", "Clock")
    # the addListener() call will run the python routine "blink" whenever the pulse event occurs.
    BlinkClock.addListener("pulse", python.name, "blink")
    if MRL == "Nixie":
        BlinkClock.addListener("publishClockStarted", python.name, "startBlink")
        BlinkClock.addListener("publishClockStopped", python.name, "stopBlink")
    else:
        BlinkClock.addListener("clockStarted", python.name, "startBlink")
        BlinkClock.addListener("clockStopped", python.name, "stopBlink")
    # Initially, we will set the blink interval at 10 seconds.
    BlinkClock.setInterval(10000)
    # Then we start the clock running.
    print "--Start Blink Clock"
    BlinkClock.startClock()

