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

# Pan and Tilt are the common methods of controlling a camera.
# normally, you would have a rotating base and the place a tilt mechinism on the pan base.
# we have a Pitch and Roll with the Yaw on top of that.
# When we look up at 20 and then turn the head 90 to the left,
# the head will end up with a tilt of 0 but the head will roll 20
# to overcome this we need a Pan and Tilt translation.
# This function assumes that 0, 0, 0 is facing straight ahead with tilt and roll level.
def HeadPanTilt(Pan, Tilt, Roll):
    print "PanTilt( ", Pan, ", ", Tilt, ", ", Roll, ")"
    PanTo = 50 + Pan
    print "Panning To ", PanTo
    if EnableHeadYaw == True:
        HeadYaw.moveTo(PanTo)
    PanRadians = math.radians(Pan)
    print "Thats ", PanRadians, "Radians"
    if EnableHeadPitch == True:
        HeadPitch.moveTo(50+(Tilt*math.cos(PanRadians) + Roll*math.sin(PanRadians)))
    if EnableHeadRoll == True:
        HeadRoll.moveTo(50+(Tilt*math.sin(PanRadians) + Roll*math.cos(PanRadians)))
    print "PanTilt finished"

def HeadPan(NewPan):
    global HeadPanPos
    global HeadTiltPos
    global HeadRollRos
    HeadPanPos = NewPan
    HeadPanTilt(HeadPanTilt, HeadTiltPos, HeadRollRos)
    
# To make is a bit easier to control, we define functions to
# move the two eyes togeter.
# if you have only the one servo for each of these axis, then
# don't worry, this code will ignore the one you don't have
# without crashing
# Like the Pan, Tilt and Roll, we will use 0 as the center
# position and negative number will look down or left.
def eyesLR(eyesLRpos):
    if EnableRightEyeX == True:
        RightEyeLR.moveTo(50+eyesLRpos)
    if EnableLeftEyeX == True:
        LeftEyeLR.moveTo(50+eyesLRpos)

def eyesUD(eyesUDpos):
    if EnableRightEyeY == True:
        RightEyeUD.moveTo(50+eyesUDpos)
    if EnableLeftEyeY == True:
        LeftEyeUD.moveTo(50+eyesUDpos)

# We want the robot to appear to be more alive, and nothing
# speaks to being alive more than small random movements.
def MoveEyes(timedata):
    MoveEyesTimer.setInterval(random.randint(1000,2000))
    if Awake:
        #need to look at speed settings
        eyesLR(random.uniform(-20,20))
        eyesUD(random.uniform(-20,20))

def MoveEyesStart(timedata):
    if isTalking:
        MoveEyesTimer.stopClock()

def MoveEyesStop(timedata):
    eyesLR(0)
    eyesUD(0)

if EnableRandomEyeMovements == True:
    MoveEyesTimer = Runtime.createAndStart("MoveEyesTimer","Clock")
    MoveEyesTimer.addListener("pulse", python.name, "MoveEyes")
    MoveEyesTimer.addListener("clockStarted", python.name, "MoveEyesStart")  
    MoveEyesTimer.addListener("clockStopped", python.name, "MoveEyesStop")

# General eye lid functions
# because there are so many possible configureations, we need to consider a standard set
# of function to implement the eye lids movements.
# Here we define the general ryr lids open and closed as well as half way and wink commands.
# These functions can be called at any time, and won't crash is the feature is not supported.

def UpperEyeLidsOpen():
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(0) # open the right upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(0) # open the left upper eye lid

def UpperEyeLidsMidway():
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(50) # Move to mid pos the right upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(50) # close the upper eye lid

def UpperEyeLidsClose():
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(100) # close the right Upper eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(100) # close the left Upper eye lid

def LowerEyeLidsOpen():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(0) # open the right Lower eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(0) # open the left Lower eye lid

def LowerEyeLidsMidway():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(50) # Move to mid pos the right upper eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(50) # close the upper eye lid

def LowerEyeLidsClose():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(100) # close the right lower eye lid
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(100) # close the left lower eye lid

def WinkLeftEye():
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(100) # close the left lower eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(100) # close the left Upper eye lid
    time.sleep(0.5)
    if EnableLeftLowerEyeLid == True:
        LowerEyeLidL.moveTo(0) # open the left Lower eye lid
    if EnableLeftUpperEyeLid == True:
        UpperEyeLidL.moveTo(0) # open the left upper eye lid

def WinkRightEye():
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(100) # close the Right lower eye lid
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(100) # close the Right Upper eye lid
    time.sleep(0.5)
    if EnableRightLowerEyeLid == True:
        LowerEyeLidR.moveTo(0) # open the Right Lower eye lid
    if EnableRightUpperEyeLid == True:
        UpperEyeLidR.moveTo(0) # open the Right upper eye lid

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
        UpperEyeLidsMidway()
        LowerEyeLidsMidway()
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
if (UseMarySpeech == True or UseMimicSpeech or UseEspeak) and EnableMouthControl == True:
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
    #mouthcontrol.setmouth(JawMinPos, JawMaxPos)
    mouthcontrol.setmouth(10, 80)
    #mouthcontrol.mouthClosedPos = JawMinPos
    #mouthcontrol.mouthOpenedPos = JawMaxPos
    # next we need to setup the delays for the jaw movement.
    # Thanks to Steve Rayner for explaining this group of settings
    # on his YouTube Channel https://www.youtube.com/watch?v=jswk8lDtGOc
    mouthcontrol.delaytime = 75
    mouthcontrol.delaytimestop = 150
    mouthcontrol.delaytimeletter = 40
    mouthcontrol.startService()
