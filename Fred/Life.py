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

# When ever you look at a robot just standing there, it looks
# lifeless and dead, that is until it starts to move.
# To make our robot appear to be alive, we need it to move.
# The movements don't need to be large, a small eye movement
# or the eyes blinking can help to bring the robot to life.
# In this file, we will call on a series of small programs
# designed to provide small random movements to simulate a
# living being and in some cases provide simplified interface
# for controlling the robot.

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

# The Eye Balls are controlled from this sub program
execfile(RuningFolder+'/6_Life_Functions/1_Eye_Movements.py')

# The Eye Lids are controlled from this sub program
execfile(RuningFolder+'/6_Life_Functions/2_Eye_Lids.py')

# We don't want our robot being active all the time, so we
# need to put the robot to sleep when it's been idel for a
# while and wake it up when a sense event occurs.
execfile(RuningFolder+'/6_Life_Functions/Wake_Up_And_Sleep')

# Use the PIR sensor to wake up or keep awake
if EnablePIR == True:
    def PirLifeEvent(Sense):
        global Awake
        if Sense:
            print "Warm body movement detected !!!"
            if EnableSleepTimer==True:
                WakeUpEvent()
    pir.addListener("publishSense",python.name,"PirLifeEvent")

# Jaw control based on MarySpeech.
# This section will cause the jaw to open and close as the robot is speaking.
if (UseMarySpeech or UseMimicSpeech or UseEspeak) and EnableMouthControl and EnableJawServo:
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
