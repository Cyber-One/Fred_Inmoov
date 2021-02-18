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
# IO.py                                                      #
# This file handels the various Sensors and outputs          #
# not already covered in other modules                       #
#                                                            #
##############################################################
print "Creating the various IO Services"

#######################################################
# Create the PIR service                              #
#######################################################
if EnablePIR == True:
    # Passive Inrea Red (PIR) works on the principle that a 
    # warm body emits Infra Red (IR) light. The level of this 
    # light can indicate the current temperature.
    # PIR sensors, use a single sensing element to measure the 
    # ambient IR level.
    # By using a segmented lens in front of the sensor, there 
    # will be areas where the sensor can not see the IR 
    # levels, and areas where it is amplified.  
    # As a warm body such as a person moves from one area to 
    # another, there is a large change in the IR levels 
    # detected, when this change occurs the output of the PIR 
    # sensor is turned on.
    pir = Runtime.start('pir','Pir')
    pir.attach(PirAttachment, PirPin) # arduinoNano is controler like i2c arduinoNano ... / 2 is pin number
    # The isVerbose function is handy if your trying to debug 
    # the PIR sensor, If you are setting it to True can be 
    # handy, but a pain when trying to debug other bits of 
    # code :-)
    pir.isVerbose=False
    # pir enable is how we start the PIR sensor.
    # the value we pass it is how many time per second we poll 
    # the PIR input.
    pir.enable(1)
    # Once started, you can disable it by using the following line
    #pir.disable()
    # event listener
    #pir.addListener("publishSense",python.name,"publishSense")
    #def publishSense(event):
    #  if event:print "Warm body movement detected !!!"


#######################################################
# Create the Ultrasonic services                      #
#######################################################
if EnableLeftUltrasonic == True:
    LeftUltraSonic = Runtime.start("LeftUltraSonic", "UltrasonicSensor")
    LeftUltraSonic.attach(LeftUltrasonicAttachment, LeftUltrasonicPin1, LeftUltrasonicPin2)
    LeftUltraSonic.addRangeListener(python)

if EnableRightUltraSonic == True:
    RightUltraSonic = Runtime.start("RightUltraSonic", "UltrasonicSensor")
    RightUltraSonic.attach(RightUltrasonicAttachment, RightUltrasonicPin1, RightUltrasonicPin2)
    RightUltraSonic.addRangeListener(python)

# Both the Ultra-Sonic sensor service will call the same 
# onRange function in Python.
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
