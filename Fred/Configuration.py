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
# Configuration.py                                           #
# This is where the configuration settings will live.        #
# As well as some of the global variable initilisations      #
#                                                            #
##############################################################
print "Creating the Config"

##############################################################
#                                                            #
# The Graphical User Interface (GUI)                         #
#                                                            #
##############################################################

# SwingGUI was the origonal one and still my prefference 
# until the rest of the WebGUI pages are conpleted.
RunSwingGUI = True  # True for on, False for off

# WebGUI is the new boy on the block and is getting better.
# It will be started in anycase if you decide to use 
# WebKitSpeechRecognition.
RunWebGUI = False   # True for on, False for off


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


##############################################################
#                                                            #
# Servo Head Group                                           #
#                                                            #
##############################################################

# Each servo has a number of parameters that need to be setup 
# before it can be used, these include where it's attached 
# and how far it can be moved.
# In the InMoov scripts and services, it assumes that your 
# servos are connected to one of the Arduino Mega 2560's.
# In the case of Fred using the PCA9685, this is not the case.
# In this config, the only assumption I will make is that the
# Servo will be attaches somewhere :-)
# The default values will be one of our controllers.
# "arduinoLeft", "arduinoRight", "arduinoNano", "Head", 
# "Back", "RightArm", "LeftArm".
# If a new controller is released of more are added, 
# then add it to this list.
# Comments after the setting are for a Nervo Boards based 
# InMoov configuration as listed on the InMoov web site.

# The Jaw
EnableJawServo = True # True or False
JawAttachment = "Head"          # "arduinoLeft"
JawPin = 9                      # 26
JawMinPos = 0                   # 10
JawMaxPos = 180                 # 25
JawRestPos = 90                 # 10

EnableRightEyeX = True
RightEyeXAttachment = "Head"    # "arduinoLeft"
RightEyeXPin = 15               # 22
RightEyeXMinPos = 0             # 60
RightEyeXMaxPos = 180           # 120
RightEyeXRestPos = 90           # 90

EnableRightEyeY = True
RightEyeYAttachment = "Head"    # "arduinoLeft"
RightEyeYPin = 14               # 24
RightEyeYMinPos = 0             # 60
RightEyeYMaxPos = 180           # 120
RightEyeYRestPos = 90           # 90

EnableLeftEyeX = True
LeftEyeXAttachment = "Head"     # Not Present
LeftEyeXPin = 13                #
LeftEyeXMinPos = 0              #
LeftEyeXMaxPos = 180            #
LeftEyeXRestPos = 90            #

EnableLeftEyeY = True
LeftEyeYAttachment = "Head"     # Not Present
LeftEyeYPin = 12                #
LeftEyeYMinPos = 0              #
LeftEyeYMaxPos = 180            #
LeftEyeYRestPos = 90            #

EnableUpperEyeLid = True
UpperEyeLidAttachment = "Head"  # "arduinoRight"
UpperEyeLidPin = 11             # 13
UpperEyeLidMinPos = 45          # 60
UpperEyeLidMaxPos = 180         # 120
UpperEyeLidRestPos = 45         # 60

EnableLowerEyeLid = True
LowerEyeLidAttachment = "Head"  # Not Present
LowerEyeLidPin = 10             #
LowerEyeLidMinPos = 0           #
LowerEyeLidMaxPos = 120         #
LowerEyeLidRestPos = 30         #

##############################################################
#                                                            #
# Servo Neck Group                                           #
#                                                            #
##############################################################

EnableHeadYaw = True
HeadYawAttachment = "Head"      # "arduinoLeft"
HeadYawPin = 8                  # 13
HeadYawMinPos = 0               # 30
HeadYawMaxPos = 180             # 150
HeadYawRestPos = 90             # 90

EnableHeadPitch = True
HeadPitchAttachment = "Back"    # "arduinoLeft"
HeadPitchPin = 7                # 12
HeadPitchMinPos = 0             # 20
HeadPitchMaxPos = 180           # 160
HeadPitchRestPos = 90           # 90

EnableHeadRoll = True
HeadRollAttachment = "Back"     # "arduinoRight"
HeadRollPin = 6                 # 13
HeadRollMinPos = 0              # 60
HeadRollMaxPos = 180            # 130
HeadRollRestPos = 90            # 90

##############################################################
#                                                            #
# Servo Torso Group                                          #
#                                                            #
##############################################################

EnableTopStomach = False
TopStomachAttchment = "Back"    # "arduinoLeft"
TopStomachPin = 8               # 27
TopStomachMinPos = 0            # 60
TopStomachMaxPos = 180          # 120
TopStomachRestPos = 90          # 90

EnableMidStomach = False
MidStomachAttchment = "Back"    # "arduinoLeft"
MidStomachPin = 9               # 28
MidStomachMinPos = 0            # 60
MidStomachMaxPos = 180          # 120
MidStomachRestPos = 90          # 90

##############################################################
#                                                            #
# Servo Right Arm Group                                      #
#                                                            #
##############################################################

EnableRightOmoPlate = False
RightOmoPlateAttachment = "Back"# "arduionRight"
RightOmoPlatePin = 1            # 11
RightOmoPlateMinPos = 0         # 10
RightOmoPlateMaxPos = 180       # 80
RightOmoPlateRestPos = 90       # 10

EnableRightShoulder = False
RightShoulderAttachment="Back"  # "arduionRight"
RightShoulderPin = 2            # 10
RightShoulderMinPos = 0         # 0
RightShoulderMaxPos = 180       # 180
RightShoulderRestPos = 90       # 30

EnableRightRotate = False
RightRotateAttachment = "Back"  # "arduionRight"
RightRotatePin = 3              # 9
RightRotateMinPos = 0           # 40
RightRotateMaxPin = 180         # 180
RightRotateRestPOs = 90         # 90

EnableRightBicep = False
RightBicepAttachment ="RightArm"# "arduioRight"
RightBicepPin = 1               # 8
RightBicepMinPos = 0            # 0
RightBicepMaxPos = 180          # 90
RightBicepRestPos = 90          # 0

##############################################################
#                                                            #
# Servo Left Arm Group                                       #
#                                                            #
##############################################################

EnableLeftOmoPlate = False
LeftOmoPlateAttachment = "Back" # "arduioLeft"
LeftOmoPlatePin = 15            # 11
LeftOmoPlateMinPos = 0          # 10
LeftOmoPlateMaxPos = 180        # 80
LeftOmoPlateRestPos = 90        # 10

EnableLeftShoulder = False
LeftShoulderAttachment = "Back" # "arduioLeft"
LeftShoulderPin = 14            # 10
LeftShoulderMinPos = 0          # 0
LeftShoulderMaxPos = 180        # 180
LeftShoulderRestPos = 90        # 30

EnableLeftRotate = False
LeftRotateAttachment = "Back"   # "arduioLeft"
LeftRotatePin = 13              # 9
LeftRotateMinPos = 0            # 40
LeftRotateMaxPin = 180          # 180
LeftRotateRestPOs = 90          # 90

EnableLeftBicep = False
LeftBicepAttachment = "LeftArm" # "arduioLeft"
LeftBicepPin = 1                # 8
LeftBicepMinPos = 0             # 0
LeftBicepMaxPos = 180           # 90
LeftBicepRestPos = 90           # 0

##############################################################
#                                                            #
# Servo Right Hand Group                                     #
#                                                            #
##############################################################

EnableRightThumb = False
RightThumbAttachment ="RightArm"# "arduioRight"
RightThumbPin = 2               # 2
RightThumbMinPos = 0            # 0
RightThumbMaxPos = 180          # 180
RightThumbRestPos = 0           # 0

EnableRightIndex = False
RightIndexAttachment ="RightArm"# "arduioRight"
RightIndexPin = 2               # 3
RightIndexMinPos = 0            # 0
RightIndexMaxPos = 180          # 180
RightIndexRestPos = 0           # 0

EnableRightMajor = False
RightMajorAttachment ="RightArm"# "arduioRight"
RightMajorPin = 2               # 4
RightMajorMinPos = 0            # 0
RightMajorMaxPos = 180          # 180
RightMajorRestPos = 0           # 0

EnableRightRing = False
RightRingAttachment = "RightArm"# "arduioRight"
RightRingPin = 2                # 5
RightRingMinPos = 0             # 0
RightRingMaxPos = 180           # 180
RightRingRestPos = 0            # 0

EnableRightPinky = False
RightPinkyAttachment ="RightArm"# "arduioRight"
RightPinkyPin = 2               # 6
RightPinkyMinPos = 0            # 0
RightPinkyMaxPos = 180          # 180
RightPinkyRestPos = 0           # 0

EnableRightWrist = False
RightWristAttachment ="RightArm"# "arduioRight"
RightWristPin = 2               # 7
RightWristMinPos = 0            # 0
RightWristMaxPos = 180          # 180
RightWristRestPos = 0           # 0

##############################################################
#                                                            #
# Servo Left Hand Group                                      #
#                                                            #
##############################################################

EnableLeftThumb = False
LeftThumbAttachment = "LeftArm" # "arduioLeft"
LeftThumbPin = 2                # 2
LeftThumbMinPos = 0             # 0
LeftThumbMaxPos = 180           # 180
LeftThumbRestPos = 0            # 0

EnableLeftIndex = False
LeftIndexAttachment = "LeftArm" # "arduioLeft"
LeftIndexPin = 2                # 3
LeftIndexMinPos = 0             # 0
LeftIndexMaxPos = 180           # 180
LeftIndexRestPos = 0            # 0

EnableLeftMajor = False
LeftMajorAttachment = "LeftArm" # "arduioLeft"
LeftMajorPin = 2                # 4
LeftMajorMinPos = 0             # 0
LeftMajorMaxPos = 180           # 180
LeftMajorRestPos = 0            # 0

EnableLeftRing = False
LeftRingAttachment = "LeftArm"  # "arduioLeft"
LeftRingPin = 2                 # 5
LeftRingMinPos = 0              # 0
LeftRingMaxPos = 180            # 180
LeftRingRestPos = 0             # 0

EnableLeftPinky = False
LeftPinkyAttachment = "LeftArm" # "arduioLeft"
LeftPinkyPin = 2                # 6
LeftPinkyMinPos = 0             # 0
LeftPinkyMaxPos = 180           # 180
LeftPinkyRestPos = 0            # 0

EnableLeftWrist = False
LeftWristAttachment = "LeftArm" # "arduioLeft"
LeftWristPin = 2                # 7
LeftWristMinPos = 0             # 0
LeftWristMaxPos = 180           # 180
LeftWristRestPos = 0            # 0

##############################################################
#                                                            #
# Input / Output Device Group                                #
#                                                            #
##############################################################

EnablePIR = True
PirAttachment = "arduinoNano"   # "arduioLeft"
PirPin = 2                      # 23

EnableLeftUltrasonic = True
LeftUltrasonicAttachment = "arduinoNano"
LeftUltrasonicPin1 = 12
LeftUltrasonicPin2 = 11

EnableRightUltraSonic = True
RightUltrasonicAttachment = "arduinoNano"
RightUltrasonicPin1 = 10
RightUltrasonicPin2 = 9


##############################################################
#                                                            #
# Speech To Text and Text To Speech Group                    #
#                                                            #
##############################################################

# TTS Select only one of these options.
UseMarySpeech = True
UseMimicSpeech = False

# STT Select only one of these options.
UseSphinx = False
UseWebKit = True

##############################################################
#                                                            #
# Life Simulati9on Function Group                            #
#                                                            #
##############################################################



##############################################################
#                                                            #
# System wide global variable creation                       #
#                                                            #
##############################################################

# This is how much quiet time must elapse for the robot 
# goes to sleep. The time is in mili-seconds.
TimeToSleep = 15 * 60000    

# when the sleep timer is enabled, this allows the robot to sleep.
Awake = True                
