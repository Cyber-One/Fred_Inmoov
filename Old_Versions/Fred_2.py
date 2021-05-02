########################################
#
# Program Code for Fred Inmoov
# Of the Cyber_One YouTube Channel
#
# This is version 2 with Blink and TTS
#
######################################### generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# start the service
raspi = Runtime.createAndStart("raspi","RasPi")

# Head.setController("RasPi","1","0x40")
Head = Runtime.createAndStart("Head","Adafruit16CServoDriver")
Head.attach("raspi","1","0x40")

# Start the clock services
BlinkClock = Runtime.createAndStart("BlinkClock","Clock")
AwakeClock = Runtime.createAndStart("AwakeClock","Clock")
Awake = False

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

HeadPitch = Runtime.createAndStart("HeadPitch", "Servo")
# attach it to the pwm board - pin 7
HeadPitch.attach(Head,7)
HeadPitch.setMinMax(0,180)
HeadPitch.map(0,180,1,180)
HeadPitch.setRest(90)
HeadPitch.setInverted(False)
HeadPitch.setVelocity(120)
HeadPitch.setAutoDisable(True)
HeadPitch.rest()

HeadRoll = Runtime.createAndStart("HeadRoll", "Servo")
# attach it to the pwm board - pin 6
HeadRoll.attach(Head,6)
HeadRoll.setMinMax(0,180)
HeadRoll.map(0,180,1,180)
HeadRoll.setRest(90)
HeadRoll.setInverted(False)
HeadRoll.setVelocity(120)
HeadRoll.setAutoDisable(True)
HeadRoll.rest()

# TTS speech 
mouth = Runtime.createAndStart("mouth", "MarySpeech")
#mouth.setVoice("cmu-bdl") # Mark
#mouth.setVoice("cmu-bdl-hsmm") # Mark
#mouth.setVoice("cmu-rms") # Henry
mouth.setVoice("cmu-rms-hsmm") # Henry
#mouth.setVoice("dfki-obadiah") # Obadiah
#mouth.setVoice("dfki-obadiah-hsmm") # Obadiah
#mouth.setVoice("dfki-spike") # Spike
#mouth.setVoice("dfki-spike-hsmm") # Spike
#mouth.installComponentsAcceptLicense("dfki-obadiah-hsmm") #Use this line to install more voice files
mouth.setVolume(100.0)

# Jaw control based on speech.
mouthcontrol = Runtime.create("mouthcontrol","MouthControl")
mouthcontrol.setJaw(Jaw)
mouthcontrol.setMouth(mouth)
mouthcontrol.setmouth(77, 120)
mouthcontrol.setdelays(60, 60, 70)
mouthcontrol.startService()

# Define Wakeup and sleep routines.
def WakeSleep(timedata):
	if Awake == False:
		BlinkClock.startClock()
		Awake = True	# need to add a wake up sequence here.
	else:
		BlinkClock.stopClock()
		Awake = False	# need to add a going to sleep sequence here.

# Routine to create the blinking motion
def blink(timedata):
	UpperEyeLid.moveTo(150) # close the upper eye lid
	LowerEyeLid.moveTo(150) # close the lower eye lid
	sleep(0.5)
	UpperEyeLid.moveTo(45) # Open the upper eye lid
	LowerEyeLid.moveTo(45) # Open the lower eye lid
	BlinkClock.setInterval(randint(5000, 10000)) # Set a new random time for the next blink

sleep(10.0)
BlinkClock.addListener("pulse", python.name, "blink")
BlinkClock.setInterval(10000)
BlinkClock.startClock()

def eyesLR(eyesLRpos):
	RightEyeLR.moveTo(eyesLRpos)
	LeftEyeLR.moveTo(eyesLRpos)

def eyesUD(eyesUDpos):
	RightEyeUD.moveTo(eyesUDpos)
	LeftEyeUD.moveTo(eyesUDpos)

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

#mouth.speak(u"I wonder if non blocking is a good idea?")
