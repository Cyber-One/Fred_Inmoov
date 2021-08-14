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
# 1_Servos_Head.py                                           #
# This file is to start all the servos used in the Robots    #
# Head other than the Neck servo.                            #
#                                                            #
##############################################################
print "Starting the various Head Servos Services"

# For more information on what each of the servos do, refer
# to the /1_Configuration/3_Servo_Head_Config.py file

##############################################################
# Load the configuration for the Servos_Head.
execfile(RuningFolder+'/1_Configuration/3_Servo_Head_Config.py')

# Test to make sure the configured controller is enabled.
if not ((JawAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (JawAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (JawAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (JawAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (JawAttachment == "arduinoNano" and EnableArduinoNano) 
    or (JawAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (JawAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (JawAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableJawServo = False

if EnableJawServo == True:
    print "--The Jaw"
    # The Servo service is designede to operate a number of
    # different types of servos via different controllers
    # while providing a common interface for your robot.
    # Before we can use a servo, we must first create the
    # servo object by using the Runtime service and the 
    # createAndStart function, passing in the Name we want to
    # call our new servo service as well as the type of 
    # service, in this case "Servo".
    # We then assign this new object to a variable.
    # In this example, we are assigning a Servo Service to 
    # the variable Jaw
    Jaw = Runtime.createAndStart("Jaw", "Servo")
    # Once we have a Servo service, we need to attach it to 
    # a controller on our system.  There can be more than one 
    # controller or even types of controllers within the 
    # system, so we need to tell the service where to find 
    # the controller and what pin to connect ther servo 
    # service to.  For that we use the attach method.
    # This method takes two parameters, the first is the 
    # service object.
    # The second parameter is the pin on the controller that 
    # the servo will be attached to.
    # Because we have a number of options for the controller 
    # service, and we want to make is easy to configure, we 
    # will set a config string with the service names and 
    # then select the service based on that name from a list 
    # of possible service we are likely to use.
    if JawAttachment == "Head":
        Jaw.attach(Head, JawPin)
    elif JawAttachment == "Back":
        Jaw.attach(Back, JawPin)
    elif JawAttachment == "RightArm":
        Jaw.attach(RightArm, JawPin)
    elif JawAttachment == "LeftArm":
        Jaw.attach(LeftArm, JawPin)
    elif JawAttachment == "arduinoLeft":
        Jaw.attach(arduinoLeft, JawPin)
    elif JawAttachment == "arduinoRight":
        Jaw.attach(arduinoRight, JawPin)
    elif JawAttachment == "arduinoNano":
        Jaw.attach(arduinoNano, JawPin)
    elif JawAttachment == "arduinoNano2":
        Jaw.attach(arduinoNano2, JawPin)
    # When you install your servo into your robot, you may 
    # find that the servo turns to far and has to potential 
    # of damaging your robot.  In this case you will want to 
    # limit how far the servo turns.   To do this we use the 
    # set Min/Max method.  This method while still working is 
    # being depreciated, it is suggested to use the map 
    # method instead.
    # Jaw.setMinMax(JawMinPos, JawMaxPos)
    Jaw.setMinMax(0, 100)
    # A lot of servos will have a 180 degree range of motion.
    # however there are some with more range and others with 
    # less range, the servo service cannot tell these types 
    # apart, the solution is to Map them :-)
    # If you have a 270 degree servo, the same PWM signal 
    # range for the 180 dgree servos will rotate 270 degree.
    # What we can do is Map the 0 - 180 to the 0 - 270 degrees
    # In this case, we would map the 0 - 270 as the input to 
    # the 0 - 180 on the output. Then when you adjust the 
    # output by 90 degrees the servo will turn 90 degrees.
    if JawMinPos < JawMaxPos:
        Jaw.map(0, 100, JawMinPos, JawMaxPos)
    else:
        Jaw.map(0, 100, JawMaxPos, JawMinPos)
    # On occasion you may need to reverse the direction of a 
    # servo. You may have an arm on each side of the robot, 
    # where 90 degree it pointing forward, but 0 degrees has 
    # one arm move up while the other moves down.  In this 
    # case you may want both servo to mover the arms down.
    # What you will want to do is Invert the direction of one 
    # of the servos so that both are down at 0 degrees.
    # Setting the setInvert to True will invert the servo.
    if JawMinPos < JawMaxPos:
        Jaw.setInverted(False)
    else:
        Jaw.setInverted(True)
    # The Rest position is a pre-programmed position for the 
    # servo to move to when you call the rest method.
    Jaw.setRest(10)
    # Without any speed control, when you change a servos 
    # position, the servo will try and rotate to the new 
    # position as fast as it can.  This can at times be 
    # undesirable, resulting in your whole robot shaking or 
    # worse falling over causing damage.  The speed at which 
    # the servo rotate can limited or controlled by sending a 
    # series of position updates between the current position 
    # and the target position.  The rate of rotation is set 
    # in degrees per second.  
    # A value of -1 disables speed control.
    # The setVelocity method used in Manticore has been
    # depreciated in Nixie, that is it still works, but the
    # version after Nixie it will be gone.
    # When I asked the lead developer about this change,
    # he pointed out, Velocity is a Vector, since most servos
    # are a rotation or a linera motion and we are not given
    # the 3 components of the vector, then speed in more
    # apropriate.  Lets face it, in your car when you want to
    # know how fast you are traveling, you check the
    # Speedometer, not the Velociometer
    if MRL == "Nixie":
        Jaw.setSpeed(JawVelocity)
    else:
        Jaw.setVelocity(JawVelocity) ## max velocity
    # The Servo service has a feature where it will disable a 
    # servos, saving power and potentially preventing the 
    # servo from burning out.  This feature can be disabled 
    # when disabling the servo would be bad.
    Jaw.setAutoDisable(True)
    # The rest method will send to servo to the pre-programmed 
    # position as set by the setRest method or if not set, to 
    # the default position of 90 degrees.
    Jaw.rest()

# Test to make sure the configured controller is enabled.
if not ((RightEyeXAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (RightEyeXAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (RightEyeXAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (RightEyeXAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (RightEyeXAttachment == "arduinoNano" and EnableArduinoNano) 
    or (RightEyeXAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (RightEyeXAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (RightEyeXAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightEyeX = False

if EnableRightEyeX == True:
    print "--Right Eye X axis"
    RightEyeLR = Runtime.createAndStart("RightEyeLR", "Servo")
    if RightEyeXAttachment == "Head":
        RightEyeLR.attach(Head, RightEyeXPin)
    elif RightEyeXAttachment == "Back":
        RightEyeLR.attach(Back, RightEyeXPin)
    elif RightEyeXAttachment == "RightArm":
        RightEyeLR.attach(RightArm, RightEyeXPin)
    elif RightEyeXAttachment == "LeftArm":
        RightEyeLR.attach(LeftArm, RightEyeXPin)
    elif RightEyeXAttachment == "arduinoLeft":
        RightEyeLR.attach(arduinoLeft, RightEyeXPin)
    elif RightEyeXAttachment == "arduinoRight":
        RightEyeLR.attach(arduinoRight, RightEyeXPin)
    elif RightEyeXAttachment == "arduinoNano":
        RightEyeLR.attach(arduinoNano, RightEyeXPin)
    elif RightEyeXAttachment == "arduinoNano2":
        RightEyeLR.attach(arduinoNano2, RightEyeXPin)
    #RightEyeLR.setMinMax(RightEyeXMinPos, RightEyeXMaxPos)
    RightEyeLR.setMinMax(0, 100)
    # In the prefious servo service, I used a seperate If
    # statment for the map and inverted methods, from now
    # on i will combine them in to a singel if statement.
    if RightEyeXMinPos < RightEyeXMaxPos:
        RightEyeLR.map(0, 100, RightEyeXMinPos, RightEyeXMaxPos)
        RightEyeLR.setInverted(False)
    else:
        RightEyeLR.map(0, 100, RightEyeXMaxPos, RightEyeXMinPos)
        RightEyeLR.setInverted(True)
    RightEyeLR.setRest(50)
    if MRL == "Nixie":
        RightEyeLR.setSpeed(RightEyeXVelocity)
    else:
        RightEyeLR.setVelocity(RightEyeXVelocity) ## max velocity
    RightEyeLR.setAutoDisable(True)
    RightEyeLR.rest()

# Test to make sure the configured controller is enabled.
if not ((RightEyeYAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (RightEyeYAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (RightEyeYAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (RightEyeYAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (RightEyeYAttachment == "arduinoNano" and EnableArduinoNano) 
    or (RightEyeYAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (RightEyeYAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (RightEyeYAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightEyeY = False

if EnableRightEyeY == True:
    print "--Right Eye Y axis"
    RightEyeUD = Runtime.createAndStart("RightEyeUD", "Servo")
    if RightEyeYAttachment == "Head":
        RightEyeUD.attach(Head, RightEyeYPin)
    elif RightEyeYAttachment == "Back":
        RightEyeUD.attach(Back, RightEyeYPin)
    elif RightEyeYAttachment == "RightArm":
        RightEyeUD.attach(RightArm, RightEyeYPin)
    elif RightEyeYAttachment == "LeftArm":
        RightEyeUD.attach(LeftArm, RightEyeYPin)
    elif RightEyeYAttachment == "arduinoLeft":
        RightEyeUD.attach(arduinoLeft, RightEyeYPin)
    elif RightEyeYAttachment == "arduinoRight":
        RightEyeUD.attach(arduinoRight, RightEyeYPin)
    elif RightEyeYAttachment == "arduinoNano":
        RightEyeUD.attach(arduinoNano, RightEyeYPin)
    elif RightEyeYAttachment == "arduinoNano2":
        RightEyeUD.attach(arduinoNano2, RightEyeYPin)
    #RightEyeUD.setMinMax(RightEyeYMinPos, RightEyeYMaxPos)
    RightEyeUD.setMinMax(0, 100)
    if RightEyeYMinPos < RightEyeYMaxPos:
        RightEyeUD.map(0, 100, RightEyeYMinPos, RightEyeYMaxPos)
        RightEyeUD.setInverted(False)
    else:
        RightEyeUD.map(0, 100, RightEyeYMaxPos, RightEyeYMinPos)
        RightEyeUD.setInverted(True)
    RightEyeUD.setRest(50)
    if MRL == "Nixie":
        RightEyeUD.setSpeed(RightEyeYVelocity)
    else:
        RightEyeUD.setVelocity(RightEyeYVelocity) ## max velocity
    RightEyeUD.setAutoDisable(True)
    RightEyeUD.rest()

# Test to make sure the configured controller is enabled.
if not ((LeftEyeXAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (LeftEyeXAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (LeftEyeXAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (LeftEyeXAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (LeftEyeXAttachment == "arduinoNano" and EnableArduinoNano) 
    or (LeftEyeXAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (LeftEyeXAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (LeftEyeXAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableLeftEyeX = False

if EnableLeftEyeX == True:
    print "--Left Eye X axis"
    LeftEyeLR = Runtime.createAndStart("LeftEyeLR", "Servo")
    if LeftEyeXAttachment == "Head":
        LeftEyeLR.attach(Head, LeftEyeXPin)
    elif LeftEyeXAttachment == "Back":
        LeftEyeLR.attach(Back, LeftEyeXPin)
    elif LeftEyeXAttachment == "RightArm":
        LeftEyeLR.attach(RightArm, LeftEyeXPin)
    elif LeftEyeXAttachment == "LeftArm":
        LeftEyeLR.attach(LeftArm, LeftEyeXPin)
    elif LeftEyeXAttachment == "arduinoLeft":
        LeftEyeLR.attach(arduinoLeft, LeftEyeXPin)
    elif LeftEyeXAttachment == "arduinoRight":
        LeftEyeLR.attach(arduinoRight, LeftEyeXPin)
    elif LeftEyeXAttachment == "arduinoNano":
        LeftEyeLR.attach(arduinoNano, LeftEyeXPin)
    elif LeftEyeXAttachment == "arduinoNano2":
        LeftEyeLR.attach(arduinoNano2, LeftEyeXPin)
    #LeftEyeLR.setMinMax(LeftEyeXMinPos, LeftEyeXMaxPos)
    LeftEyeLR.setMinMax(0, 100)
    if LeftEyeXMinPos < LeftEyeXMaxPos:
        LeftEyeLR.map(0, 100, LeftEyeXMinPos, LeftEyeXMaxPos)
        LeftEyeLR.setInverted(False)
    else:
        LeftEyeLR.map(0, 100, LeftEyeXMaxPos, LeftEyeXMinPos)
        LeftEyeLR.setInverted(True)
    LeftEyeLR.setRest(50)
    if MRL == "Nixie":
        LeftEyeLR.setSpeed(LeftEyeXVelocity)
    else:
        LeftEyeLR.setVelocity(LeftEyeXVelocity) ## max velocity
    LeftEyeLR.setAutoDisable(True)
    LeftEyeLR.rest()

# Test to make sure the configured controller is enabled.
if not ((LeftEyeYAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (LeftEyeYAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (LeftEyeYAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (LeftEyeYAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (LeftEyeYAttachment == "arduinoNano" and EnableArduinoNano) 
    or (LeftEyeYAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (LeftEyeYAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (LeftEyeYAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableLeftEyeY = False

if EnableLeftEyeY == True:
    print "--Left Eye Y axis"
    LeftEyeUD = Runtime.createAndStart("LeftEyeUD", "Servo")
    if LeftEyeYAttachment == "Head":
        LeftEyeUD.attach(Head, LeftEyeYPin)
    elif LeftEyeYAttachment == "Back":
        LeftEyeUD.attach(Back, LeftEyeYPin)
    elif LeftEyeYAttachment == "RightArm":
        LeftEyeUD.attach(RightArm, LeftEyeYPin)
    elif LeftEyeYAttachment == "LeftArm":
        LeftEyeUD.attach(LeftArm, LeftEyeYPin)
    elif LeftEyeYAttachment == "arduinoLeft":
        LeftEyeUD.attach(arduinoLeft, LeftEyeYPin)
    elif LeftEyeYAttachment == "arduinoRight":
        LeftEyeUD.attach(arduinoRight, LeftEyeYPin)
    elif LeftEyeYAttachment == "arduinoNano":
        LeftEyeUD.attach(arduinoNano, LeftEyeYPin)
    elif LeftEyeYAttachment == "arduinoNano2":
        LeftEyeUD.attach(arduinoNano2, LeftEyeYPin)
    #LeftEyeUD.setMinMax(LeftEyeYMinPos, LeftEyeYMaxPos)
    LeftEyeUD.setMinMax(0, 100)
    if LeftEyeYMinPos < LeftEyeYMaxPos:
        LeftEyeUD.map(0, 100, LeftEyeYMinPos, LeftEyeYMaxPos)
        LeftEyeUD.setInverted(False)
    else:
        LeftEyeUD.map(0, 100, LeftEyeYMaxPos, LeftEyeYMinPos)
        LeftEyeUD.setInverted(True)
    LeftEyeUD.setRest(50)
    if MRL == "Nixie":
        LeftEyeUD.setSpeed(LeftEyeYVelocity)
    else:
        LeftEyeUD.setVelocity(LeftEyeYVelocity) ## max velocity
    LeftEyeUD.setAutoDisable(True)
    LeftEyeUD.rest()

# Test to make sure the configured controller is enabled.
if not ((UpperREyeLidAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (UpperREyeLidAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (UpperREyeLidAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (UpperREyeLidAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (UpperREyeLidAttachment == "arduinoNano" and EnableArduinoNano) 
    or (UpperREyeLidAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (UpperREyeLidAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (UpperREyeLidAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightUpperEyeLid = False

if EnableRightUpperEyeLid == True:
    print "--Upper Right Eyelid"
    UpperEyeLidR = Runtime.createAndStart("UpperEyeLidR", "Servo")
    if UpperREyeLidAttachment == "Head":
        UpperEyeLidR.attach(Head, UpperREyeLidPin)
    elif UpperREyeLidAttachment == "Back":
        UpperEyeLidR.attach(Back, UpperREyeLidPin)
    elif UpperREyeLidAttachment == "RightArm":
        UpperEyeLidR.attach(RightArm, UpperREyeLidPin)
    elif UpperREyeLidAttachment == "LeftArm":
        UpperEyeLidR.attach(LeftArm, UpperREyeLidPin)
    elif UpperREyeLidAttachment == "arduinoLeft":
        UpperEyeLidR.attach(arduinoLeft, UpperREyeLidPin)
    elif UpperREyeLidAttachment == "arduinoRight":
        UpperEyeLidR.attach(arduinoRight, UpperREyeLidPin)
    elif UpperREyeLidAttachment == "arduinoNano":
        UpperEyeLidR.attach(arduinoNano, UpperREyeLidPin)
    elif UpperREyeLidAttachment == "arduinoNano2":
        UpperEyeLidR.attach(arduinoNano2, UpperREyeLidPin)
    #UpperEyeLidR.setMinMax(UpperREyeLidMinPos, UpperREyeLidMaxPos)
    UpperEyeLidR.setMinMax(0, 100)
    if UpperREyeLidMinPos < UpperREyeLidMaxPos:
        UpperEyeLidR.map(0, 100, UpperREyeLidMinPos, UpperREyeLidMaxPos)
        UpperEyeLidR.setInverted(False)
    else:
        UpperEyeLidR.map(0, 100, UpperREyeLidMaxPos, UpperREyeLidMinPos)
        UpperEyeLidR.setInverted(True)
    UpperEyeLidR.setRest(50)
    if MRL == "Nixie":
        UpperEyeLidR.setSpeed(UpperREyeLidVelocity)
    else:
        UpperEyeLidR.setVelocity(UpperREyeLidVelocity) ## max velocity
    UpperEyeLidR.setAutoDisable(False)
    UpperEyeLidR.rest()

# Test to make sure the configured controller is enabled.
if not ((LowerREyeLidAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (LowerREyeLidAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (LowerREyeLidAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (LowerREyeLidAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (LowerREyeLidAttachment == "arduinoNano" and EnableArduinoNano) 
    or (LowerREyeLidAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (LowerREyeLidAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (LowerREyeLidAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRightLowerEyeLid = False

if EnableRightLowerEyeLid == True:
    print "--Lower Right Eyelid"
    LowerEyeLidR = Runtime.createAndStart("LowerEyeLidR", "Servo")
    if LowerREyeLidAttachment == "Head":
        LowerEyeLidR.attach(Head, LowerREyeLidPin)
    elif LowerREyeLidAttachment == "Back":
        LowerEyeLidR.attach(Back, LowerREyeLidPin)
    elif LowerREyeLidAttachment == "RightArm":
        LowerEyeLidR.attach(RightArm, LowerREyeLidPin)
    elif LowerREyeLidAttachment == "LeftArm":
        LowerEyeLidR.attach(LeftArm, LowerREyeLidPin)
    elif LowerREyeLidAttachment == "arduinoLeft":
        LowerEyeLidR.attach(arduinoLeft, LowerREyeLidPin)
    elif LowerREyeLidAttachment == "arduinoRight":
        LowerEyeLidR.attach(arduinoRight, LowerREyeLidPin)
    elif LowerREyeLidAttachment == "arduinoNano":
        LowerEyeLidR.attach(arduinoNano, LowerREyeLidPin)
    elif LowerREyeLidAttachment == "arduinoNano2":
        LowerEyeLidR.attach(arduinoNano2, LowerREyeLidPin)
    #LowerEyeLidR.setMinMax(LowerREyeLidMinPos, LowerREyeLidMaxPos)
    LowerEyeLidR.setMinMax(0, 100)
    if LowerREyeLidMinPos < LowerREyeLidMaxPos:
        LowerEyeLidR.map(0, 100, LowerREyeLidMinPos, LowerREyeLidMaxPos)
        LowerEyeLidR.setInverted(False)
    else:
        LowerEyeLidR.map(0, 100, LowerREyeLidMaxPos, LowerREyeLidMinPos)
        LowerEyeLidR.setInverted(True)
    LowerEyeLidR.setRest(50)
    if MRL == "Nixie":
        LowerEyeLidR.setSpeed(LowerREyeLidVelocity)
    else:
        LowerEyeLidR.setVelocity(LowerREyeLidVelocity) ## max velocity
    LowerEyeLidR.setAutoDisable(False)
    LowerEyeLidR.rest()

# Test to make sure the configured controller is enabled.
if not ((UpperLEyeLidAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (UpperLEyeLidAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (UpperLEyeLidAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (UpperLEyeLidAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (UpperLEyeLidAttachment == "arduinoNano" and EnableArduinoNano) 
    or (UpperLEyeLidAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (UpperLEyeLidAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (UpperLEyeLidAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableLeftUpperEyeLid = False

if EnableLeftUpperEyeLid == True:
    print "--Upper Left Eyelid"
    UpperEyeLidL = Runtime.createAndStart("UpperEyeLidL", "Servo")
    if UpperLEyeLidAttachment == "Head":
        UpperEyeLidL.attach(Head, UpperLEyeLidPin)
    elif UpperLEyeLidAttachment == "Back":
        UpperEyeLidL.attach(Back, UpperLEyeLidPin)
    elif UpperLEyeLidAttachment == "RightArm":
        UpperEyeLidL.attach(RightArm, UpperLEyeLidPin)
    elif UpperLEyeLidAttachment == "LeftArm":
        UpperEyeLidL.attach(LeftArm, UpperLEyeLidPin)
    elif UpperLEyeLidAttachment == "arduinoLeft":
        UpperEyeLidL.attach(arduinoLeft, UpperLEyeLidPin)
    elif UpperLEyeLidAttachment == "arduinoRight":
        UpperEyeLidL.attach(arduinoRight, UpperLEyeLidPin)
    elif UpperLEyeLidAttachment == "arduinoNano":
        UpperEyeLidL.attach(arduinoNano, UpperLEyeLidPin)
    elif UpperLEyeLidAttachment == "arduinoNano2":
        UpperEyeLidL.attach(arduinoNano2, UpperLEyeLidPin)
    #UpperEyeLidL.setMinMax(UpperLEyeLidMinPos, UpperLEyeLidMaxPos)
    UpperEyeLidL.setMinMax(0, 100)
    if UpperLEyeLidMinPos < UpperLEyeLidMaxPos:
        UpperEyeLidL.map(0, 100, UpperLEyeLidMinPos, UpperLEyeLidMaxPos)
        UpperEyeLidL.setInverted(False)
    else:
        UpperEyeLidL.map(0, 100, UpperLEyeLidMaxPos, UpperLEyeLidMinPos)
        UpperEyeLidL.setInverted(True)
    UpperEyeLidL.setRest(50)
    if MRL == "Nixie":
        UpperEyeLidL.setSpeed(UpperLEyeLidVelocity)
    else:
        UpperEyeLidL.setVelocity(UpperLEyeLidVelocity) ## max velocity
    UpperEyeLidL.setAutoDisable(False)
    UpperEyeLidL.rest()

# Test to make sure the configured controller is enabled.
if not ((LowerLEyeLidAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (LowerLEyeLidAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (LowerLEyeLidAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (LowerLEyeLidAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (LowerLEyeLidAttachment == "arduinoNano" and EnableArduinoNano) 
    or (LowerLEyeLidAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (LowerLEyeLidAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (LowerLEyeLidAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableLeftLowerEyeLid = False

if EnableLeftLowerEyeLid == True:
    print "--Lower Left Eyelid"
    LowerEyeLidL = Runtime.createAndStart("LowerEyeLidL", "Servo")
    if LowerLEyeLidAttachment == "Head":
        LowerEyeLidL.attach(Head, LowerLEyeLidPin)
    elif LowerLEyeLidAttachment == "Back":
        LowerEyeLidL.attach(Back, LowerLEyeLidPin)
    elif LowerLEyeLidAttachment == "RightArm":
        LowerEyeLidL.attach(RightArm, LowerLEyeLidPin)
    elif LowerLEyeLidAttachment == "LeftArm":
        LowerEyeLidL.attach(LeftArm, LowerLEyeLidPin)
    elif LowerLEyeLidAttachment == "arduinoLeft":
        LowerEyeLidL.attach(arduinoLeft, LowerLEyeLidPin)
    elif LowerLEyeLidAttachment == "arduinoRight":
        LowerEyeLidL.attach(arduinoRight, LowerLEyeLidPin)
    elif LowerLEyeLidAttachment == "arduinoNano":
        LowerEyeLidL.attach(arduinoNano, LowerLEyeLidPin)
    elif LowerLEyeLidAttachment == "arduinoNano2":
        LowerEyeLidL.attach(arduinoNano2, LowerLEyeLidPin)
    #LowerEyeLidL.setMinMax(LowerLEyeLidMinPos, LowerLEyeLidMaxPos)
    LowerEyeLidL.setMinMax(0, 100)
    if LowerLEyeLidMinPos < LowerLEyeLidMaxPos:
        LowerEyeLidL.map(0, 100, LowerLEyeLidMinPos, LowerLEyeLidMaxPos)
        LowerEyeLidL.setInverted(False)
    else:
        LowerEyeLidL.map(0, 100, LowerLEyeLidMaxPos, LowerLEyeLidMinPos)
        LowerEyeLidL.setInverted(True)
    LowerEyeLidL.setRest(50)
    if MRL == "Nixie":
        LowerEyeLidL.setSpeed(LowerLEyeLidVelocity)
    else:
        LowerEyeLidL.setVelocity(LowerLEyeLidVelocity) ## max velocity
    LowerEyeLidL.setAutoDisable(False)
    LowerEyeLidL.rest()

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

# Test to make sure the configured controller is enabled.
if not ((LatJawAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (LatJawAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (LatJawAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (LatJawAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (LatJawAttachment == "arduinoNano" and EnableArduinoNano) 
    or (LatJawAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (LatJawAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (LatJawAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableLatJaw = False
if EnableLatJaw == True:
    print "--Lower Left Eyelid"
    LatJaw = Runtime.createAndStart("LatJaw", "Servo")
    if LatJawAttachment == "Head":
        LatJaw.attach(Head, LatJawPin)
    elif LatJawAttachment == "Back":
        LatJaw.attach(Back, LatJawPin)
    elif LatJawAttachment == "RightArm":
        LatJaw.attach(RightArm, LatJawPin)
    elif LatJawAttachment == "LeftArm":
        LatJaw.attach(LeftArm, LatJawPin)
    elif LatJawAttachment == "arduinoLeft":
        LatJaw.attach(arduinoLeft, LatJawPin)
    elif LatJawAttachment == "arduinoRight":
        LatJaw.attach(arduinoRight, LatJawPin)
    elif LatJawAttachment == "arduinoNano":
        LatJaw.attach(arduinoNano, LatJawPin)
    elif LatJawAttachment == "arduinoNano2":
        LatJaw.attach(arduinoNano2, LatJawPin)
    LatJaw.setMinMax(0, 100)
    if LatJawMinPos < LatJawMaxPos:
        LatJaw.map(0, 100, LatJawMinPos, LatJawMaxPos)
        LatJaw.setInverted(False)
    else:
        LatJaw.map(0, 100, LatJawMaxPos, LatJawMinPos)
        LatJaw.setInverted(True)
    LatJaw.setRest(50)
    if MRL == "Nixie":
        LatJaw.setSpeed(LatJawVelocity)
    else:
        LatJaw.setVelocity(LatJawVelocity) ## max velocity
    LatJaw.setAutoDisable(False)
    LatJaw.rest()

## The inner right eyebrow.
## This will allow the eyebrow to move up and down.

# Test to make sure the configured controller is enabled.
if not ((RBrowInAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (RBrowInAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (RBrowInAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (RBrowInAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (RBrowInAttachment == "arduinoNano" and EnableArduinoNano) 
    or (RBrowInAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (RBrowInAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (RBrowInAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRBrowIn = False
if EnableRBrowIn == True:
    print "--Lower Left Eyelid"
    RBrowIn = Runtime.createAndStart("RBrowIn", "Servo")
    if RBrowInAttachment == "Head":
        RBrowIn.attach(Head, RBrowInPin)
    elif RBrowInAttachment == "Back":
        RBrowIn.attach(Back, RBrowInPin)
    elif RBrowInAttachment == "RightArm":
        RBrowIn.attach(RightArm, RBrowInPin)
    elif RBrowInAttachment == "LeftArm":
        RBrowIn.attach(LeftArm, RBrowInPin)
    elif RBrowInAttachment == "arduinoLeft":
        RBrowIn.attach(arduinoLeft, RBrowInPin)
    elif RBrowInAttachment == "arduinoRight":
        RBrowIn.attach(arduinoRight, RBrowInPin)
    elif RBrowInAttachment == "arduinoNano":
        RBrowIn.attach(arduinoNano, RBrowInPin)
    elif RBrowInAttachment == "arduinoNano2":
        RBrowIn.attach(arduinoNano2, RBrowInPin)
    RBrowIn.setMinMax(0, 100)
    if RBrowInMinPos < RBrowInMaxPos:
        RBrowIn.map(0, 100, RBrowInMinPos, RBrowInMaxPos)
        RBrowIn.setInverted(False)
    else:
        RBrowIn.map(0, 100, RBrowInMaxPos, RBrowInMinPos)
        RBrowIn.setInverted(True)
    RBrowIn.setRest(50)
    if MRL == "Nixie":
        RBrowIn.setSpeed(RBrowInVelocity)
    else:
        RBrowIn.setVelocity(RBrowInVelocity) ## max velocity
    RBrowIn.setAutoDisable(False)
    RBrowIn.rest()

## The outter right eyebrow.
## This will allow the eyebrow to move up and down.

# Test to make sure the configured controller is enabled.
if not ((RBrowOutAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (RBrowOutAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (RBrowOutAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (RBrowOutAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (RBrowOutAttachment == "arduinoNano" and EnableArduinoNano) 
    or (RBrowOutAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (RBrowOutAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (RBrowOutAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableRBrowOut = False
if EnableRBrowOut == True:
    print "--Lower Left Eyelid"
    RBrowOut = Runtime.createAndStart("RBrowOut", "Servo")
    if RBrowOutAttachment == "Head":
        RBrowOut.attach(Head, RBrowOutPin)
    elif RBrowOutAttachment == "Back":
        RBrowOut.attach(Back, RBrowOutPin)
    elif RBrowOutAttachment == "RightArm":
        RBrowOut.attach(RightArm, RBrowOutPin)
    elif RBrowOutAttachment == "LeftArm":
        RBrowOut.attach(LeftArm, RBrowOutPin)
    elif RBrowOutAttachment == "arduinoLeft":
        RBrowOut.attach(arduinoLeft, RBrowOutPin)
    elif RBrowOutAttachment == "arduinoRight":
        RBrowOut.attach(arduinoRight, RBrowOutPin)
    elif RBrowOutAttachment == "arduinoNano":
        RBrowOut.attach(arduinoNano, RBrowOutPin)
    elif RBrowOutAttachment == "arduinoNano2":
        RBrowOut.attach(arduinoNano2, RBrowOutPin)
    RBrowOut.setMinMax(0, 100)
    if RBrowOutMinPos < RBrowOutMaxPos:
        RBrowOut.map(0, 100, RBrowOutMinPos, RBrowOutMaxPos)
        RBrowOut.setInverted(False)
    else:
        RBrowOut.map(0, 100, RBrowOutMaxPos, RBrowOutMinPos)
        RBrowOut.setInverted(True)
    RBrowOut.setRest(50)
    if MRL == "Nixie":
        RBrowOut.setSpeed(RBrowOutVelocity)
    else:
        RBrowOut.setVelocity(RBrowOutVelocity) ## max velocity
    RBrowOut.setAutoDisable(False)
    RBrowOut.rest()

## The inner left eyebrow.
## This will allow the eyebrow to move up and down.

# Test to make sure the configured controller is enabled.
if not ((LBrowInAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (LBrowInAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (LBrowInAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (LBrowInAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (LBrowInAttachment == "arduinoNano" and EnableArduinoNano) 
    or (LBrowInAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (LBrowInAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (LBrowInAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableLBrowIn = False
if EnableLBrowIn == True:
    print "--Lower Left Eyelid"
    LBrowIn = Runtime.createAndStart("LBrowIn", "Servo")
    if LBrowInAttachment == "Head":
        LBrowIn.attach(Head, LBrowInPin)
    elif LBrowInAttachment == "Back":
        LBrowIn.attach(Back, LBrowInPin)
    elif LBrowInAttachment == "RightArm":
        LBrowIn.attach(RightArm, LBrowInPin)
    elif LBrowInAttachment == "LeftArm":
        LBrowIn.attach(LeftArm, LBrowInPin)
    elif LBrowInAttachment == "arduinoLeft":
        LBrowIn.attach(arduinoLeft, LBrowInPin)
    elif LBrowInAttachment == "arduinoRight":
        LBrowIn.attach(arduinoRight, LBrowInPin)
    elif LBrowInAttachment == "arduinoNano":
        LBrowIn.attach(arduinoNano, LBrowInPin)
    elif LBrowInAttachment == "arduinoNano2":
        LBrowIn.attach(arduinoNano2, LBrowInPin)
    LBrowIn.setMinMax(0, 100)
    if LBrowInMinPos < LBrowInMaxPos:
        LBrowIn.map(0, 100, LBrowInMinPos, LBrowInMaxPos)
        LBrowIn.setInverted(False)
    else:
        LBrowIn.map(0, 100, LBrowInMaxPos, LBrowInMinPos)
        LBrowIn.setInverted(True)
    LBrowIn.setRest(50)
    if MRL == "Nixie":
        LBrowIn.setSpeed(LBrowInVelocity)
    else:
        LBrowIn.setVelocity(LBrowInVelocity) ## max velocity
    LBrowIn.setAutoDisable(False)
    LBrowIn.rest()

## The outter left eyebrow.
## This will allow the eyebrow to move up and down.

# Test to make sure the configured controller is enabled.
if not ((LBrowOutAttachment == "Head" and EnableAdafruit16CServoDriverHead) 
    or (LBrowOutAttachment == "Back" and EnableAdafruit16CServoDriverBack) 
    or (LBrowOutAttachment == "RightArm" and EnableAdafruit16CServoDriverRightArm)
    or (LBrowOutAttachment == "LeftArm" and EnableAdafruit16CServoDriverLeftArm)
    or (LBrowOutAttachment == "arduinoNano" and EnableArduinoNano) 
    or (LBrowOutAttachment == "arduinoNano2" and EnableArduinoNano2) 
    or (LBrowOutAttachment == "arduinoLeft" and EnableArduinoLeft) 
    or (LBrowOutAttachment == "arduinoRight" and EnableArduinoRight)):
    EnableLBrowOut = False
if EnableLBrowOut == True:
    print "--Lower Left Eyelid"
    LBrowOut = Runtime.createAndStart("LBrowOut", "Servo")
    if LBrowOutAttachment == "Head":
        LBrowOut.attach(Head, LBrowOutPin)
    elif LBrowOutAttachment == "Back":
        LBrowOut.attach(Back, LBrowOutPin)
    elif LBrowOutAttachment == "RightArm":
        LBrowOut.attach(RightArm, LBrowOutPin)
    elif LBrowOutAttachment == "LeftArm":
        LBrowOut.attach(LeftArm, LBrowOutPin)
    elif LBrowOutAttachment == "arduinoLeft":
        LBrowOut.attach(arduinoLeft, LBrowOutPin)
    elif LBrowOutAttachment == "arduinoRight":
        LBrowOut.attach(arduinoRight, LBrowOutPin)
    elif LBrowOutAttachment == "arduinoNano":
        LBrowOut.attach(arduinoNano, LBrowOutPin)
    elif LBrowOutAttachment == "arduinoNano2":
        LBrowOut.attach(arduinoNano2, LBrowOutPin)
    LBrowOut.setMinMax(0, 100)
    if LBrowOutMinPos < LBrowOutMaxPos:
        LBrowOut.map(0, 100, LBrowOutMinPos, LBrowOutMaxPos)
        LBrowOut.setInverted(False)
    else:
        LBrowOut.map(0, 100, LBrowOutMaxPos, LBrowOutMinPos)
        LBrowOut.setInverted(True)
    LBrowOut.setRest(50)
    if MRL == "Nixie":
        LBrowOut.setSpeed(LBrowOutVelocity)
    else:
        LBrowOut.setVelocity(LBrowOutVelocity) ## max velocity
    LBrowOut.setAutoDisable(False)
    LBrowOut.rest()
