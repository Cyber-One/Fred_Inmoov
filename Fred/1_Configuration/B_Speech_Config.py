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
print "Creating the Speech System Config"
##############################################################
#                                                            #
# Speech To Text and Text To Speech Group                    #
#                                                            #
##############################################################

##############################################################
# TTS Select only one of these three options.
##############################################################

# This is the default TTS used in the InMoov robot.
# It's been around for a while and works, but there are others.
UseMarySpeech = False

# MimicSpeech TTS
# Created by Microft-AI this TTS is pretty good.
# before you can use this on the Raspberry Pi, 
# you first need to install it.
# By default this is not installed for the ARM based computer 
# like the Raspberry Pi, for detailed instructions on 
# installing this please watch my video
# https://youtu.be/OSbqlRWYBkQ
UseMimicSpeech = False

# Espeak TTS
# before you can use this on the Raspberry Pi, 
# you first need to install it.
# By default this is not installed for the ARM based 
# computer like the Raspberry Pi.
# This is very easy with the command 
# "sudo apt-get install espeak"
UseEspeak = True

# Local speech is different between the Windows system and the
# Linux/Mac system.  Linux/Mac uses Festival Speech while the
# Windows version uses the TTS.exe file that is installed as
# part of MRL.
# On the Raspberry Pi and possibly on the Mac, you will need
# to install the Festival STT before you can use this service.
# "sudo apt-get install festival"
UseLocalSpeech = False

##############################################################
# STT Select only one of these two options.
##############################################################

# Sphinx is locally run service that does not require access to the internet to work
# The down side is that is doesn't recognise anywhere near as many words.
UseSphinx = False

# WebkitSpeechRecognition is a very capable service recognising most spoken 
# words with a number of different accents.
# The down side is it does require an Internet access to reach the cloud.
# the cloud service does support quite a number of languages, for a full
# list have a look here: https://cloud.google.com/speech/docs/languages
UseWebKit = False
WebkitLanguage = "en-AU"
WebKitWakeWord = ""
