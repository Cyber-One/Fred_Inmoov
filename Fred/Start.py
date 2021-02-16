########################################
#
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
########################################

# Because you might want to place your robots files into a different dicrectory 
# compared to what I have, the RunningFolder variable is the name of the folder 
# you will be using.
RuningFolder="Fred"
RunSwingGUI=True
RunWebGUI=False

# Just to help with diagnostics, we will write out we are starting the system.
print "Starting the Fred MRL OS"

# Before we get too carried away, I plan to start Fred using a shell script callsed start_fred.sh
# This will start the MRL and the Fred scripts with no Graphical User Interfaces (GUI) at all.
# To overcome this issue, we will start the GUI here.
# There are two types of GUI installed in MRL, the SwingGUI and the WebGUI
if RunSwingGUI == True:
    gui = Runtime.start('gui','SwingGui')

if RunWebGUI == True:
    WebGui = Runtime.create("WebGui","WebGui")
    WebGui.hide('cli')
    sleep(1)
    WebGui.show('cli')
    sleep(1)
    WebGui.set('cli', 400, 400, 999)
# if you don't want the browser to autostart to homepage
#    WebGui.autoStartBrowser(false)
# set a different port number to listen to. default is 8888
#    WebGui.setPort(7777)
# on startup the WebGui will look for a "resources"
# directory (may change in the future)
# static html files can be placed here and accessed through
# the WebGui service
# starts the websocket server
# and attempts to autostart browser
    WebGui.startService();


# The execfile() function loads and executes the named program.
# this is handy for breaking a program into smaller more manageable parts.

# Controllers.py starts the major controller interface services
# such as the Raspberry Pi service and the Adafruit Servo controller services
# This is also where you would start any Arduino services you might want to add
# Like the Nano for the Ultra-Sonic sensors or the PIR sensor.
execfile(RuningFolder+'/Controllers.py')

# The next is for the different servos we will be running.
# This file is responsible for starting and configuring each of the servos throughout the robot.
execfile(RuningFolder+'/Servos.py')

# The IO services are for things like the PIR, Ultrasonic range finders and NeoPixel rings ect.
execfile(RuningFolder+'/IO.py')

# When not activly executing a command, we don't want the robot to just stand there,
# This file is responsible for giving our robot a bitof life.
# By blinking the eyes, coordinating the left and right eyes and performing other 
# random like movements, just to make our robot appear to be alive.
execfile(RuningFolder+'/Life.py')

# From time to time, you may want your robot to signal with body movements
# such as nodding or shaking of it's head, this is the file we keep those movements in
execfile(RuningFolder+'/Gestures.py')

# This file sets up the WebKitSpeechRecognition service
# The MarySpeech TTS service and the ProgramAB service that
# interperates the Alice2 AIML files
execfile(RuningFolder+'/Brain.py')

