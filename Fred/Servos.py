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
# Servos.py                                                  #
# This file is to start all the servos used in the Robot     #
#                                                            #
##############################################################
print "Starting the various Servos Services"

##############################################################
#                                                            #
# Servo Head Group                                           #
#                                                            #
##############################################################

print "-Head Group"

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
    if JawAttachment == "Back":
        Jaw.attach(Back, JawPin)
    if JawAttachment == "RightArm":
        Jaw.attach(RightArm, JawPin)
    if JawAttachment == "LeftArm":
        Jaw.attach(LeftArm, JawPin)
    if JawAttachment == "arduinoLeft":
        Jaw.attach(arduinoLeft, JawPin)
    if JawAttachment == "arduinoRight":
        Jaw.attach(arduinoRight, JawPin)
    if JawAttachment == "arduinoNano":
        Jaw.attach(arduinoNano, JawPin)
    # When you install your servo into your robot, you may 
    # find that the servo turns to far and has to potential 
    # of damaging your robot.  In this case you will want to 
    # limit how far the servo turns.   To do this we use the 
    # set Min/Max method.  This method while still working is 
    # being depreciated, it is suggested to use the map 
    # method instead.
    Jaw.setMinMax(JawMinPos, JawMaxPos)
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
    #Jaw.map(0,180,1,180)
    # The Rest position is a pre-programmed position for the 
    # servo to move to when you call the rest method.
    Jaw.setRest(JawRestPos)
    # On occasion you may need to reverse the direction of a 
    # servo. You may have an arm on each side of the robot, 
    # where 90 degree it pointing forward, but 0 degrees has 
    # one arm move up while the other moves down.  In this 
    # case you may want both servo to mover the arms down.
    # What you will want to do is Invert the direction of one 
    # of the servos so that both are down at 0 degrees.
    # Setting the setInvert to True will invert the servo.
    Jaw.setInverted(False)
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
    Jaw.setSpeed(-1)
    # The Servo service has a feature where it will disable a 
    # servos, saving power and potentially preventing the 
    # servo from burning out.  This feature can be disabled 
    # when disabling the servo would be bad.
    Jaw.setAutoDisable(True)
    # The rest method will send to servo to the pre-programmed 
    # position as set by the setRest method or if not set, to 
    # the default position of 90 degrees.
    #Jaw.rest()

if EnableRightEyeX == True:
    print "--Right Eye X axis"
    RightEyeLR = Runtime.createAndStart("RightEyeLR", "Servo")
    if RightEyeXAttachment == "Head":
        RightEyeLR.attach(Head, RightEyeXPin)
    if RightEyeXAttachment == "Back":
        RightEyeLR.attach(Back, RightEyeXPin)
    if RightEyeXAttachment == "RightArm":
        RightEyeLR.attach(RightArm, RightEyeXPin)
    if RightEyeXAttachment == "LeftArm":
        RightEyeLR.attach(LeftArm, RightEyeXPin)
    if RightEyeXAttachment == "arduinoLeft":
        RightEyeLR.attach(arduinoLeft, RightEyeXPin)
    if RightEyeXAttachment == "arduinoRight":
        RightEyeLR.attach(arduinoRight, RightEyeXPin)
    if RightEyeXAttachment == "arduinoNano":
        RightEyeLR.attach(arduinoNano, RightEyeXPin)
    RightEyeLR.setMinMax(RightEyeXMinPos, RightEyeXMaxPos)
    #RightEyeLR.map(0,180,1,180)
    RightEyeLR.setRest(RightEyeXRestPos)
    RightEyeLR.setInverted(False)
    RightEyeLR.setSpeed(60)
    RightEyeLR.setAutoDisable(True)
    RightEyeLR.rest()

if EnableRightEyeY == True:
    print "--Right Eye Y axis"
    RightEyeUD = Runtime.createAndStart("RightEyeUD", "Servo")
    if RightEyeYAttachment == "Head":
        RightEyeUD.attach(Head, RightEyeYPin)
    if RightEyeYAttachment == "Back":
        RightEyeUD.attach(Back, RightEyeYPin)
    if RightEyeYAttachment == "RightArm":
        RightEyeUD.attach(RightArm, RightEyeYPin)
    if RightEyeYAttachment == "LeftArm":
        RightEyeUD.attach(LeftArm, RightEyeYPin)
    if RightEyeYAttachment == "arduinoLeft":
        RightEyeUD.attach(arduinoLeft, RightEyeYPin)
    if RightEyeYAttachment == "arduinoRight":
        RightEyeUD.attach(arduinoRight, RightEyeYPin)
    if RightEyeYAttachment == "arduinoNano":
        RightEyeUD.attach(arduinoNano, RightEyeYPin)
    RightEyeUD.setMinMax(RightEyeYMinPos, RightEyeYMaxPos)
    #RightEyeUD.map(0,180,1,180)
    RightEyeUD.setRest(RightEyeYRestPos)
    RightEyeUD.setInverted(False)
    RightEyeUD.setSpeed(120)
    RightEyeUD.setAutoDisable(True)
    RightEyeUD.rest()

if EnableLeftEyeX == True:
    print "--Left Eye X axis"
    LeftEyeLR = Runtime.createAndStart("LefttEyeLR", "Servo")
    if LeftEyeXAttachment == "Head":
        LeftEyeLR.attach(Head, LeftEyeXPin)
    if LeftEyeXAttachment == "Back":
        LeftEyeLR.attach(Back, LeftEyeXPin)
    if LeftEyeXAttachment == "RightArm":
        LeftEyeLR.attach(RightArm, LeftEyeXPin)
    if LeftEyeXAttachment == "LeftArm":
        LeftEyeLR.attach(LeftArm, LeftEyeXPin)
    if LeftEyeXAttachment == "arduinoLeft":
        LeftEyeLR.attach(arduinoLeft, LeftEyeXPin)
    if LeftEyeXAttachment == "arduinoRight":
        LeftEyeLR.attach(arduinoRight, LeftEyeXPin)
    if LeftEyeXAttachment == "arduinoNano":
        LeftEyeLR.attach(arduinoNano, LeftEyeXPin)
    LeftEyeLR.setMinMax(LeftEyeXMinPos, LeftEyeXMaxPos)
    #LeftEyeLR.map(0,180,1,180)
    LeftEyeLR.setRest(LeftEyeXRestPos)
    LeftEyeLR.setInverted(False)
    LeftEyeLR.setSpeed(120)
    LeftEyeLR.setAutoDisable(True)
    LeftEyeLR.rest()

if EnableLeftEyeY == True:
    print "--Left Eye Y axis"
    LeftEyeUD = Runtime.createAndStart("LeftEyeUD", "Servo")
    if LeftEyeYAttachment == "Head":
        LeftEyeUD.attach(Head, LeftEyeYPin)
    if LeftEyeYAttachment == "Back":
        LeftEyeUD.attach(Back, LeftEyeYPin)
    if LeftEyeYAttachment == "RightArm":
        LeftEyeUD.attach(RightArm, LeftEyeYPin)
    if LeftEyeYAttachment == "LeftArm":
        LeftEyeUD.attach(LeftArm, LeftEyeYPin)
    if LeftEyeYAttachment == "arduinoLeft":
        LeftEyeUD.attach(arduinoLeft, LeftEyeYPin)
    if LeftEyeYAttachment == "arduinoRight":
        LeftEyeUD.attach(arduinoRight, LeftEyeYPin)
    if LeftEyeYAttachment == "arduinoNano":
        LeftEyeUD.attach(arduinoNano, LeftEyeYPin)
    LeftEyeUD.setMinMax(LeftEyeYMinPos, LeftEyeYMaxPos)
    #LeftEyeUD.map(0,180,1,180)
    LeftEyeUD.setRest(LeftEyeYRestPos)
    LeftEyeUD.setInverted(False)
    LeftEyeUD.setSpeed(60)
    LeftEyeUD.setAutoDisable(True)
    LeftEyeUD.rest()

if EnableRightUpperEyeLid == True:
    print "--Upper Right Eyelid"
    UpperEyeLidR = Runtime.createAndStart("UpperEyeLidR", "Servo")
    if UpperREyeLidAttachment == "Head":
        UpperEyeLidR.attach(Head, UpperREyeLidPin)
    if UpperREyeLidAttachment == "Back":
        UpperEyeLidR.attach(Back, UpperREyeLidPin)
    if UpperREyeLidAttachment == "RightArm":
        UpperEyeLidR.attach(RightArm, UpperREyeLidPin)
    if UpperREyeLidAttachment == "LeftArm":
        UpperEyeLidR.attach(LeftArm, UpperREyeLidPin)
    if UpperREyeLidAttachment == "arduinoLeft":
        UpperEyeLidR.attach(arduinoLeft, UpperREyeLidPin)
    if UpperREyeLidAttachment == "arduinoRight":
        UpperEyeLidR.attach(arduinoRight, UpperREyeLidPin)
    if UpperREyeLidAttachment == "arduinoNano":
        UpperEyeLidR.attach(arduinoNano, UpperREyeLidPin)
    UpperEyeLidR.setMinMax(UpperREyeLidMinPos, UpperREyeLidMaxPos)
    #UpperEyeLidR.map(0,180,45,180)
    UpperEyeLidR.setRest(UpperREyeLidRestPos)
    UpperEyeLidR.setInverted(False)
    UpperEyeLidR.setSpeed(-1)
    UpperEyeLidR.setAutoDisable(False)
    # UpperEyeLidR.rest()

if EnableRightLowerEyeLid == True:
    print "--Lower Right Eyelid"
    LowerEyeLidR = Runtime.createAndStart("LowerEyeLidR", "Servo")
    if LowerREyeLidAttachment == "Head":
        LowerEyeLidR.attach(Head, LowerREyeLidPin)
    if LowerREyeLidAttachment == "Back":
        LowerEyeLidR.attach(Back, LowerREyeLidPin)
    if LowerREyeLidAttachment == "RightArm":
        LowerEyeLidR.attach(RightArm, LowerREyeLidPin)
    if LowerREyeLidAttachment == "LeftArm":
        LowerEyeLidR.attach(LeftArm, LowerREyeLidPin)
    if LowerREyeLidAttachment == "arduinoLeft":
        LowerEyeLidR.attach(arduinoLeft, LowerREyeLidPin)
    if LowerREyeLidAttachment == "arduinoRight":
        LowerEyeLidR.attach(arduinoRight, LowerREyeLidPin)
    if LowerREyeLidAttachment == "arduinoNano":
        LowerEyeLidR.attach(arduinoNano, LowerREyeLidPin)
    LowerEyeLidR.setMinMax(LowerREyeLidMinPos, LowerREyeLidMaxPos)
    #LowerEyeLidR.map(0,180,0,120)
    LowerEyeLidR.setRest(LowerREyeLidRestPos)
    LowerEyeLidR.setInverted(False)
    LowerEyeLidR.setSpeed(-1)
    LowerEyeLidR.setAutoDisable(False)
    # LowerEyeLidR.rest()

if EnableLeftUpperEyeLid == True:
    print "--Upper Left Eyelid"
    UpperEyeLidL = Runtime.createAndStart("UpperEyeLidL", "Servo")
    if UpperREyeLidAttachment == "Head":
        UpperEyeLidL.attach(Head, UpperLEyeLidPin)
    if UpperREyeLidAttachment == "Back":
        UpperEyeLidL.attach(Back, UpperLEyeLidPin)
    if UpperREyeLidAttachment == "RightArm":
        UpperEyeLidL.attach(RightArm, UpperLEyeLidPin)
    if UpperREyeLidAttachment == "LeftArm":
        UpperEyeLidL.attach(LeftArm, UpperLEyeLidPin)
    if UpperREyeLidAttachment == "arduinoLeft":
        UpperEyeLidL.attach(arduinoLeft, UpperLEyeLidPin)
    if UpperREyeLidAttachment == "arduinoRight":
        UpperEyeLidL.attach(arduinoRight, UpperLEyeLidPin)
    if UpperREyeLidAttachment == "arduinoNano":
        UpperEyeLidL.attach(arduinoNano, UpperLEyeLidPin)
    UpperEyeLidL.setMinMax(UpperLEyeLidMinPos, UpperLEyeLidMaxPos)
    #UpperEyeLidL.map(0,180,45,180)
    UpperEyeLidL.setRest(UpperLEyeLidRestPos)
    UpperEyeLidL.setInverted(False)
    UpperEyeLidL.setSpeed(-1)
    UpperEyeLidL.setAutoDisable(False)
    # UpperEyeLidL.rest()

if EnableLeftLowerEyeLid == True:
    print "--Lower Left Eyelid"
    LowerEyeLidL = Runtime.createAndStart("LowerEyeLidL", "Servo")
    if LowerREyeLidAttachment == "Head":
        LowerEyeLidL.attach(Head, LowerLEyeLidPin)
    if LowerREyeLidAttachment == "Back":
        LowerEyeLidL.attach(Back, LowerLEyeLidPin)
    if LowerREyeLidAttachment == "RightArm":
        LowerEyeLidL.attach(RightArm, LowerLEyeLidPin)
    if LowerREyeLidAttachment == "LeftArm":
        LowerEyeLidL.attach(LeftArm, LowerLEyeLidPin)
    if LowerREyeLidAttachment == "arduinoLeft":
        LowerEyeLidL.attach(arduinoLeft, LowerLEyeLidPin)
    if LowerREyeLidAttachment == "arduinoRight":
        LowerEyeLidL.attach(arduinoRight, LowerLEyeLidPin)
    if LowerREyeLidAttachment == "arduinoNano":
        LowerEyeLidL.attach(arduinoNano, LowerLEyeLidPin)
    LowerEyeLidL.setMinMax(LowerLEyeLidMinPos, LowerLEyeLidMaxPos)
    #LowerEyeLidL.map(0,180,0,120)
    LowerEyeLidL.setRest(LowerLEyeLidRestPos)
    LowerEyeLidL.setInverted(False)
    LowerEyeLidL.setSpeed(-1)
    LowerEyeLidL.setAutoDisable(False)
    # LowerEyeLidL.rest()

##############################################################
#                                                            #
# Servo Neck Group                                           #
#                                                            #
##############################################################

if EnableHeadYaw == True:
    print "Head Yaw"
    HeadYaw = Runtime.createAndStart("HeadYaw", "Servo")
    if HeadYawAttachment == "Head":
        HeadYaw.attach(Head, HeadYawPin)
    if HeadYawAttachment == "Back":
        HeadYaw.attach(Back, HeadYawPin)
    if HeadYawAttachment == "RightArm":
        HeadYaw.attach(RightArm, HeadYawPin)
    if HeadYawAttachment == "LeftArm":
        HeadYaw.attach(LeftArm, HeadYawPin)
    if HeadYawAttachment == "arduinoLeft":
        HeadYaw.attach(arduinoLeft, HeadYawPin)
    if HeadYawAttachment == "arduinoRight":
        HeadYaw.attach(arduinoRight, HeadYawPin)
    if HeadYawAttachment == "arduinoNano":
        HeadYaw.attach(arduinoNano, HeadYawPin)
    HeadYaw.setMinMax(HeadYawMinPos, HeadYawMaxPos)
    #HeadYaw.map(0,180,1,180)
    HeadYaw.setRest(HeadYawRestPos)
    HeadYaw.setInverted(False)
    HeadYaw.setSpeed(120)
    HeadYaw.setAutoDisable(True)
    HeadYaw.rest()

print "-Back Servo Group"

if EnableHeadPitch == True:
    print "--Head Pitch"
    HeadPitch = Runtime.createAndStart("HeadPitch", "Servo")
    if HeadPitchAttachment == "Head":
        HeadPitch.attach(Head, HeadPitchPin)
    if HeadPitchAttachment == "Back":
        HeadPitch.attach(Back, HeadPitchPin)
    if HeadPitchAttachment == "RightArm":
        HeadPitch.attach(RightArm, HeadPitchPin)
    if HeadPitchAttachment == "LeftArm":
        HeadPitch.attach(LeftArm, HeadPitchPin)
    if HeadPitchAttachment == "arduinoLeft":
        HeadPitch.attach(arduinoLeft, HeadPitchPin)
    if HeadPitchAttachment == "arduinoRight":
        HeadPitch.attach(arduinoRight, HeadPitchPin)
    if HeadPitchAttachment == "arduinoNano":
        HeadPitch.attach(arduinoNano, HeadPitchPin)
    HeadPitch.setMinMax(HeadPitchMinPos, HeadPitchMaxPos)
    #HeadPitch.map(0,180,1,180)
    HeadPitch.setRest(HeadPitchRestPos)
    HeadPitch.setInverted(False)
    HeadPitch.setSpeed(120)
    HeadPitch.setAutoDisable(True)
    HeadPitch.rest()

if EnableHeadRoll == True:
    print "--Head Roll"
    HeadRoll = Runtime.createAndStart("HeadRoll", "Servo")
    if HeadRollAttachment == "Head":
        HeadRoll.attach(Head, HeadRollPin)
    if HeadRollAttachment == "Back":
        HeadRoll.attach(Back, HeadRollPin)
    if HeadRollAttachment == "RightArm":
        HeadRoll.attach(RightArm, HeadRollPin)
    if HeadRollAttachment == "LeftArm":
        HeadRoll.attach(LeftArm, HeadRollPin)
    if HeadRollAttachment == "arduinoLeft":
        HeadRoll.attach(arduinoLeft, HeadRollPin)
    if HeadRollAttachment == "arduinoRight":
        HeadRoll.attach(arduinoRight, HeadRollPin)
    if HeadRollAttachment == "arduinoNano":
        HeadRoll.attach(arduinoNano, HeadRollPin)
    HeadRoll.setMinMax(HeadRollMinPos, HeadRollMaxPos)
    #HeadRoll.map(0,180,1,180)
    HeadRoll.setRest(HeadRollRestPos)
    HeadRoll.setInverted(False)
    HeadRoll.setSpeed(120)
    HeadRoll.setAutoDisable(True)
    HeadRoll.rest()

##############################################################
#                                                            #
# Servo Torso Group                                          #
#                                                            #
##############################################################

if EnableTopStomach == True:
    print "--Top Stomach"
    TopStomach = Runtime.createAndStart("TopStomach", "Servo")
    if TopStomachAttachment == "Head":
        TopStomach.attach(Head, TopStomachPin)
    if TopStomachAttachment == "Back":
        TopStomach.attach(Back, TopStomachPin)
    if TopStomachAttachment == "RightArm":
        TopStomach.attach(RightArm, TopStomachPin)
    if TopStomachAttachment == "LeftArm":
        TopStomach.attach(LeftArm, TopStomachPin)
    if TopStomachAttachment == "arduinoLeft":
        TopStomach.attach(arduinoLeft, TopStomachPin)
    if TopStomachAttachment == "arduinoRight":
        TopStomach.attach(arduinoRight, TopStomachPin)
    if TopStomachAttachment == "arduinoNano":
        TopStomach.attach(arduinoNano, TopStomachPin)
    TopStomach.setMinMax(TopStomachMinPos, TopStomachMaxPos)
    #TopStomach.map(0,180,1,180)
    TopStomach.setRest(TopStomachRestPos)
    TopStomach.setInverted(False)
    TopStomach.setSpeed(120)
    TopStomach.setAutoDisable(True)
    TopStomach.rest()

if EnableMidStomach == True:
    print "--Top Stomach"
    MidStomach = Runtime.createAndStart("TopStomach", "Servo")
    if MidStomachAttachment == "Head":
        MidStomach.attach(Head, MidStomachPin)
    if MidStomachAttachment == "Back":
        MidStomach.attach(Back, MidStomachPin)
    if MidStomachAttachment == "RightArm":
        MidStomach.attach(RightArm, MidStomachPin)
    if MidStomachAttachment == "LeftArm":
        MidStomach.attach(LeftArm, MidStomachPin)
    if MidStomachAttachment == "arduinoLeft":
        MidStomach.attach(arduinoLeft, MidStomachPin)
    if MidStomachAttachment == "arduinoRight":
        MidStomach.attach(arduinoRight, MidStomachPin)
    if MidStomachAttachment == "arduinoNano":
        MidStomach.attach(arduinoNano, MidStomachPin)
    MidStomach.setMinMax(MidStomachMinPos, MidStomachMaxPos)
    #MidStomach.map(0,180,1,180)
    MidStomach.setRest(MidStomachRestPos)
    MidStomach.setInverted(False)
    MidStomach.setSpeed(120)
    MidStomach.setAutoDisable(True)
    MidStomach.rest()

##############################################################
#                                                            #
# Servo Right Arm Group                                      #
#                                                            #
##############################################################

if EnableRightOmoPlate == True:
    print "--Right OmoPlate"
    RightOmoPlate = Runtime.createAndStart("RightOmoPlate", "Servo")
    if RightOmoPlateAttachment == "Head":
        RightOmoPlate.attach(Head, RightOmoPlatePin)
    if RightOmoPlateAttachment == "Back":
        RightOmoPlate.attach(Back, RightOmoPlatePin)
    if RightOmoPlateAttachment == "RightArm":
        RightOmoPlate.attach(RightArm, RightOmoPlatePin)
    if RightOmoPlateAttachment == "LeftArm":
        RightOmoPlate.attach(LeftArm, RightOmoPlatePin)
    if RightOmoPlateAttachment == "arduinoLeft":
        RightOmoPlate.attach(arduinoLeft, RightOmoPlatePin)
    if RightOmoPlateAttachment == "arduinoRight":
        RightOmoPlate.attach(arduinoRight, RightOmoPlatePin)
    if RightOmoPlateAttachment == "arduinoNano":
        RightOmoPlate.attach(arduinoNano, RightOmoPlatePin)
    RightOmoPlate.setMinMax(RightOmoPlateMinPos, RightOmoPlateMaxPos)
    #RightOmoPlate.map(0,180,1,180)
    RightOmoPlate.setRest(RightOmoPlateRestPos)
    RightOmoPlate.setInverted(False)
    RightOmoPlate.setSpeed(120)
    RightOmoPlate.setAutoDisable(True)
    RightOmoPlate.rest()

if EnableRightShoulder == True:
    print "--Right Shoulder"
    RightShoulder = Runtime.createAndStart("RightShoulder", "Servo")
    if RightShoulderAttachment == "Head":
        RightShoulder.attach(Head, RightShoulderPin)
    if RightShoulderAttachment == "Back":
        RightShoulder.attach(Back, RightShoulderPin)
    if RightShoulderAttachment == "RightArm":
        RightShoulder.attach(RightArm, RightShoulderPin)
    if RightShoulderAttachment == "LeftArm":
        RightShoulder.attach(LeftArm, RightShoulderPin)
    if RightShoulderAttachment == "arduinoLeft":
        RightShoulder.attach(arduinoLeft, RightShoulderPin)
    if RightShoulderAttachment == "arduinoRight":
        RightShoulder.attach(arduinoRight, RightShoulderPin)
    if RightShoulderAttachment == "arduinoNano":
        RightShoulder.attach(arduinoNano, RightShoulderPin)
    RightShoulder.setMinMax(RightShoulderMinPos, RightShoulderMaxPos)
    #RightShoulder.map(0,180,1,180)
    RightShoulder.setRest(RightShoulderRestPos)
    RightShoulder.setInverted(False)
    RightShoulder.setSpeed(120)
    RightShoulder.setAutoDisable(True)
    RightShoulder.rest()

if EnableRightRotate == True:
    print "--Right Rotate"
    RightRotate = Runtime.createAndStart("RightRotate", "Servo")
    if RightRotateAttachment == "Head":
        RightRotate.attach(Head, RightRotatePin)
    if RightRotateAttachment == "Back":
        RightRotate.attach(Back, RightRotatePin)
    if RightRotateAttachment == "RightArm":
        RightRotate.attach(RightArm, RightRotatePin)
    if RightRotateAttachment == "LeftArm":
        RightRotate.attach(LeftArm, RightRotatePin)
    if RightRotateAttachment == "arduinoLeft":
        RightRotate.attach(arduinoLeft, RightRotatePin)
    if RightRotateAttachment == "arduinoRight":
        RightRotate.attach(arduinoRight, RightRotatePin)
    if RightRotateAttachment == "arduinoNano":
        RightRotate.attach(arduinoNano, RightRotatePin)
    RightRotate.setMinMax(RightRotateMinPos, RightRotateMaxPos)
    #RightRotate.map(0,180,1,180)
    RightRotate.setRest(RightRotateRestPos)
    RightRotate.setInverted(False)
    RightRotate.setSpeed(120)
    RightRotate.setAutoDisable(True)
    RightRotate.rest()

if EnableRightBicep == True:
    print "--Right Bicep"
    RightBicep = Runtime.createAndStart("RightBicep", "Servo")
    if RightBicepAttachment == "Head":
        RightBicep.attach(Head, RightBicepPin)
    if RightBicepAttachment == "Back":
        RightBicep.attach(Back, RightBicepPin)
    if RightBicepAttachment == "RightArm":
        RightBicep.attach(RightArm, RightBicepPin)
    if RightBicepAttachment == "LeftArm":
        RightBicep.attach(LeftArm, RightBicepPin)
    if RightBicepAttachment == "arduinoLeft":
        RightBicep.attach(arduinoLeft, RightBicepPin)
    if RightBicepAttachment == "arduinoRight":
        RightBicep.attach(arduinoRight, RightBicepPin)
    if RightBicepAttachment == "arduinoNano":
        RightBicep.attach(arduinoNano, RightBicepPin)
    RightBicep.setMinMax(RightBicepMinPos, RightBicepMaxPos)
    #RightBicep.map(0,180,1,180)
    RightBicep.setRest(RightBicepRestPos)
    RightBicep.setInverted(False)
    RightBicep.setSpeed(120)
    RightBicep.setAutoDisable(True)
    RightBicep.rest()

##############################################################
#                                                            #
# Servo Left Arm Group                                       #
#                                                            #
##############################################################

if EnableLeftOmoPlate == True:
    print "--Left OmoPlate"
    LeftOmoPlate = Runtime.createAndStart("LeftOmoPlate", "Servo")
    if LeftOmoPlateAttachment == "Head":
        LeftOmoPlate.attach(Head, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "Back":
        LeftOmoPlate.attach(Back, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "RightArm":
        LeftOmoPlate.attach(RightArm, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "LeftArm":
        LeftOmoPlate.attach(LeftArm, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "arduinoLeft":
        LeftOmoPlate.attach(arduinoLeft, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "arduinoRight":
        LeftOmoPlate.attach(arduinoRight, LeftOmoPlatePin)
    if LeftOmoPlateAttachment == "arduinoNano":
        LeftOmoPlate.attach(arduinoNano, LeftOmoPlatePin)
    LeftOmoPlate.setMinMax(LeftOmoPlateMinPos, LeftOmoPlateMaxPos)
    #LeftOmoPlate.map(0,180,1,180)
    LeftOmoPlate.setRest(LeftOmoPlateRestPos)
    LeftOmoPlate.setInverted(False)
    LeftOmoPlate.setSpeed(120)
    LeftOmoPlate.setAutoDisable(True)
    LeftOmoPlate.rest()

if EnableLeftShoulder == True:
    print "--Left Shoulder"
    LeftShoulder = Runtime.createAndStart("LeftShoulder", "Servo")
    if LeftShoulderAttachment == "Head":
        LeftShoulder.attach(Head, LeftShoulderPin)
    if LeftShoulderAttachment == "Back":
        LeftShoulder.attach(Back, LeftShoulderPin)
    if LeftShoulderAttachment == "RightArm":
        LeftShoulder.attach(RightArm, LeftShoulderPin)
    if LeftShoulderAttachment == "LeftArm":
        LeftShoulder.attach(LeftArm, LeftShoulderPin)
    if LeftShoulderAttachment == "arduinoLeft":
        LeftShoulder.attach(arduinoLeft, LeftShoulderPin)
    if LeftShoulderAttachment == "arduinoRight":
        LeftShoulder.attach(arduinoRight, LeftShoulderPin)
    if LeftShoulderAttachment == "arduinoNano":
        LeftShoulder.attach(arduinoNano, LeftShoulderPin)
    LeftShoulder.setMinMax(LeftShoulderMinPos, LeftShoulderMaxPos)
    #LeftShoulder.map(0,180,1,180)
    LeftShoulder.setRest(LeftShoulderRestPos)
    LeftShoulder.setInverted(False)
    LeftShoulder.setSpeed(120)
    LeftShoulder.setAutoDisable(True)
    LeftShoulder.rest()

if EnableLeftRotate == True:
    print "--Left Rotate"
    LeftRotate = Runtime.createAndStart("LeftRotate", "Servo")
    if LeftRotateAttachment == "Head":
        LeftRotate.attach(Head, LeftRotatePin)
    if LeftRotateAttachment == "Back":
        LeftRotate.attach(Back, LeftRotatePin)
    if LeftRotateAttachment == "RightArm":
        LeftRotate.attach(RightArm, LeftRotatePin)
    if LeftRotateAttachment == "LeftArm":
        LeftRotate.attach(LeftArm, LeftRotatePin)
    if LeftRotateAttachment == "arduinoLeft":
        LeftRotate.attach(arduinoLeft, LeftRotatePin)
    if LeftRotateAttachment == "arduinoRight":
        LeftRotate.attach(arduinoRight, LeftRotatePin)
    if LeftRotateAttachment == "arduinoNano":
        LeftRotate.attach(arduinoNano, LeftRotatePin)
    LeftRotate.setMinMax(LeftRotateMinPos, LeftRotateMaxPos)
    #LeftRotate.map(0,180,1,180)
    LeftRotate.setRest(RightRotateRestPos)
    LeftRotate.setInverted(False)
    LeftRotate.setSpeed(120)
    LeftRotate.setAutoDisable(True)
    LeftRotate.rest()

if EnableLeftBicep == True:
    print "--Left Bicep"
    LeftBicep = Runtime.createAndStart("LeftBicep", "Servo")
    if LeftBicepAttachment == "Head":
        LeftBicep.attach(Head, LeftBicepPin)
    if LeftBicepAttachment == "Back":
        LeftBicep.attach(Back, LeftBicepPin)
    if LeftBicepAttachment == "RightArm":
        LeftBicep.attach(RightArm, LeftBicepPin)
    if LeftBicepAttachment == "LeftArm":
        LeftBicep.attach(LeftArm, LeftBicepPin)
    if LeftBicepAttachment == "arduinoLeft":
        LeftBicep.attach(arduinoLeft, LeftBicepPin)
    if LeftBicepAttachment == "arduinoRight":
        LeftBicep.attach(arduinoRight, LeftBicepPin)
    if LeftBicepAttachment == "arduinoNano":
        LeftBicep.attach(arduinoNano, LeftBicepPin)
    LeftBicep.setMinMax(LeftBicepMinPos, LeftBicepMaxPos)
    #LeftBicep.map(0,180,1,180)
    LeftBicep.setRest(LeftBicepRestPos)
    LeftBicep.setInverted(False)
    LeftBicep.setSpeed(120)
    LeftBicep.setAutoDisable(True)
    LeftBicep.rest()

##############################################################
#                                                            #
# Servo Right Hand Group                                     #
#                                                            #
##############################################################

if EnableRightThumb == True:
    print "--Right Thumb"
    RightThumb = Runtime.createAndStart("RightThumb", "Servo")
    if RightThumbAttachment == "Head":
        RightThumb.attach(Head, RightThumbPin)
    if RightThumbAttachment == "Back":
        RightThumb.attach(Back, RightThumbPin)
    if RightThumbAttachment == "RightArm":
        RightThumb.attach(RightArm, RightThumbPin)
    if RightThumbAttachment == "LeftArm":
        RightThumb.attach(LeftArm, RightThumbPin)
    if RightThumbAttachment == "arduinoLeft":
        RightThumb.attach(arduinoLeft, RightThumbPin)
    if RightThumbAttachment == "arduinoRight":
        RightThumb.attach(arduinoRight, RightThumbPin)
    if RightThumbAttachment == "arduinoNano":
        RightThumb.attach(arduinoNano, RightThumbPin)
    RightThumb.setMinMax(RightThumbMinPos, RightThumbMaxPos)
    #RightThumb.map(0,180,1,180)
    RightThumb.setRest(RightThumbRestPos)
    RightThumb.setInverted(False)
    RightThumb.setSpeed(120)
    RightThumb.setAutoDisable(True)
    RightThumb.rest()

if EnableRightIndex == True:
    print "--Right Index"
    RightIndex = Runtime.createAndStart("RightIndex", "Servo")
    if RightIndexAttachment == "Head":
        RightIndex.attach(Head, RightIndexPin)
    if RightIndexAttachment == "Back":
        RightIndex.attach(Back, RightIndexPin)
    if RightIndexAttachment == "RightArm":
        RightIndex.attach(RightArm, RightIndexPin)
    if RightIndexAttachment == "LeftArm":
        RightIndex.attach(LeftArm, RightIndexPin)
    if RightIndexAttachment == "arduinoLeft":
        RightIndex.attach(arduinoLeft, RightIndexPin)
    if RightIndexAttachment == "arduinoRight":
        RightIndex.attach(arduinoRight, RightIndexPin)
    if RightIndexAttachment == "arduinoNano":
        RightIndex.attach(arduinoNano, RightIndexPin)
    RightIndex.setMinMax(RightIndexMinPos, RightIndexMaxPos)
    #RightIndex.map(0,180,1,180)
    RightIndex.setRest(RightIndexRestPos)
    RightIndex.setInverted(False)
    RightIndex.setSpeed(120)
    RightIndex.setAutoDisable(True)
    RightIndex.rest()

if EnableRightMajor == True:
    print "--Right Major"
    RightMajor = Runtime.createAndStart("RightMajor", "Servo")
    if RightMajorAttachment == "Head":
        RightMajor.attach(Head, RightMajorPin)
    if RightMajorAttachment == "Back":
        RightMajor.attach(Back, RightMajorPin)
    if RightMajorAttachment == "RightArm":
        RightMajor.attach(RightArm, RightMajorPin)
    if RightMajorAttachment == "LeftArm":
        RightMajor.attach(LeftArm, RightMajorPin)
    if RightMajorAttachment == "arduinoLeft":
        RightMajor.attach(arduinoLeft, RightMajorPin)
    if RightMajorAttachment == "arduinoRight":
        RightMajor.attach(arduinoRight, RightMajorPin)
    if RightMajorAttachment == "arduinoNano":
        RightMajor.attach(arduinoNano, RightMajorPin)
    RightMajor.setMinMax(RightMajorMinPos, RightMajorMaxPos)
    #RightMajor.map(0,180,1,180)
    RightMajor.setRest(RightMajorRestPos)
    RightMajor.setInverted(False)
    RightMajor.setSpeed(120)
    RightMajor.setAutoDisable(True)
    RightMajor.rest()

if EnableRightRing == True:
    print "--Right Ring"
    RightRing = Runtime.createAndStart("RightRing", "Servo")
    if RightRingAttachment == "Head":
        RightRing.attach(Head, RightRingPin)
    if RightRingAttachment == "Back":
        RightRing.attach(Back, RightRingPin)
    if RightRingAttachment == "RightArm":
        RightRing.attach(RightArm, RightRingPin)
    if RightRingAttachment == "LeftArm":
        RightRing.attach(LeftArm, RightRingPin)
    if RightRingAttachment == "arduinoLeft":
        RightRing.attach(arduinoLeft, RightRingPin)
    if RightRingAttachment == "arduinoRight":
        RightRing.attach(arduinoRight, RightRingPin)
    if RightRingAttachment == "arduinoNano":
        RightRing.attach(arduinoNano, RightRingPin)
    RightRing.setMinMax(RightRingMinPos, RightRingMaxPos)
    #RightRing.map(0,180,1,180)
    RightRing.setRest(RightRingRestPos)
    RightRing.setInverted(False)
    RightRing.setSpeed(120)
    RightRing.setAutoDisable(True)
    RightRing.rest()

if EnableRightPinky == True:
    print "--Right Pinky"
    RightPinky = Runtime.createAndStart("RightPinky", "Servo")
    if RightPinkyAttachment == "Head":
        RightPinky.attach(Head, RightPinkyPin)
    if RightPinkyAttachment == "Back":
        RightPinky.attach(Back, RightPinkyPin)
    if RightPinkyAttachment == "RightArm":
        RightPinky.attach(RightArm, RightPinkyPin)
    if RightPinkyAttachment == "LeftArm":
        RightPinky.attach(LeftArm, RightPinkyPin)
    if RightPinkyAttachment == "arduinoLeft":
        RightPinky.attach(arduinoLeft, RightPinkyPin)
    if RightPinkyAttachment == "arduinoRight":
        RightPinky.attach(arduinoRight, RightPinkyPin)
    if RightPinkyAttachment == "arduinoNano":
        RightPinky.attach(arduinoNano, RightPinkyPin)
    RightPinky.setMinMax(RightPinkyMinPos, RightPinkyMaxPos)
    #RightPinky.map(0,180,1,180)
    RightPinky.setRest(RightPinkyRestPos)
    RightPinky.setInverted(False)
    RightPinky.setSpeed(120)
    RightPinky.setAutoDisable(True)
    RightPinky.rest()

if EnableRightWrist == True:
    print "--Right Wrist"
    RightWrist = Runtime.createAndStart("RightWrist", "Servo")
    if RightWristAttachment == "Head":
        RightWrist.attach(Head, RightWristPin)
    if RightWristAttachment == "Back":
        RightWrist.attach(Back, RightWristPin)
    if RightWristAttachment == "RightArm":
        RightWrist.attach(RightArm, RightWristPin)
    if RightWristAttachment == "LeftArm":
        RightWrist.attach(LeftArm, RightWristPin)
    if RightWristAttachment == "arduinoLeft":
        RightWrist.attach(arduinoLeft, RightWristPin)
    if RightWristAttachment == "arduinoRight":
        RightWrist.attach(arduinoRight, RightWristPin)
    if RightWristAttachment == "arduinoNano":
        RightWrist.attach(arduinoNano, RightWristPin)
    RightWrist.setMinMax(RightWristMinPos, RightWristMaxPos)
    #RightWrist.map(0,180,1,180)
    RightWrist.setRest(RightWristRestPos)
    RightWrist.setInverted(False)
    RightWrist.setSpeed(120)
    RightWrist.setAutoDisable(True)
    RightWrist.rest()

##############################################################
#                                                            #
# Servo Left Hand Group                                      #
#                                                            #
##############################################################

if EnableLeftThumb == True:
    print "--Left Thumb"
    LeftThumb = Runtime.createAndStart("LeftThumb", "Servo")
    if LeftThumbAttachment == "Head":
        LeftThumb.attach(Head, LeftThumbPin)
    if LeftThumbAttachment == "Back":
        LeftThumb.attach(Back, LeftThumbPin)
    if LeftThumbAttachment == "RightArm":
        LeftThumb.attach(RightArm, LeftThumbPin)
    if LeftThumbAttachment == "LeftArm":
        LeftThumb.attach(LeftArm, LeftThumbPin)
    if LeftThumbAttachment == "arduinoLeft":
        LeftThumb.attach(arduinoLeft, LeftThumbPin)
    if LeftThumbAttachment == "arduinoRight":
        LeftThumb.attach(arduinoRight, LeftThumbPin)
    if LeftThumbAttachment == "arduinoNano":
        LeftThumb.attach(arduinoNano, LeftThumbPin)
    LeftThumb.setMinMax(LeftThumbMinPos, LeftThumbMaxPos)
    #LeftThumb.map(0,180,1,180)
    LeftThumb.setRest(LeftThumbRestPos)
    LeftThumb.setInverted(False)
    LeftThumb.setSpeed(120)
    LeftThumb.setAutoDisable(True)
    LeftThumb.rest()

if EnableLeftIndex == True:
    print "--Left Index"
    LeftIndex = Runtime.createAndStart("LeftIndex", "Servo")
    if LeftIndexAttachment == "Head":
        LeftIndex.attach(Head, LeftIndexPin)
    if LeftIndexAttachment == "Back":
        LeftIndex.attach(Back, LeftIndexPin)
    if LeftIndexAttachment == "RightArm":
        LeftIndex.attach(RightArm, LeftIndexPin)
    if LeftIndexAttachment == "LeftArm":
        LeftIndex.attach(LeftArm, LeftIndexPin)
    if LeftIndexAttachment == "arduinoLeft":
        LeftIndex.attach(arduinoLeft, LeftIndexPin)
    if LeftIndexAttachment == "arduinoRight":
        LeftIndex.attach(arduinoRight, LeftIndexPin)
    if LeftIndexAttachment == "arduinoNano":
        LeftIndex.attach(arduinoNano, LeftIndexPin)
    LeftIndex.setMinMax(LeftIndexMinPos, LeftIndexMaxPos)
    #LeftIndex.map(0,180,1,180)
    LeftIndex.setRest(LeftIndexRestPos)
    LeftIndex.setInverted(False)
    LeftIndex.setSpeed(120)
    LeftIndex.setAutoDisable(True)
    LeftIndex.rest()

if EnableLeftMajor == True:
    print "--Left Major"
    LeftMajor = Runtime.createAndStart("LeftMajor", "Servo")
    if LeftMajorAttachment == "Head":
        LeftMajor.attach(Head, LeftMajorPin)
    if LeftMajorAttachment == "Back":
        LeftMajor.attach(Back, LeftMajorPin)
    if LeftMajorAttachment == "RightArm":
        LeftMajor.attach(RightArm, LeftMajorPin)
    if LeftMajorAttachment == "LeftArm":
        LeftMajor.attach(LeftArm, LeftMajorPin)
    if LeftMajorAttachment == "arduinoLeft":
        LeftMajor.attach(arduinoLeft, LeftMajorPin)
    if LeftMajorAttachment == "arduinoRight":
        LeftMajor.attach(arduinoRight, LeftMajorPin)
    if LeftMajorAttachment == "arduinoNano":
        LeftMajor.attach(arduinoNano, LeftMajorPin)
    LeftMajor.setMinMax(LeftMajorMinPos, LeftMajorMaxPos)
    #LeftMajor.map(0,180,1,180)
    LeftMajor.setRest(LeftMajorRestPos)
    LeftMajor.setInverted(False)
    LeftMajor.setSpeed(120)
    LeftMajor.setAutoDisable(True)
    LeftMajor.rest()

if EnableLeftRing == True:
    print "--Left Ring"
    LeftRing = Runtime.createAndStart("LeftRing", "Servo")
    if LeftRingAttachment == "Head":
        LeftRing.attach(Head, LeftRingPin)
    if LeftRingAttachment == "Back":
        LeftRing.attach(Back, LeftRingPin)
    if LeftRingAttachment == "RightArm":
        LeftRing.attach(RightArm, LeftRingPin)
    if LeftRingAttachment == "LeftArm":
        LeftRing.attach(LeftArm, LeftRingPin)
    if LeftRingAttachment == "arduinoLeft":
        LeftRing.attach(arduinoLeft, LeftRingPin)
    if LeftRingAttachment == "arduinoRight":
        LeftRing.attach(arduinoRight, LeftRingPin)
    if LeftRingAttachment == "arduinoNano":
        LeftRing.attach(arduinoNano, LeftRingPin)
    LeftRing.setMinMax(LeftRingMinPos, LeftRingMaxPos)
    #LeftRing.map(0,180,1,180)
    LeftRing.setRest(LeftRingRestPos)
    LeftRing.setInverted(False)
    LeftRing.setSpeed(120)
    LeftRing.setAutoDisable(True)
    LeftRing.rest()

if EnableLeftPinky == True:
    print "--Left Pinky"
    LeftPinky = Runtime.createAndStart("LeftPinky", "Servo")
    if LeftPinkyAttachment == "Head":
        LeftPinky.attach(Head, LeftPinkyPin)
    if LeftPinkyAttachment == "Back":
        LeftPinky.attach(Back, LeftPinkyPin)
    if LeftPinkyAttachment == "RightArm":
        LeftPinky.attach(RightArm, LeftPinkyPin)
    if LeftPinkyAttachment == "LeftArm":
        LeftPinky.attach(LeftArm, LeftPinkyPin)
    if LeftPinkyAttachment == "arduinoLeft":
        LeftPinky.attach(arduinoLeft, LeftPinkyPin)
    if LeftPinkyAttachment == "arduinoRight":
        LeftPinky.attach(arduinoRight, LeftPinkyPin)
    if LeftPinkyAttachment == "arduinoNano":
        LeftPinky.attach(arduinoNano, LeftPinkyPin)
    LeftPinky.setMinMax(LeftPinkyMinPos, LeftPinkyMaxPos)
    #LeftPinky.map(0,180,1,180)
    LeftPinky.setRest(LeftPinkyRestPos)
    RightPinky.setInverted(False)
    LeftPinky.setSpeed(120)
    LeftPinky.setAutoDisable(True)
    LeftPinky.rest()

if EnableLeftWrist == True:
    print "--Left Wrist"
    LeftWrist = Runtime.createAndStart("LeftWrist", "Servo")
    if LeftWristAttachment == "Head":
        LeftWrist.attach(Head, LeftWristPin)
    if LeftWristAttachment == "Back":
        LeftWrist.attach(Back, LeftWristPin)
    if LeftWristAttachment == "RightArm":
        LeftWrist.attach(RightArm, LeftWristPin)
    if LeftWristAttachment == "LeftArm":
        LeftWrist.attach(LeftArm, LeftWristPin)
    if LeftWristAttachment == "arduinoLeft":
        LeftWrist.attach(arduinoLeft, LeftWristPin)
    if LeftWristAttachment == "arduinoRight":
        LeftWrist.attach(arduinoRight, LeftWristPin)
    if LeftWristAttachment == "arduinoNano":
        LeftWrist.attach(arduinoNano, LeftWristPin)
    LeftWrist.setMinMax(LeftWristMinPos, LeftWristMaxPos)
    #LeftWrist.map(0,180,1,180)
    LeftWrist.setRest(LeftWristRestPos)
    LeftWrist.setInverted(False)
    LeftWrist.setSpeed(120)
    LeftWrist.setAutoDisable(True)
    LeftWrist.rest()
