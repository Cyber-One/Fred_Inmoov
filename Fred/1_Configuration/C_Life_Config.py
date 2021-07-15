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
# C_Life_Config.py                                           #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Loading the Life Simulation System Config"
##############################################################
#                                                            #
# Life Simulation Group Group                                #
#                                                            #
##############################################################

##############################################################
#                                                            #
# Torso Type Setting                                         #
#                                                            #
##############################################################
# This setting is only valid if the third torso servo is
# fitted.  In this case, the default will be Bob Houstons
# design in which case the setting is False.
# When Bartoz diferential control is used, set this to True.
TorsoType = False

##############################################################
#                                                            #
# Eye Lids Blinking Controls                                 #
#                                                            #
##############################################################
# Having a robot stationary just looking at you with no
# movement is not very life like, so where eye lids are fitted
# we have the blink action.  This action wil close the eye
# lids for a short ime at random intervals between
# RandBlinkMinTime and RandBlinkMaxTime time intervals.
# The Blinking feature can be very anoying, 
# so the option to turn it of is here.
EnableBlinking = True           # Set to True or False
# Minimum time between blinks
RandBlinkMinTime = 5000         # int milliSeconds
# Maximum time between blinks
RandBlinkMaxTime = 10000        # int milliSeconds

##############################################################
#                                                            #
# Eye Movement Controls                                      #
#                                                            #
##############################################################
# while it's good to have the robot blinking above, a living
# creature will tend to get bored and start to move it eyes
# around looking to see what there is.  The section configures
# those movements, if enabled. 
# If servos to move the eyes are not installed, the function
# will still run, but will affect the whole of the head.
EnableRandomEyeMovements = True # Set to True or False
# Min time between movements
RandEyeMovementsMinTime = 1000  # int miliSeconds
# Max time between movements
RandEyeMovementsMaxTime = 5000  # int miliSeconds
# Max amount to move the eyes from last position
# each time the random function is called.
RandEyeMovementsMaxRot = 20     # Perecnt of total range
# When the robot is looking forward, there can be some
# mis-calibration is the eye left right position, and this can
# look very strange.  The solution can be to apply some
# correction with this control.
# A positive number will cross the eyes while a negative
# number will turn them out.
DefaultEyeCrossAmount = 0       # The amount of crossing.

##############################################################
#                                                            #
# Sleep and Wake up  Controls                                #
#                                                            #
##############################################################
# From time to time, we will want the robot to stop running
# the life simulations, this is done by putting the robot
# to sleep after a period of no activity.
# This is only possible when there is a way to wake the Robot
# back up again, This auto sleep can be disabled by disabling
# the Sleep Timer
EnableSleepTimer = True         # Set to True or False
# This is how much quiet time must elapse for the robot 
# goes to sleep.  There are various events that will restart
# the timer, including talking or proximity sensors avtivating
# The time is in mili-seconds.
TimeToSleep = 5 * 60000    
# Wakeup Message
# This message is spoken whenever the robot wakes up
# Set the message to OFF if you don't want this message.
WakeupMessage = u"Hello, How are you"
#WakeupMessage = "OFF"

##############################################################
#                                                            #
# Mouth Control                                              #
#                                                            #
##############################################################
# Mouth control syncronises the Jaw movement with the Speech
# that is spoken using the TTS services.
# There are times when setting up your robot, you don't want
# the jaw to move, this is where you can disable this feature.
# If there are no TTS services enabled or the Jaw is disabled
# then this control has no effect.
EnableMouthControl = True       # Set to True or False

##############################################################
#                                                            #
# NeoPixel Diagnostic Mode Config.                           #
#                                                            #
##############################################################
# We use a multi dimensional array to configure the NeoPixels
# configuration. 
NeoPixelUpdateRate = 500    # mili-Seconds
# Each pixel needs to have is configuration defined.
# We start with the function:
# 0 = Set Pixel color static, Value is ignored and only the
#     first set of colors are used.
# 1 = Left UltraSonic Range, when the distance is less than the
#     value in centimeters, the the first set of LED are used,
#     when greater, the second set are used. Remember, the
#     closer an object is the lower the distance.
# 2 = Right UltraSonic Range, As per the Left Ultrasonic sensor.
# 3 = PIR, this is on or off, so the preset value is ignored.
#     Off uses the first set of colors, on uses the second set.
# 4 = Battery Level, below the value the first est of colors
#     are used, above that the second set of colours are used.
# 5 = Not yet defined, Please make reasonable suggestions :-)
# Next the preset value, The Neopixel will change color based
# on this value.  Then the colour when above and the colour
# when below the preset value.
# Each colour consists of 3 values, Red, Green and Blue with a
# range of 0 - 255, all 0 = off
# [[Function, Value, R_low, G_Low, B_Low, R_High, G_High, B_High]]
NeoPixelDiagConfig = [[1, 250,   0,   0, 200,  10,   0,   0], # pixel 1
    [1, 200,   0,   0, 200,  10,   0,   0],                   # Pixel 2
    [1, 150,   0,   0, 200,  10,   0,   0],                   # Pixel 3
    [1, 100,   0,   0, 200,  10,   0,   0],                   # Pixel 4
    [1,  75,   0,   0, 200,  10,   0,   0],                   # Pixel 5
    [1,  50,   0,   0, 200,  10,   0,   0],                   # Pixel 6
    [1,  25,   0,   0, 200,  10,   0,   0],                   # Pixel 7
    [3,   0,  10,   0,  10, 200, 200,   0],                   # Pixel 8
    [3,   0,  10,   0,  10, 200, 200,   0],                   # Pixel 9
    [2,  25,   0,   0, 200,  10,   0,   0],                   # Pixel 10
    [2,  50,   0,   0, 200,  10,   0,   0],                   # Pixel 11
    [2,  75,   0,   0, 200,  10,   0,   0],                   # Pixel 12
    [2, 100,   0,   0, 200,  10,   0,   0],                   # Pixel 13
    [2, 150,   0,   0, 200,  10,   0,   0],                   # Pixel 14
    [2, 200,   0,   0, 200,  10,   0,   0],                   # Pixel 15
    [2, 250,   0,   0, 200,  10,   0,   0],                   # Pixel 16
    [4, 650,  10,   0,   0, 200, 200, 200],                   # Pixel 17
    [4, 540,  10,   0,   0,   0,  20,  20],                   # Pixel 18
    [4, 560,  10,   0,   0,   0,  20,  20],                   # Pixel 19
    [4, 580,  10,   0,   0,   0,  20,  20],                   # Pixel 20
    [4, 600,  10,   0,   0,   0,  20,  20],                   # Pixel 21
    [4, 620,  10,   0,   0,   0,  20,  20],                   # Pixel 22
    [4, 640,  10,   0,   0,   0,  20,  20],                   # Pixel 23
    [4, 660,  10,   0,   0,   0,  20,  20]]                   # Pixel 24


# For those with NeoPixels in the eyes, there is only the mode
# control to change how the eyes show through.
