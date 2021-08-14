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
# If a new controller is released or more servos are added, 
# then add it to this list and to each of the servos in the 
# related Servo.py file.  In this case 1_Servos_Head.py
# Comments after the setting are for a Nervo Boards based 
# InMoov configuration as listed on the InMoov web site.
# In some cases, the direction of travel is sometime in the
# oposite direction to what we need.  In this case, swap the
# Min and Max pos, this will swap the direction to what we need.

# The Jaw
# There are a few different variations on how the mechanics
# of this works, but essentially, rotating the servo closes
# the jaw while rotating it the other way opens it.
EnableJawServo = True # True or False
# This is the controller the Jaw Servo is attached to
JawAttachment = "Head"          # "arduinoLeft"
# The controller will have a number of pis, this is the pin 
# this servo is connected to.
JawPin = 9                      # 26
# The is the value from testing where the Jaw is all the way closed.
JawMinPos = 70                  # 10
# This is the value from testing where the jaw is all the way open
JawMaxPos = 140                 # 25
# This is the speed that the moves at. -1 is no speed limit,
# the jaw will move as fast as possible.
JawVelocity = -1                #


# In the original design, there are only two servos for the
# eyes, the X and Y servos.  Later, another servo was added
# for eye lids.
# In the Advanced Eye Mech by Dakota76, there are 6 servo used

# The Right Eye X-Axis (Left / Right motion)
EnableRightEyeX = True
RightEyeXAttachment = "Head"    # "arduinoLeft"
RightEyeXPin = 15               # 22
RightEyeXMinPos = 0             # 60
RightEyeXMaxPos = 180           # 120
RightEyeXVelocity = -1          #

# The Right Eye Y-Axis (Up / Down Motion)
EnableRightEyeY = True
RightEyeYAttachment = "Head"    # "arduinoLeft"
RightEyeYPin = 14               # 24
RightEyeYMinPos = 0             # 60
RightEyeYMaxPos = 180           # 120
RightEyeYVelocity = -1          #

# The Left Eye X-Axis (Left / Right motion)
# The Advance Eye Mech by Dakota76 has servos for both eyes.
EnableLeftEyeX = True
LeftEyeXAttachment = "Head"     # Not Present
LeftEyeXPin = 13                #
LeftEyeXMinPos = 0              #
LeftEyeXMaxPos = 180            #
LeftEyeXVelocity = -1           #

# The Left Eye Y-Axis (Up / Down Motion)
EnableLeftEyeY = True
LeftEyeYAttachment = "Head"     # Not Present
LeftEyeYPin = 12                #
LeftEyeYMinPos = 180            #
LeftEyeYMaxPos = 0              #
LeftEyeYVelocity = -1           #

# The Right Upper Eye Lid
EnableRightUpperEyeLid = True
UpperREyeLidAttachment = "Head" # "arduinoRight"
UpperREyeLidPin = 11            # 13
UpperREyeLidMinPos = 150        # 60
UpperREyeLidMaxPos = 45         # 120
UpperREyeLidVelocity = -1       #

# The Right Lower Eye Lid
# The Advance Eye Mech by Dakota76 has both upper
# and lower Eye Lids controlled a single servo each.
EnableRightLowerEyeLid = True
LowerREyeLidAttachment = "Head" # Not Present
LowerREyeLidPin = 10            #
LowerREyeLidMinPos = 0          #
LowerREyeLidMaxPos = 30         #
LowerREyeLidVelocity = -1       #

# The Left Upper Eye Lid.
# There is a proposed design that may support Left
# and right, Upper and Lower eye lids, so provision
# has been made for them :-)
EnableLeftUpperEyeLid = False
UpperLEyeLidAttachment = "Head" # Not Present
UpperLEyeLidPin = 9             # 
UpperLEyeLidMinPos = 45         # 
UpperLEyeLidMaxPos = 150        # 
UpperLEyeLidVelocity = -1       # 

# The Left Lower Eye Lid.
# There is a proposed design that may support Left
# and right, Upper and Lower eye lids, so provision
# has been made for them :-)
EnableLeftLowerEyeLid = False
LowerLEyeLidAttachment = "Head" # Not Present
LowerLEyeLidPin = 8             #
LowerLEyeLidMinPos = 0          #
LowerLEyeLidMaxPos = 120        #
LowerLEyeLidVelocity = -1       #

##############################################################
#                                                            #
# Advanced Head Group                                        #
# Added at Shido's request to support his advanced jaw and   #
# eyebrow design                                             #
#                                                            #
##############################################################
## The lateral jaw.
## This will allow the jaw to move side to side.
## Both lateral law servos will be connected on the same pin.
EnableLatJaw = False
LatJawAttachment = "Head" # Not Present
LatJawPin = 1             #
LatJawMinPos = 0          #
LatJawMaxPos = 180        #
LatJawVelocity = -1       #

## The inner right eyebrow.
## This will allow the eyebrow to move up and down.
EnableRBrowIn = False
RBrowInAttachment = "Head" # Not Present
RBrowInPin = 2             #
RBrowInMinPos = 0          #
RBrowInMaxPos = 180        #
RBrowInVelocity = -1       #

## The outter right eyebrow.
## This will allow the eyebrow to move up and down.
EnableRBrowOut = False
RBrowOutAttachment = "Head" # Not Present
RBrowOutPin = 3             #
RBrowOutMinPos = 0          #
RBrowOutMaxPos = 180        #
RBrowOutVelocity = -1       #

## The inner left eyebrow.
## This will allow the eyebrow to move up and down.
EnableLBrowIn = False
LBrowInAttachment = "Head" # Not Present
LBrowInPin = 4             #
LBrowInMinPos = 0          #
LBrowInMaxPos = 180        #
LBrowInVelocity = -1       #

## The outter left eyebrow.
## This will allow the eyebrow to move up and down.
EnableLBrowOut = False
LBrowOutAttachment = "Head" # Not Present
LBrowOutPin = 5             #
LBrowOutMinPos = 0          #
LBrowOutMaxPos = 180        #
LBrowOutVelocity = -1       #