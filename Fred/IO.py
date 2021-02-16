#######################################################
# Program Code for Fred InMoov
# Of the Cyber_One YouTube Channel
# https://www.youtube.com/cyber_one
#
# This is version 5
# Divided up into sub programs
#
# Running on MyRobotLab (MRL) http://myrobotlab.org/
# Fred in a modified InmMoov robot, you can find all the
# origonal files on the Inmoov web site. http://inmoov.fr/ 
#
# IO.py
# This file handels the various Sensors and outputs
# not already covered in other modules
#                                                     #
#######################################################
print "Creating the various IO Services"

#######################################################
# Create the PIR service                              #
#######################################################
# Passive Inrea Red (PIR) works on the principle that a warm body emits
# Infra Red (IR) light. The level of this light can indicate the current temperature.
# PIR sensors, use a single sensing element to measure the ambient IR level.
# By using a segmented lens in front of the sensor, there will be areas where the sensor
# can not see the IR levels, and areas where it is amplified.  
# As a warm body such as a person moves from one area to another, there is a large change
# in the IR levels detected, when this change occurs the output of the PIR sensor is turned on.
pir = Runtime.start('pir','Pir')
pir.attach(arduinoNano,2 ) # arduinoNano is controler like i2c arduinoNano ... / 2 is pin number
# pir start
pir.isVerbose=True
pir.enable(1) # 1 is how many time per second we poll the PIR input.
# event listener
pir.addListener("publishSense",python.name,"publishSense")
def publishSense(event):
  if event:print "Warm body movement detected !!!"


#######################################################
# Create the Ultrasonic services                      #
#######################################################
LeftUltraSonic = Runtime.start("LeftUltraSonic", "UltrasonicSensor")
LeftUltraSonic.attach(arduinoNano, 12, 11)
LeftUltraSonic.addRangeListener(python)
  
RightUltraSonic = Runtime.start("RightUltraSonic", "UltrasonicSensor")
RightUltraSonic.attach(arduinoNano, 10, 9)
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
