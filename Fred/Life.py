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
# Life.py                                                    #
# This file is to Simulate movements associated with a       #
# living entity                                              #
#                                                            #
##############################################################
import math
import time
import random

print "Creating the various life simulation functions"
# Load the configuration for the IO devices.
execfile(RuningFolder+'/1_Configuration/C_Life_Config.py')

# To make is a bit easier to control, we define functions to move the two eyes togeter.
# if you have only the one servo for each of these axis, then comment out the RightEyeLR and the RightEyeUD lines.
def eyesLR(eyesLRpos):
    RightEyeLR.moveTo(eyesLRpos)
    LeftEyeLR.moveTo(eyesLRpos)

def eyesUD(eyesUDpos):
    RightEyeUD.moveTo(eyesUDpos)
    LeftEyeUD.moveTo(eyesUDpos)

# Pan and Tilt are the common methods of controlling a camera.
# normally, you would have a rotating base and the place a tilt mechinism on the pan base.
# we have a Pitch and Roll with the Yaw on top of that.
# When we look up at 20 and then turn the head 90 to the left,
# the head will end up with a tilt of 0 but the head will roll 20
# to overcome this we need a Pan and Tilt translation.
# This function assumes that 0, 0, 0 is facing straight ahead with tilt and roll level.
def HeadPanTilt(Pan, Tilt, Roll):
    print "PanTilt( ", Pan, ", ", Tilt, ", ", Roll, ")"
    PanTo = 90 + Pan
    print "Panning To ", PanTo
    if EnableHeadYaw == True:
        HeadYaw.moveTo(PanTo)
    PanRadians = math.radians(Pan)
    print "Thats ", PanRadians, "Radians"
    if EnableHeadPitch == True:
        HeadPitch.moveTo(90+(Tilt*math.cos(PanRadians) + Roll*math.sin(PanRadians)))
    if EnableHeadRoll == True:
        HeadRoll.moveTo(90+(Tilt*math.sin(PanRadians) + Roll*math.cos(PanRadians)))
    print "PanTilt finished"

def HeadPan():
    global HeadPanPos
    global HeadTiltPos
    global HeadRollRos
    HeadPanPos = NewPan
    HeadPanTilt(HeadPanTilt, HeadTiltPos, HeadRollRos)
    
# General eye lid functions
# because there are so many possible configureations, we need to consider a standard set
# of function to implement the eye lids movements.
# Here we define the general ryr lids open and closed as well as half way and wink commands.
# These functions can be called at any time, and won't crash is the feature is not supported.

def UpperEyeLidsOpen():
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(UpperREyeLidMinPos) # open the right upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(UpperLEyeLidMinPos) # open the left upper eye lid

def UpperEyeLidsMidway():
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo((UpperREyeLidMaxPos-UpperREyeLidMinPos)/2+UpperREyeLidMinPos) # Move to mid pos the right upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo((UpperLEyeLidMaxPos-UpperLEyeLidMinPos)/2+UpperLEyeLidMinPos) # close the upper eye lid

def UpperEyeLidsClose():
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(UpperREyeLidMaxPos) # close the right Upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(UpperLEyeLidMaxPos) # close the left Upper eye lid

def LowerEyeLidsOpen():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(LowerREyeLidMinPos) # open the right Lower eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(LowerLEyeLidMinPos) # open the left Lower eye lid

def LowerEyeLidsMidway():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo((LowerREyeLidMaxPos-LowerREyeLidMinPos)/2+LowerREyeLidMinPos) # Move to mid pos the right upper eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo((LowerLEyeLidMaxPos-LowerLEyeLidMinPos)/2+LowerLEyeLidMinPos) # close the upper eye lid

def LowerEyeLidsClose():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(LowerREyeLidMaxPos) # close the right lower eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(LowerLEyeLidMaxPos) # close the left lower eye lid

def WinkLeftEye():
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(LowerLEyeLidMaxPos) # close the left lower eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(UpperLEyeLidMaxPos) # close the left Upper eye lid
    time.sleep(0.5)
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(LowerLEyeLidMinPos) # open the left Lower eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(UpperLEyeLidMinPos) # open the left upper eye lid

def WinkRightEye():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(LowerREyeLidMaxPos) # close the Right lower eye lid
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(UpperREyeLidMaxPos) # close the Right Upper eye lid
    time.sleep(0.5)
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(LowerREyeLidMinPos) # open the Right Lower eye lid
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(UpperREyeLidMinPos) # open the Right upper eye lid

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

# If our robot has been sleeping, Then we need to wake it up
# and at least half open it's eyes. 
# Call the blink to fully open the eyes :-)
def WakeUpEvent():
    global Awake
    print "Wake Up Event Occured"
    if Awake == True:
        print "Keep Awake"
        if EnableSleepTimer==True:
            SleepTimer.restartClock(True)
    if Awake == False:
        print "Waking Up"
        UpperEyeLidsMidway()
        LowerEyeLidsMidway()
        if EnableSleepTimer==True:
            SleepTimer.restartClock(True)
        if EnableBlinking == True:
            BlinkClock.restartClock(True)
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
    UpperEyeLidsClose() # close the upper eye lid
    LowerEyeLidsClose() # close the lower eye lid
    print "Sleeping"

# Use the PIR sensor to wake up or keep awake
if EnablePIR == True:
    if EnableSleepTimer==True:
        SleepTimer =Runtime.createAndStart("SleepTimer", "Clock")
        print "Sleep Timer Adding Listner"
        SleepTimer.addListener("pulse", python.name, "GoToSleepEvent")
        print "Sleep Timer Setting Sleep Time"
        SleepTimer.setInterval(TimeToSleep)
        print "Sleep Timer Starting Clock"
        SleepTimer.startClock(False)
        print "Sleep Timer Running"
    def PirLifeEvent(event):
        global Awake
        if event:
            print "Warm body movement detected !!!"
            if EnableSleepTimer==True:
                WakeUpEvent()
    pir.addListener("publishSense",python.name,"PirLifeEvent")

# Jaw control based on MarySpeech.
if UseMarySpeech == True and EnableMouthControl == True:
    # Before we can use this feature, we first need to create it :-)
    mouthcontrol = Runtime.create("mouthcontrol","MouthControl")
    #mouthcontrol = Runtime.start("mouthcontrol","MouthControl")
    # Once created we need to link it to the servo that controls the mouth opening and closing
    # in out case we called that Jaw back in the Servo.py file.
    #mouthcontrol.attach(Jaw)
    mouthcontrol.setJaw(Jaw)
    # Next we need to link it to the TTS service, we called that Mouth
    #mouthcontrol.attach(Mouth)
    mouthcontrol.setMouth(Mouth)
    # We need to set the range of motion for the Jaw
    mouthcontrol.setmouth(JawMinPos, JawMaxPos)
    #mouthcontrol.mouthClosedPos = JawMinPos
    #mouthcontrol.mouthOpenedPos = JawMaxPos
    # next we need to setup the delays for the jaw movement.
    # Thanks to Steve Rayner for explaining this group of settings
    # on his YouTube Channel https://www.youtube.com/watch?v=jswk8lDtGOc
    mouthcontrol.delaytime = 75
    mouthcontrol.delaytimestop = 150
    mouthcontrol.delaytimeletter = 40
    mouthcontrol.startService()
