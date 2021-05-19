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
# The NeoPixel Ring                                          #
#                                                            #
##############################################################
EnableStomachNeoPixel = True
StomachNeoPixelAttachment = "arduinoNano"
StomachNeoPixelPin = 8
StomachNeoPixelsNumber = 23
