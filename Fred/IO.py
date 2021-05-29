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
BatteryLevel = [0, 0, 0, 0]
# Test to make sure the configured controller is enabled.
if not ((BatteryMonitorAttachment == "arduinoNano" and EnableArduinoNano) or (BatteryMonitorAttachment == "arduinoLeft" and EnableArduinoLeft) or (BatteryMonitorAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableBatteryMonitor = 0

if EnableBatteryMonitor > 0 and EnableBatteryMonitor < 5:
    # Lets set a default value for the Battery Monitor value
    # Once the first poll sequence is complete, this will be more accurate
    BatteryLevel[0] = 1
    if EnableBatteryMonitor > 1:
        BatteryLevel[1] = 1
    if EnableBatteryMonitor > 2:
        BatteryLevel[2] = 1
    if EnableBatteryMonitor > 3:
        BatteryLevel[3] = 1
    def BattMonPublishedPins(pins):
        for pin in range(0, len(pins)):
            if pins[pin].pin == BatteryMonitorPin1:
                BatteryLevel[0] = pins[pin].value
            elif pins[pin].pin == BatteryMonitorPin2:
                BatteryLevel[1] = pins[pin].value
            elif pins[pin].pin == BatteryMonitorPin3:
                BatteryLevel[2] = pins[pin].value
            elif pins[pin].pin == BatteryMonitorPin4:
                BatteryLevel[3] = pins[pin].value
    # Because we are dealing with the controller itself, we 
    # need to reference the controller directly.
    # That means creating the control program for each of 
    # the variations that may be used in the config. 
    if BatteryMonitorAttachment == "arduinoLeft":
        arduinoLeft.setBoardMega() 
        arduinoLeft.setAref("DEFAULT")
        arduinoLeft.addListener("publishPinArray","python","BattMonPublishedPins")
    elif BatteryMonitorAttachment == "arduinoRight":
        arduinoRight.setBoardMega() 
        arduinoRight.setAref("DEFAULT")
        arduinoRight.addListener("publishPinArray","python","BattMonPublishedPins")
    elif BatteryMonitorAttachment == "arduinoNano":
        arduinoNano.setBoardNano() 
        arduinoNano.setAref("DEFAULT")
        arduinoNano.addListener("publishPinArray","python","BattMonPublishedPins")
        arduinoNano.enablePin(BatteryMonitorPin1, 1)
        if EnableBatteryMonitor > 1:
            arduinoNano.enablePin(BatteryMonitorPin2, 1)
        if EnableBatteryMonitor > 2:
            arduinoNano.enablePin(BatteryMonitorPin3, 1)
        if EnableBatteryMonitor > 3:
            arduinoNano.enablePin(BatteryMonitorPin4, 1)
 
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

##############################################################
#                                                            #
# MPU6050 Inertial Measurment Unit (IMU)                     #
#                                                            #
##############################################################
# The first parameter is the service we want to attach it to, 
# normally either the RasPi or one of the Arduinos
# in our case it will be the Raspi4.
#
# The second parameter is the bus, This is normally 1 for the 
# RasPi or 0 for an Arduino.

# First lets make sure the I2C controller enabled
if not ((MPU6050AAttached == "raspi" and EnableRaspberryPi) or (MPU6050AAttached == "arduinoNano" and EnableArduinoNano) or (MPU6050AAttached == "arduinoLeft" and EnableArduinoLeft) or (MPU6050AAttached == "arduinoRight" and EnableArduinoRight)):
    EnableMPU6050A = False

if EnableMPU6050A == True:
    MPU6050A = Runtime.createAndStart("MPU6050A","Mpu6050")
    MPU6050A.attach(MPU6050AAttached, MPU6050APort, MPU6050AAddr)
    #MPU6050A.initialize()
    MPU6050A.dmpInitialize()
    #MPU6050A.refresh()
    #MPU6050A.getRaw() 
    #MPU6050A.startOrientationTracking()
    #MPU6050A.stopOrientationTracking()
    #python.subscribe('MPU6050A', 'publishOrientation', 'python', 'MPU6050Head')
    #publishOrientation(Orientation data) 

# First lets make sure the I2C controller enabled
if not ((MPU6050BAttached == "raspi" and EnableRaspberryPi) or (MPU6050BAttached == "arduinoNano" and EnableArduinoNano) or (MPU6050BAttached == "arduinoLeft" and EnableArduinoLeft) or (MPU6050BAttached == "arduinoRight" and EnableArduinoRight)):
    EnableMPU6050B = False

if EnableMPU6050B == True:
    MPU6050B = Runtime.createAndStart("MPU6050B","Mpu6050")
    MPU6050B.attach(MPU6050BAttached, MPU6050BPort, MPU6050BAddr)
    #MPU6050B.initialize()
    MPU6050B.dmpInitialize()
    #MPU6050B.refresh()
    #MPU6050B.getRaw() 
    #MPU6050B.startOrientationTracking()
    #MPU6050B.stopOrientationTracking()
    #python.subscribe('MPU6050B', 'publishOrientation', 'python', 'MPU6050Body')
    #publishOrientation(Orientation data) 
