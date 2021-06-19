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
# 1_Sys_Config.py                                            #
# This is where the configuration settings live for the      #
# system.                                                    #
#                                                            #
##############################################################
print "Creating the System Config"

##############################################################
#                                                            #
# The Graphical User Interface (GUI)                         #
#                                                            #
##############################################################
# This is the name the robot will use in some sections of the
# program such as WebKitSpeechRecognition.
RobotsName = "Fred"

# SwingGUI was the origonal one and still my prefference 
# until the rest of the WebGUI pages are conpleted.
RunSwingGUI = True          # True for on, False for off

# WebGUI is the new boy on the block and is getting better.
# It will be started in anycase if you decide to use 
# WebKitSpeechRecognition.
RunWebGUI = True           # True for on, False for off
# WebGUI can be run headless, that is the web client interface 
# can be on another computer.  In this case we don't want to 
# launch the local web browser.  The local web browser also 
# uses a lot of computer power.
RunWebGUIbrowser = False    # True for on, False for off
