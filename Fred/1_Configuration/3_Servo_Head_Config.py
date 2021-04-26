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
# 3_Servo_Head_Config.py                                     #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Servo Head Config"
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
# then add it to this list and to each of the servos in the 
# Servo.py file.
# Comments after the setting are for a Nervo Boards based 
# InMoov configuration as listed on the InMoov web site.

# The Jaw
EnableJawServo = True # True or False
JawAttachment = "Head"          # "arduinoLeft"
JawPin = 9                      # 26
JawMinPos = 70                  # 10
JawMaxPos = 140                 # 25
JawRestPos = 80                 # 10
JawVelocity = -1                #

EnableRightEyeX = True
RightEyeXAttachment = "Head"    # "arduinoLeft"
RightEyeXPin = 15               # 22
RightEyeXMinPos = 0             # 60
RightEyeXMaxPos = 180           # 120
RightEyeXRestPos = 90           # 90
RightEyeXVelocity = 60          #

EnableRightEyeY = True
RightEyeYAttachment = "Head"    # "arduinoLeft"
RightEyeYPin = 14               # 24
RightEyeYMinPos = 0             # 60
RightEyeYMaxPos = 180           # 120
RightEyeYRestPos = 90           # 90
RightEyeYVelocity = 60          #

EnableLeftEyeX = True
LeftEyeXAttachment = "Head"     # Not Present
LeftEyeXPin = 13                #
LeftEyeXMinPos = 0              #
LeftEyeXMaxPos = 180            #
LeftEyeXRestPos = 90            #
LeftEyeXVelocity = 60           #

EnableLeftEyeY = True
LeftEyeYAttachment = "Head"     # Not Present
LeftEyeYPin = 12                #
LeftEyeYMinPos = 0              #
LeftEyeYMaxPos = 180            #
LeftEyeYRestPos = 90            #
LeftEyeYVelocity = 60           #

EnableRightUpperEyeLid = True
UpperREyeLidAttachment = "Head" # "arduinoRight"
UpperREyeLidPin = 11            # 13
UpperREyeLidMinPos = 45         # 60
UpperREyeLidMaxPos = 150        # 120
UpperREyeLidRestPos = 45        # 60
UpperREyeLidVelocity = -1       #

EnableRightLowerEyeLid = True
LowerREyeLidAttachment = "Head" # Not Present
LowerREyeLidPin = 10            #
LowerREyeLidMinPos = 0          #
LowerREyeLidMaxPos = 120        #
LowerREyeLidRestPos = 30        #
LowerREyeLidVelocity = -1       #

EnableLeftUpperEyeLid = False
UpperLEyeLidAttachment = "Head" # Not Present
UpperLEyeLidPin = 9             # 
UpperLEyeLidMinPos = 45         # 
UpperLEyeLidMaxPos = 150        # 
UpperLEyeLidRestPos = 45        # 
UpperLEyeLidVelocity = -1       # 

EnableLeftLowerEyeLid = False
LowerLEyeLidAttachment = "Head" # Not Present
LowerLEyeLidPin = 8             #
LowerLEyeLidMinPos = 0          #
LowerLEyeLidMaxPos = 120        #
LowerLEyeLidRestPos = 30        #
LowerLEyeLidVelocity = -1       #

