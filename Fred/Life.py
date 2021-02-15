#######################################################
# Program Code for Fred Inmoov
# Of the Cyber_One YouTube Channel
# https://www.youtube.com/cyber_one
#
# This is version 5
# Divided up into sub programs
#
# Running on MyRobotLab (MRL) http://myrobotlab.org/
# Fred in a modified Inmmov robot, you can find all the
# origonal files on the Inmoov web site. http://inmoov.fr/ 
#
# Life.py
# This file is to start all the servos 
# used in the head
#                                                     #
#######################################################
print "Creating the various life simulation functions"

EnableBlinking=True

# To make is a bit easier to control, we define functions to move the two eyes togeter.
# if you have only the one servo for each of these axis, then comment out the RightEyeLR and the RightEyeUD lines.
def eyesLR(eyesLRpos):
	RightEyeLR.moveTo(eyesLRpos)
	LeftEyeLR.moveTo(eyesLRpos)

def eyesUD(eyesUDpos):
	RightEyeUD.moveTo(eyesUDpos)
	LeftEyeUD.moveTo(eyesUDpos)

# Routines to create the blinking motion
# we use the Clock service to provide a regular event that calls the blink procedure.
# one of the things we do within the blink routine is to change the blink interval to a random number between 5 and 10 seconds.
# future enhancements may include shifting the random range based on the current light levels and the average light levels,
# blink more often when the light levels increase until an average value has been reached.
print "-Eye blinking"
if EnableBlinking == True:
    BlinkClock = Runtime.createAndStart("BlinkClock", "Clock")

if EnableBlinking == True:
    def blink(timedata):
        UpperEyeLid.moveTo(150) # close the upper eye lid
        LowerEyeLid.moveTo(150) # close the lower eye lid
        sleep(0.5)
        UpperEyeLid.moveTo(45) # Open the upper eye lid
        LowerEyeLid.moveTo(45) # Open the lower eye lid
        BlinkClock.setInterval(randint(5000, 10000)) # Set a new random time for the next blink

if EnableBlinking == True:
# the addListener() call will run the python routine "blink" whenever the pulse event occurs.
    BlinkClock.addListener("pulse", python.name, "blink")
# Initially, we will set the blink interval at 10 seconds.
    BlinkClock.setInterval(10000)
# Then we start the clock running.
    print "--Start Blink Clock"
    BlinkClock.startClock()
