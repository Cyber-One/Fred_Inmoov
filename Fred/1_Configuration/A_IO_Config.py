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
# A_IO_Config.py                                 #
# This is where the configuration settings live for the      #
# varoius devices that don't fit in the other catagories.    #
#                                                            #
##############################################################
print "Creating the Input/Output Config"

##############################################################
#                                                            #
# The PIR                                                    #
#                                                            #
##############################################################
# Passive Inrea Red (PIR) works on the principle that a 
# warm body emits Infra Red (IR) light. The level of this 
# light can indicate the current temperature.
# PIR sensors, use a single sensing element to measure the 
# ambient IR level.
# By using a segmented lens in front of the sensor, there 
# will be areas where the sensor can not see the IR 
# levels, and areas where it is amplified.  
# As a warm body such as a person moves from one area to 
# another, there is a large change in the IR levels 
# detected, when this change occurs the output of the PIR 
# sensor is turned on.
EnablePIR = True
PirAttachment = "arduinoNano"               # "arduioLeft"
PirPin = 2                                  # 23

##############################################################
#                                                            #
# The Ultra-Sonic Range Sensors                              #
#                                                            #
##############################################################
# Ultrasonic sensors emit a pulse of high frequency sound normally
# 8 cycles at a frequency the we can not hear.
# They then wait for the reflected sound to be detected.
# The time taken for the sound pulse to travel to an object and be
# reflected back can be timed and give a reasonable indication of
# the distance the object is away from the sensor.
# The speed of sound in air is about 343 metres per second 
# or 1,235 km/h; 1,125 ft/s; 767 mph.
# The speed of sound however will vary with temperature.
# Speed = 331.3 + (0.606 * airTemp) m/s
EnableLeftUltrasonic = True                 #
LeftUltrasonicAttachment = "arduinoNano"    # "arduioLeft"
LeftUltrasonicPin1 = 12                     # 64
LeftUltrasonicPin2 = 11                     # 63

EnableRightUltraSonic = True                #
RightUltrasonicAttachment = "arduinoNano"   # "arduioRight"
RightUltrasonicPin1 = 10                    # 64
RightUltrasonicPin2 = 9                     # 63

# Time between Pings in milli-seconds.
PingTime = 1000

##############################################################
#                                                            #
# The Battery Voltage Monitor                                #
#                                                            #
##############################################################
# Battery Voltage can be a very important thing to monitor
# when your robot is running on batteries.  For the most part
# this is done with a simple resistor divider network.
# For this to work, an analog pin needs to be allocated from
# one of the installed Arduino's.  A resistor divider network,
# two resistors connected in series is connected between the
# ground and the battery power.  The junction of the two
# resistors is then connected to teh Arduino's analoginput.
# The resistors are selected so that at no time would the
# voltage at the Arduino exceed 5 volts.
# For Freds build, he's using 20Vdc batteries, so if we use a
# 10K resistor between gnd and the input and a 56K resistor
# between the input and the battery, we should be safe up to
# 33Vdc
EnableBatteryMonitor = False
BatteryMonitorAttachment = "arduinoNano"
BatteryMonitorPin = "A0"
BatteryMonitorPollInterval = 10000 # milli-seconds

##############################################################
#                                                            #
# The NeoPixel Ring                                          #
#                                                            #
##############################################################
# NeoPixels are a RGB LED that are configured via a single
# data line, these can be cascaded allowing strings of
# NeoPixels to be connected with each pixel being able to be
# controlled.  This can make for some fantastic displays.
EnableStomachNeoPixel = True
StomachNeoPixelAttachment = "arduinoNano"   # This was attached to a secondary board
StomachNeoPixelPin = 8                      # 2
StomachNeoPixelNumber = 23                  # 16
StomachNeoPixelMode = 0                     # This is how we will use the Neopixel ring/s