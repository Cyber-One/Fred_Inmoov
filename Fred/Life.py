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
# This file is to Simulate movements associated with a
# living entity
#                                                     #
#######################################################
#from cmath import math

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

# Pan and Tilt are the common methods of controlling a camera.
# normally, you would have a rotating base and the place a tilt mechinism on the pan base.
# we have a Pitch and Roll with the Yaw on top of that.
# When we look up at 20° and then turn the head 90° to the left,
# the head will end up with a tilt of 0° but the head will roll 20°
# to overcome this we need a Pan and Tilt translation.
# This function assumes that 0, 0, 0 is facing straight ahead with tilt and roll level.
def PanTilt(Pan, Tilt, Roll):
    HeadYaw.moveTo(90+Pan)
    PanRadians = math.radians(Pan)
    HeadPitch.moveTo(90+(Tilt*math.cos(PanRadians) + Roll*math.sin(PanRadians)))
    HeadRoll.moveTo(90+(Tilt*math.sin(PanRadians) + Roll*math.cos(PanRadians)))

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

