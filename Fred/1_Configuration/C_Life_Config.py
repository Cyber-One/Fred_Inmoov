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

# This setting is only valid if the third torso servo is fitted.  
# In this case, the default will be Bob Houstons design in which
# case the setting is False.
# When Bartoz diferential control is used, set this to True.
TorsoType = False

# The Blinking feature can be very anoying, 
# so the option to turn it of is here.
EnableBlinking = True           # Set to True or False
# Minimum time between blinks
RandBlinkMinTime = 5000         # int milliSeconds
# Maximum time between blinks
RandBlinkMaxTime = 10000        # int milliSeconds

# Moves the eyes to make the robot appear more alive.
EnableRandomEyeMovements = True # Set to True or False
# Min time between movements
RandEyeMovementsMinTime = 1000  # int miliSeconds
# Max time between movements
RandEyeMovementsMaxTime = 5000  # int miliSeconds
# Max amount to move the eyes from last position
# each time the random function is called.
RandEyeMovementsMaxRot = 20     # Perecnt of total range

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

# There are times when setting up your robot, you don't want
# the jaw to move, this is where you can disable this feature.
EnableMouthControl = True       # Set to True or False

# NeoPixel Diagnostic Mode Config
# We use a multi dimensional array to configure the NeoPixels
# configuration. 
# Each pixel needs to have is configuration defined.
# We start with the function:
# 0 = not used
# 1 = Left UltraSonic Range
# 2 = Right UltraSonic Range
# 3 = PIR, this is on or off, so the preset value is ignored.
# 4 = Battery Level
# 5 = Set Pixel color static, Value is ignored and only the first set of colors are used.
# Next the preset value, The Neopixel will change color based
# on this value.  Then the colour when above and the colour
# when below the preset value.
# Each colour consists of 3 values, Red, Green and Blue with a
# range of 0 - 255, all 0 = off
# [[Function, Value, R_low, G_Low, B_Low, R_High, G_High, B_High]]
NeoPixelDiagConfig = [[1, 200,   0,   0, 200,  10,   0,   0], # pixel 1
    [1, 150,   0,   0, 200,  10,   0,   0],                   # Pixel 2
    [1, 100,   0,   0, 200,  10,   0,   0],                   # Pixel 3
    [1,  75,   0,   0, 200,  10,   0,   0],                   # Pixel 4
    [1,  50,   0,   0, 200,  10,   0,   0],                   # Pixel 5
    [1,  25,   0,   0, 200,  10,   0,   0],                   # Pixel 6
    [1,  10,   0,   0, 200,  10,   0,   0],                   # Pixel 7
    [3,   0,  10,   0,  10, 200, 200,   0],                   # Pixel 8
    [3,   0,  10,   0,  10, 200, 200,   0],                   # Pixel 9
    [2,  10,   0,   0, 200,  10,   0,   0],                   # Pixel 10
    [2,  25,   0,   0, 200,  10,   0,   0],                   # Pixel 11
    [2,  50,   0,   0, 200,  10,   0,   0],                   # Pixel 12
    [2,  75,   0,   0, 200,  10,   0,   0],                   # Pixel 13
    [2, 100,   0,   0, 200,  10,   0,   0],                   # Pixel 14
    [2, 150,   0,   0, 200,  10,   0,   0],                   # Pixel 15
    [2, 200,   0,   0, 200,  10,   0,   0],                   # Pixel 16
    [4, 050,  50,   0,   0,  20,  50,   0],                   # Pixel 17
    [5,   0,  10,   0,   0,   0,   0,   0],                   # Pixel 18
    [5,   0,   0,  10,   0,   0,   0,   0],                   # Pixel 19
    [5,   0,   0,   0,  10,   0,   0,   0],                   # Pixel 20
    [5,   0,  10,   0,  10,   0,   0,   0],                   # Pixel 21
    [5,   0,   0,  10,  10,   0,   0,   0],                   # Pixel 22
    [5,   0,  10,  10,  10,   0,   0,   0]]                   # Pixel 23

