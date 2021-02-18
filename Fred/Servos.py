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
    # This method takes two parameters, the first can be the 
    # name of the service or the service object.
    # The second parameter is the pin on the controller that 
    # the servo will be attached to.
    Jaw.attach(JawAttachment, JawPin)
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
    RightEyeLR.attach(RightEyeXAttachment, RightEyeXPin)
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
    RightEyeUD.attach(RightEyeYAttachment, RightEyeYPin)
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
    LeftEyeLR.attach(LeftEyeXAttachment, LeftEyeXPin)
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
    LeftEyeUD.attach(LeftEyeYAttachment, LeftEyeYPin)
    LeftEyeUD.setMinMax(LeftEyeYMinPos, LeftEyeYMaxPos)
    #LeftEyeUD.map(0,180,1,180)
    LeftEyeUD.setRest(LeftEyeYRestPos)
    LeftEyeUD.setInverted(False)
    LeftEyeUD.setSpeed(60)
    LeftEyeUD.setAutoDisable(True)
    LeftEyeUD.rest()

if EnableUpperEyeLid == True:
    print "--Upper Eyelids"
    UpperEyeLid = Runtime.createAndStart("UpperEyeLid", "Servo")
    UpperEyeLid.attach(UpperEyeLidAttachment, UpperEyeLidPin)
    UpperEyeLid.setMinMax(UpperEyeLidMinPos, UpperEyeLidMaxPos)
    #UpperEyeLid.map(0,180,45,180)
    UpperEyeLid.setRest(UpperEyeLidRestPos)
    UpperEyeLid.setInverted(False)
    UpperEyeLid.setSpeed(-1)
    UpperEyeLid.setAutoDisable(False)
    # UpperEyeLid.rest()

if EnableLowerEyeLid == True:
    print "--Lower Eyelids"
    LowerEyeLid = Runtime.createAndStart("LowerEyeLid", "Servo")
    LowerEyeLid.attach(LowerEyeLidAttachment, LowerEyeLidPin)
    LowerEyeLid.setMinMax(LowerEyeLidMinPos, LowerEyeLidMaxPos)
    #LowerEyeLid.map(0,180,0,120)
    LowerEyeLid.setRest(LowerEyeLidRestPos)
    LowerEyeLid.setInverted(False)
    LowerEyeLid.setSpeed(-1)
    LowerEyeLid.setAutoDisable(False)
    # LowerEyeLid.rest()

##############################################################
#                                                            #
# Servo Neck Group                                           #
#                                                            #
##############################################################

if EnableHeadYaw == True:
    print "Head Yaw"
    HeadYaw = Runtime.createAndStart("HeadYaw", "Servo")
    HeadYaw.attach(HeadYawAttachment, HeadYawPin)
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
    HeadPitch.attach(HeadPitchAttachment, HeadPitchPin)
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
    HeadRoll.attach(HeadRollAttachment, HeadRollPin)
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
    TopStomach.attach(TopStomachAttachment, TopStomachPin)
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
    MidStomach.attach(MidStomachAttachment, MidStomachPin)
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
    RightOmoPlate.attach(RightOmoPlateAttachment, RightOmoPlatePin)
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
    RightShoulder.attach(RightShoulderAttachment, RightShoulderPin)
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
    RightRotate.attach(RightRotateAttachment, RightRotatePin)
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
    RightBicep.attach(RightBicepAttachment, RightBicepPin)
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
    LeftOmoPlate.attach(LeftOmoPlateAttachment, LeftOmoPlatePin)
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
    LeftShoulder.attach(LeftShoulderAttachment, LeftShoulderPin)
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
    LeftRotate.attach(LeftRotateAttachment, LeftRotatePin)
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
    LeftBicep.attach(LeftBicepAttachment, LeftBicepPin)
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
    RightThumb.attach(RightThumbAttachment, RightThumbPin)
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
    RightIndex.attach(RightIndexAttachment, RightIndexPin)
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
    RightMajor.attach(RightMajorAttachment, RightMajorPin)
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
    RightRing.attach(RightRingAttachment, RightRingPin)
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
    RightPinky.attach(RightPinkyAttachment, RightPinkyPin)
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
    RightWrist.attach(RightWristAttachment, RightWristPin)
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
    LeftThumb.attach(LeftThumbAttachment, LeftThumbPin)
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
    LeftIndex.attach(LeftIndexAttachment, LeftIndexPin)
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
    LeftMajor.attach(LeftMajorAttachment, LeftMajorPin)
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
    LeftRing.attach(LeftRingAttachment, LeftRingPin)
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
    LeftPinky.attach(LeftPinkyAttachment, LeftPinkyPin)
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
    LeftWrist.attach(LeftWristAttachment, LeftWristPin)
    LeftWrist.setMinMax(LeftWristMinPos, LeftWristMaxPos)
    #LeftWrist.map(0,180,1,180)
    LeftWrist.setRest(LeftWristRestPos)
    LeftWrist.setInverted(False)
    LeftWrist.setSpeed(120)
    LeftWrist.setAutoDisable(True)
    LeftWrist.rest()
