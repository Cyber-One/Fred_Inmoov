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
# 2_Controller_Config.py                                     #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Controller Config"
##############################################################
#                                                            #
# Level 1 Controllers                                        #
#                                                            #
##############################################################

# The Raspberry Pi 4 is a small Single Board Computer (SBC)
# with enough power to experiment and run a lot of MRL 
# services, just not all at once. :-)
# Built on to the Raspberry Pi are the 
# General Purpose Input Output (GPIO) pins.  Amonst these are
# and I2C bus, a TTL Serial, I2S Audio bus and other general 
# purpose configurable Inputs and Outputs. 
# Note: The I2C bus is on Port 1. Pins 2 (SDA) and Pin 3 (SCL)
#       I2C Port 0 is used for the uSD card.
##############################################################
## NOTE: the GPIO are 3.3V only, applying 5V to these pins  ##
## will destroy your Raspberry Pi SBC, You have been warned ##
##############################################################
EnableRaspberryPi = True   # True for on, False for off

# If you were to run the two Arduino Mega 2560 as used in a 
# standard build, This is where you enable them.
# Again each of the Arduino Mega 2560 have an I2C Port 0.
# Also make sure the USB port is listed correctly and the 
# MRL_COMM is installed on each arduino that you have installed
# Each of the Arduinos connect via USB, in the Rasberry Pi or
# on a Mac this will like "/dev/ttyUSB0".  On a Windows machine
# it will be "COM3" or "COM15". In either case you will need
# to determine what port your computer has it connected to.
# Arduino's can also act as Servo Drivers.
EnableArduinoLeft = False  # True for on, False for off
ArduinoLeftComPort = "/dev/ttyUSB1" # Refer to notes above

EnableArduinoRight = False # True for on, False for off
ArduinoRightComPort = "/dev/ttyUSB2" # Refer to notes above

# In the Fred build, I'm using an Arduino Nano for the two 
# Ultrasonic Sensors and the PIR sensor.
# The Arduino also has an I2C Port 0 if we need to use it.
EnableArduinoNano = True  # True for on, False for off
ArduinoNanoComPort = "/dev/ttyUSB0" # Refer to notes above

EnableArduinoNano2 = False  # True for on, False for off
ArduinoNano2ComPort = "/dev/ttyUSB1" # Refer to notes above


##############################################################
#                                                            #
# Level 2 Controllers. I2C based devices                     #
#                                                            #
##############################################################

# Our servo controllers in Fred are the Adafruit 16 channel 
# PWM Servo drivers.  With four of these installed we will 
# need to create four separate service, one for each.
# Next we need to attach the servo drivers to the Raspi4 or 
# the Arduino
# There are three parameters we need to set,
#
# The first parameter is the service we want to attach it to, 
# normally either the RasPi or one of the Arduinos,
# "arduinoLeft", "arduinoRight" or "arduinoNano"
# in our case it will be the Raspi4. "raspi"
#
# The second parameter is the bus, This is normally 1 for the
# RasPi or 0 for an Arduino.
#
# Each servo driver has a unique address that is hard coded
# by means of a set of jumpers on the controller boards, This
# is our Third parameter, There are seven jumpers that form
# a binary number that is added to 0x40. Note the 0x 
# indicates the number is in hexadecimal format that is base
# 16 and has values in the range:
# 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
# 0x40 is equal to 64 in decimal, the seven jumpers will give
# up to 128 possible address.
# Just be aware of any other I2C devices you have on the bus
# and what their address are, some device can not be changed
# or have a very limited number of selectable addresses.

EnableAdafruit16CServoDriverHead = True # True or False
HeadServoDriverAddr = "0x40"            # Refer to notes above
HeadServoDriverPort = "1"               # Refer to notes above
HeadServoDriverAttached = "raspi"       # Refer to notes above

EnableAdafruit16CServoDriverBack = True # True or False
BackServoDriverAddr = "0x41"            # Refer to notes above
BackServoDriverPort = "1"               # Refer to notes above
BackServoDriverAttached = "raspi"       # Refer to notes above

EnableAdafruit16CServoDriverLeftArm = False # True or False
LeftArmServoDriverAddr = "0x42"         # Refer to notes above
LeftArmServoDriverPort = "1"            # Refer to notes above
LeftArmServoDriverAttached = "raspi"    # Refer to notes above

EnableAdafruit16CServoDriverRightArm = False # True or False
RightArmServoDriverAddr = "0x43"        # Refer to notes above
RightArmServoDriverPort = "1"           # Refer to notes above
RightArmServoDriverAttached = "raspi"   # Refer to notes above

