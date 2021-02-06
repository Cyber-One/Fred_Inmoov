########################################
#
# Program Code for Fred Inmoov
# Of the Cyber_One YouTube Channel
#
# This is version 4.0 
# Using a Raspberry Pi 4B+ with 8GB of RAM
# An Adafruit PCA9685 16 Ch servo drivers in the Head
# with 6 PDI-1109MG for the eyes plus 
# 2 PDI-6221MG servos, Head Yaw and the Jaw
# An Adafruit PCA9685 16 Ch servo drivers in the back
# A PDI-6221MG servos for the Head Pitch, 
# An MG966R servo as a slave to a PDI-6221MG as the master for the Head Roll.
# An Arduino Nano with 2 x Ultra-Sonic sensors and a PIR sensor.
#
########################################
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)

# start the Raspberry Pi service
RasPi = Runtime.createAndStart("RasPi","RasPi")

# Setup the Adafruit 16 Channel I2C Servo driver based on the PCA9685 I2C PWM chip
# First we create the service and set it name to Head.
Head = Runtime.createAndStart("Head","Adafruit16CServoDriver")
# Next we attach the Head service to the Rapberry Pi service "RasPi" using I2C bus "1" at I2C Address "0x40". This is a Hex address.
# Note the I2C bus on the Arduino's are on channel 0, the Raspberry Pi I2C bus 0 is used for the SD Card :-)
Head.attach("RasPi","1","0x40")

# Next we repeat the above for the Torso board configured for I2C Address "0x41"
Torso = Runtime.createAndStart("Torso","Adafruit16CServoDriver")
Torso.attach("RasPi","1","0x41")

# We also now have an Arduino Nano connected using /dev/ttyUSB0
arduino = Runtime.start("arduino","Arduino")
arduino.setBoardNano()
arduino.connect("/dev/ttyUSB0")
sleep(1)
arduino.broadcastState()

# Start the clock services
BlinkClock = Runtime.createAndStart("BlinkClock","Clock")
AwakeClock = Runtime.createAndStart("AwakeClock","Clock")
Awake = False

#######################################################
#                                                     #
# Lets  define the servos attached to the Head        #
#                                                     #
#######################################################

# Change the names of the servos and the pin numbers to your usage
RightEyeLR = Runtime.createAndStart("RightEyeLR", "Servo")
# attach it to the pwm board - pin 15
RightEyeLR.attach(Head,15)
# Next lets set the various limits and mappings.
RightEyeLR.setMinMax(0,180)
RightEyeLR.map(0,180,1,180)
RightEyeLR.setRest(90)
RightEyeLR.setInverted(False)
RightEyeLR.setVelocity(60)
RightEyeLR.setAutoDisable(True)
RightEyeLR.rest()

RightEyeUD = Runtime.createAndStart("RightEyeUD", "Servo")
# attach it to the pwm board - pin 14
RightEyeUD.attach(Head,14)
RightEyeUD.setMinMax(0,180)
RightEyeUD.map(0,180,1,180)
RightEyeUD.setRest(90)
RightEyeUD.setInverted(False)
RightEyeUD.setVelocity(120)
RightEyeUD.setAutoDisable(True)
RightEyeUD.rest()


LeftEyeLR = Runtime.createAndStart("LefttEyeLR", "Servo")
# attach it to the pwm board - pin 13
LeftEyeLR.attach(Head,13)
LeftEyeLR.setMinMax(0,180)
LeftEyeLR.map(0,180,1,180)
LeftEyeLR.setRest(90)
LeftEyeLR.setInverted(False)
LeftEyeLR.setVelocity(120)
LeftEyeLR.setAutoDisable(True)
LeftEyeLR.rest()


LeftEyeUD = Runtime.createAndStart("LeftEyeUD", "Servo")
# attach it to the pwm board - pin 12
LeftEyeUD.attach(Head,12)
LeftEyeUD.setMinMax(0,180)
LeftEyeUD.map(0,180,1,180)
LeftEyeUD.setRest(90)
LeftEyeUD.setInverted(False)
LeftEyeUD.setVelocity(60)
LeftEyeUD.setAutoDisable(True)
LeftEyeUD.rest()


UpperEyeLid = Runtime.createAndStart("UpperEyeLid", "Servo")
# attach it to the pwm board - pin 11
UpperEyeLid.attach(Head,11)
UpperEyeLid.setMinMax(60,180)
UpperEyeLid.map(0,180,60,180)
UpperEyeLid.setRest(45)
UpperEyeLid.setInverted(False)
UpperEyeLid.setVelocity(-1)
UpperEyeLid.setAutoDisable(False)
# UpperEyeLid.rest()


LowerEyeLid = Runtime.createAndStart("LowerEyeLid", "Servo")
# attach it to the pwm board - pin 10
LowerEyeLid.attach(Head,10)
LowerEyeLid.setMinMax(0,120)
LowerEyeLid.map(0,180,0,120)
LowerEyeLid.setRest(30)
LowerEyeLid.setInverted(False)
LowerEyeLid.setVelocity(-1)
LowerEyeLid.setAutoDisable(False)
# LowerEyeLid.rest()


Jaw = Runtime.createAndStart("Jaw", "Servo")
# attach it to the pwm board - pin 9
Jaw.attach(Head,9)
Jaw.setMinMax(0,180)
Jaw.map(0,180,1,180)
Jaw.setRest(90)
Jaw.setInverted(False)
Jaw.setVelocity(-1)
Jaw.setAutoDisable(True)
#Jaw.rest()

HeadYaw = Runtime.createAndStart("HeadYaw", "Servo")
# attach it to the pwm board - pin 8
HeadYaw.attach(Head,8)
HeadYaw.setMinMax(0,180)
HeadYaw.map(0,180,1,180)
HeadYaw.setRest(90)
HeadYaw.setInverted(False)
HeadYaw.setVelocity(120)
HeadYaw.setAutoDisable(True)
HeadYaw.rest()

#######################################################
#                                                     #
# Now lets define the servos attached to the back.    #
#                                                     #
#######################################################

HeadPitch = Runtime.createAndStart("HeadPitch", "Servo")
# attach it to the pwm board - pin 7
HeadPitch.attach(Torso,7)
HeadPitch.setMinMax(0,180)
HeadPitch.map(0,180,1,180)
HeadPitch.setRest(90)
HeadPitch.setInverted(False)
HeadPitch.setVelocity(120)
HeadPitch.setAutoDisable(True)
HeadPitch.rest()

HeadRoll = Runtime.createAndStart("HeadRoll", "Servo")
# attach it to the pwm board - pin 6
HeadRoll.attach(Torso,6)
HeadRoll.setMinMax(0,180)
HeadRoll.map(0,180,1,180)
HeadRoll.setRest(90)
HeadRoll.setInverted(False)
HeadRoll.setVelocity(120)
HeadRoll.setAutoDisable(True)
HeadRoll.rest()


#######################################################
#                                                     #
# Now lets define the devices attached to the Ardunio.#
#                                                     #
#######################################################

# Create the PIR service
pir = Runtime.start('pir','Pir')
pir.attach(arduino,2 ) # arduino is controler like i2c arduino ... / 2 is pin number
# pir start
pir.isVerbose=True
pir.enable(1) # 1 is how many time / second we poll the pir
# event listener
pir.addListener("publishSense",python.name,"publishSense")
 
def publishSense(event):
  if event:print "Warm body movement detected !!!"

LeftUltraSonic = Runtime.start("LeftUltraSonic", "UltrasonicSensor")
LeftUltraSonic.attach(arduino, 12, 11)
LeftUltraSonic.addRangeListener(python)
  
RightUltraSonic = Runtime.start("RightUltraSonic", "UltrasonicSensor")
RightUltraSonic.attach(arduino, 10, 9)
RightUltraSonic.addRangeListener(python)

# Both the Ultra-Sonic sensor service will call the same onRange function in Python.
def onRange(distance):
  print "distance ", distance, " cm"

# we can use the blocking call 

# print "on demand range is ", LeftUltraSonic.range()
# print "on demand range is ", RightUltraSonic.range()

# you can also ping - ping does not do any calculations
# it simply returns the duration in microseconds of the ping

# print "ping ", LeftUltraSonic.ping(), " microseconds"
# print "ping ", RightUltraSonic.ping(), " microseconds"

# event driven ranging
# start ranging for 5 seconds - the publishRange(distance) will be
# called for every attempt to range - this SHOULD NOT INTERFERE WITH SERVOS
# YAY !
# the even ranging DOES NOT USE Arduino's pulseIn() method -
# at the moment range() & ping() do

# LeftUltraSonic.startRanging()
# sleep(5)
# LeftUltraSonic.stopRanging()
# RightUltraSonic.startRanging()
# sleep(5)
# RightUltraSonic.stopRanging()

#######################################################
#                                                     #
# Now lets define the Speech services and AI system.  #
#                                                     #
#######################################################

# TTS speech 
mouth = Runtime.createAndStart("mouth", "MarySpeech")
#mouth.setVoice("cmu-bdl-hsmm") # Mark
mouth.setVoice("cmu-rms-hsmm") # Henry
#mouth.setVoice("dfki-obadiah-hsmm") # Obadiah
#mouth.setVoice("dfki-spike-hsmm") # Spike
#mouth.installComponentsAcceptLicense("dfki-obadiah-hsmm") #Use this line to install more voice files
mouth.setVolume(100.0)

# create ear Speech Recognition Service
ear = Runtime.createAndStart("ear","Sphinx")
# prevent infinite loop - this will suppress the
# recognition when speaking - default behavior
# when attaching an ear to a mouth :)
ear.attach(mouth)

# Jaw control based on speech.
mouthcontrol = Runtime.create("mouthcontrol","MouthControl")
mouthcontrol.setJaw(Jaw)
mouthcontrol.setMouth(mouth)
mouthcontrol.setmouth(77, 120)
mouthcontrol.setdelays(60, 60, 70)
mouthcontrol.startService()

# create a ProgramAB service and start a session
Fred = Runtime.start("Fred", "ProgramAB")
Fred.startSession("Ray")
# create a route which sends published Responses to the
# mouth.speak(String) method
Fred.addTextListener(mouth)
# Next lets create a route that sends the speech our 
# robot has heard to the ProgramAB
ear.addTextListener(Fred)

#######################################################
#                                                     #
# Now lets define the miscilanous functions to bring  #
# the robot to life                                   #
#                                                     #
#######################################################

# To make is a bit easier to control, we define functions to move the two eyes togeter.
def eyesLR(eyesLRpos):
	RightEyeLR.moveTo(eyesLRpos)
	LeftEyeLR.moveTo(eyesLRpos)

def eyesUD(eyesUDpos):
	RightEyeUD.moveTo(eyesUDpos)
	LeftEyeUD.moveTo(eyesUDpos)

# Routine to create the blinking motion
def blink(timedata):
	UpperEyeLid.moveTo(150) # close the upper eye lid
	LowerEyeLid.moveTo(150) # close the lower eye lid
	sleep(0.5)
	UpperEyeLid.moveTo(45) # Open the upper eye lid
	LowerEyeLid.moveTo(45) # Open the lower eye lid
	BlinkClock.setInterval(randint(5000, 10000)) # Set a new random time for the next blink

BlinkClock.addListener("pulse", python.name, "blink")
BlinkClock.setInterval(10000)
BlinkClock.startClock()

# Define Wakeup and sleep routines.
def WakeSleep(timedata):
	if Awake == False:
		BlinkClock.startClock()
		Awake = True	# need to add a wake up sequence here.
	else:
		BlinkClock.stopClock()
		Awake = False	# need to add a going to sleep sequence here.

sleep(10.0)

UpperEyeLid.moveTo(45)
LowerEyeLid.moveTo(45)
Jaw.moveTo(77)
eyesLR(0)
sleep(2.0)
eyesLR(180)
sleep(2.0)
eyesLR(90)
UpperEyeLid.moveTo(45)
LowerEyeLid.moveTo(45)

mouth.speakBlocking(u"Hello world, I am awake.")
# begin listening
ear.startListening()
sleep(10)
Fred.getResponse(u"What time is it?")

#mouth.speak(u"I wonder if non blocking is a good idea?")
