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
# Load the configuration for the IO devices.
execfile(RuningFolder+'/1_Configuration/A_IO_Config.py')

#######################################################
# Create the PIR service                              #
#######################################################
# Test to make sure the configured controller is enabled.
if  not ((PirAttachment == "arduinoNano" and EnableArduinoNano) or (PirAttachment == "arduinoLeft" and EnableArduinoLeft) or (PirAttachment == "arduinoRight" and EnableArduinoRight)):
    EnablePIR = False

if EnablePIR:
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
    if PirAttachment == "arduinoNano":
        pir.attach(arduinoNano, PirPin) # arduinoNano
    if PirAttachment == "arduinoLeft":
        pir.attach(arduinoLeft, PirPin) # arduinoLeft
    if PirAttachment == "arduinoRight":
        pir.attach(arduinoRight, PirPin) # arduinoRight
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
# the Ultrasonic services has a couple of option on how you
# can use it. In anycase the max range from a software
# perspective is 5 meters.
# 1) ping()         This returns the time of flight in
#                   milli-seconds each time you call it.
#                   This is a On-Demand method.
# 2) range()        This gives you the distance in 
#                   centimeters each time you call it.
#                   This is a On-Demand method.
# 3) startRanging() The start and stop ranging methods
#    stopRanging()  produce a series of pulses with the
#                   results returning on the callback
#                   method, the default being onRange.
#                   This is normally setup using
#                   UltraSonic.addRangeListener(python)
#                   But we will use the subscribe method
#                   from the python service so we can 
#                   seperate the two sensors returns.

# Test to make sure the configured controller is enabled.
if  not ((LeftUltrasonicAttachment == "arduinoNano" and EnableArduinoNano) or (LeftUltrasonicAttachment == "arduinoLeft" and EnableArduinoLeft) or (LeftUltrasonicAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableLeftUltrasonic = False

if EnableLeftUltrasonic:
    LeftUltraSonic = Runtime.start("LeftUltraSonic", "UltrasonicSensor")
    if LeftUltrasonicAttachment == "arduinoNano":
        LeftUltraSonic.attach(arduinoNano, LeftUltrasonicPin1, LeftUltrasonicPin2)
    elif LeftUltrasonicAttachment == "arduinoLeft":
        LeftUltraSonic.attach(arduinoLeft, LeftUltrasonicPin1, LeftUltrasonicPin2)
    elif LeftUltrasonicAttachment == "arduinoRight":
        LeftUltraSonic.attach(arduinoRight, LeftUltrasonicPin1, LeftUltrasonicPin2)
    def onRangeLeft(distance):
        print "Left distance ", distance, " cm"
    #python.subscribe('LeftUltraSonic', 'onRange', 'python', 'onRangeLeft')

# Test to make sure the configured controller is enabled.
if not ((RightUltrasonicAttachment == "arduinoNano" and EnableArduinoNano) or (RightUltrasonicAttachment == "arduinoLeft" and EnableArduinoLeft) or (RightUltrasonicAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightUltraSonic = False
    
if EnableRightUltraSonic:
    RightUltraSonic = Runtime.start("RightUltraSonic", "UltrasonicSensor")
    if RightUltrasonicAttachment == "arduinoNano":
        RightUltraSonic.attach(arduinoNano, RightUltrasonicPin1, RightUltrasonicPin2)
    elif RightUltrasonicAttachment == "arduinoLeft":
        RightUltraSonic.attach(arduinoLeft, RightUltrasonicPin1, RightUltrasonicPin2)
    elif RightUltrasonicAttachment == "arduinoRight":
        RightUltraSonic.attach(arduinoRight, RightUltrasonicPin1, RightUltrasonicPin2)
    def onRangeRight(distance):
        print "Right distance ", distance, " cm"
    #python.subscribe('RightUltraSonic', 'onRange', 'python', 'onRangeRight')

##############################################################
#                                                            #
# The Battery Voltage Monitor                                #
#                                                            #
##############################################################
BatteryLevel = 0
# Test to make sure the configured controller is enabled.
if not ((BatteryMonitorAttachment == "arduinoNano" and EnableArduinoNano) or (BatteryMonitorAttachment == "arduinoLeft" and EnableArduinoLeft) or (BatteryMonitorAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableBatteryMonitor = False

if EnableBatteryMonitor:
    # Lets set a default value for the Battery Monitor value
    # Once the forst poll sequence is complete, this will be more accurate
    BatteryLevel = 1
    # Because we are dealing with the controller itself, we 
    # need to reference the controller directly.
    # That means creating the control program for each of 
    # the variations that may be used in the config.
    if BatteryMonitorAttachment == "arduinoNano":
        arduinoLeft.setAref("DEFAULT")
        def BattMonPublishedPins(pins):
            BatteryLevel = pins[pin].value
            arduinoLeft.disablePin(BatteryMonitorPin)
        arduinoLeft.addListener("publishPinArray","python","BattMonPublishedPins")
        def BattMonTimerPulse(timedata):
            arduinoLeft.enablePin(BatteryMonitorPin, 1)
    elif BatteryMonitorAttachment == "arduinoLeft":
        arduinoRight.setAref("DEFAULT")
        def BattMonPublishedPins(pins):
            BatteryLevel = pins[pin].value
            arduinoRight.disablePin(BatteryMonitorPin)
        arduinoRight.addListener("publishPinArray","python","BattMonPublishedPins")
        def BattMonTimerPulse(timedata):
            arduinoRight.enablePin(BatteryMonitorPin, 1)
    elif BatteryMonitorAttachment == "arduinoRight":
        arduinoNano.setAref("DEFAULT")
        def BattMonPublishedPins(pins):
            BatteryLevel = pins[pin].value
            arduinoNano.disablePin(BatteryMonitorPin)
        arduinoNano.addListener("publishPinArray","python","BattMonPublishedPins")
        def BattMonTimerPulse(timedata):
            arduinoNano.enablePin(BatteryMonitorPin, 1)
    # For the Battery Monitor to work, we need a timer to control the interval between tests
    BatteryMonitorTime = Runtime.createAndStart("BatteryMonitorTime", "Clock")
    # the addListener() call will run the python routine "BattMonTimerPulse" whenever the pulse event occurs.
    BatteryMonitorTime.addListener("pulse", python.name, "BattMonTimerPulse")
    # Initially, we will set the test interval at BatteryMonitorPollInterval milli-seconds.
    BatteryMonitorTime.setInterval(BatteryMonitorPollInterval)
    # Then we start the clock running.
    BatteryMonitorTime.startClock()
 
print "start to poll pin input"
arduino.enablePin(inputPin, 1)
sleep(5)
print "stop to poll pin input"
arduino.disablePin(inputPin)
##############################################################
#                                                            #
# The NeoPixel Ring                                          #
#                                                            #
##############################################################

# Test to make sure the configured controller is enabled.
if not ((StomachNeoPixelAttachment == "arduinoNano" and EnableArduinoNano) or (StomachNeoPixelAttachment == "arduinoLeft" and EnableArduinoLeft) or (StomachNeoPixelAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableStomachNeoPixel = False

# Before we even think about starting the NeoPixel Service,
# we need to make sure it's enabled.  The previous bit will
# disable the service if the controller is not available
if EnableStomachNeoPixel:
    # We use the standard method of starting a service in MRL
    StomachNeoPixel = Runtime.start("StomachNeoPixel","NeoPixel")
    # Next we attach the NeoPixel service to the configured controller.
    if StomachNeoPixelAttachment == "arduinoNano":
        StomachNeoPixel.attach(arduinoNano, StomachNeoPixelPin, StomachNeoPixelNumber)
    if StomachNeoPixelAttachment == "arduinoLeft":
        StomachNeoPixel.attach(arduinoLeft, StomachNeoPixelPin, StomachNeoPixelNumber)
    if StomachNeoPixelAttachment == "arduinoRight":
        StomachNeoPixel.attach(arduinoRight, StomachNeoPixelPin, StomachNeoPixelNumber)
# Thats it for this part of setting up the neo Pixels.
# The rest is done in the 6_Life_Functions/7_NeoPixel_Control.py program
