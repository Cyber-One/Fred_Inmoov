# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# start the service
raspi = Runtime.start("raspi","RasPi")

# Head.setController("RasPi","1","0x40")
Head = Runtime.start("Head","Adafruit16CServoDriver")
Head.attach("raspi","1","0x40")

# Start the clock services
BlinkClock = Runtime.start("BlinkClock","Clock")
AwakeClock = Runtime.start("AwakeClock","Clock")
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
RightEyeUD.setVelocity(60)
RightEyeUD.setAutoDisable(True)
RightEyeUD.rest()


LeftEyeLR = Runtime.createAndStart("LefttEyeLR", "Servo")
# attach it to the pwm board - pin 13
LeftEyeLR.attach(Head,13)
LeftEyeLR.setMinMax(0,180)
LeftEyeLR.map(0,180,1,180)
LeftEyeLR.setRest(90)
LeftEyeLR.setInverted(False)
LeftEyeLR.setVelocity(60)
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
Jaw.setVelocity(60)
Jaw.setAutoDisable(True)
Jaw.rest()

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
	UpperEyeLid.moveTo(150)
	LowerEyeLid.moveTo(150)
	sleep(0.5)
	UpperEyeLid.moveTo(45)
	LowerEyeLid.moveTo(45)
	BlinkClock.setInterval(randint(5000, 10000))

UpperEyeLid.moveTo(45)
LowerEyeLid.moveTo(45)
BlinkClock.addListener("pulse", python.name, "blink")
BlinkClock.setInterval(10000)
BlinkClock.startClock(True)

def eyesLR(eyesLRpos):
	RightEyeLR.moveTo(eyesLRpos)
	LeftEyeLR.moveTo(eyesLRpos)

def eyesUD(eyesUDpos):
	RightEyeUD.moveTo(eyesUDpos)
	LeftEyeUD.moveTo(eyesUDpos)

eyesLR(90)
eyesUD(90)



