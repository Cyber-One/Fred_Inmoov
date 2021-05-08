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
# A_IO_Config.py                                 #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Input/Output Config"
##############################################################
#                                                            #
# Input / Output Device Group                                #
#                                                            #
##############################################################

EnablePIR = False
PirAttachment = "arduinoNano"   # "arduioLeft"
PirPin = 2                      # 23

EnableLeftUltrasonic = True
LeftUltrasonicAttachment = "arduinoNano"
LeftUltrasonicPin1 = 12
LeftUltrasonicPin2 = 11

EnableRightUltraSonic = True
RightUltrasonicAttachment = "arduinoNano"
RightUltrasonicPin1 = 10
RightUltrasonicPin2 = 9
