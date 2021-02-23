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
# B_Speech_Config.py                                         #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Input/Output Config"
##############################################################
#                                                            #
# Speech To Text and Text To Speech Group                    #
#                                                            #
##############################################################

# TTS Select only one of these options.
UseMarySpeech = False
UseMimicSpeech = False
UseEspeak = False

# STT Select only one of these options.
UseSphinx = False
UseWebKit = False
