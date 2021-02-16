#######################################################
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
# Speech.py
# This file is to handel all the speech services
# Text To Speech (TTS)
# Speech To Text (STT)
#                                                     #
#######################################################
print "Creating the Text to Speech and Speech to Text functions"
# As a general rule, we define the TTS services as the mouth and 
# STT services as the Ear :-)

# TTS Select only one of these options.
UseMarySpeech = True
UseMimicSpeech = False

# STT Select only one of these options.
UseSphinx = False
UseWebKit = True

#######################################################
#                                                     #
# Text To Speech (TTS) services                       #
#                                                     #
#######################################################

# MarySpeech TTS
if UseMarySpeech == True:
    Mouth = Runtime.createAndStart("Mouth", "MarySpeech")
    # There are multiple voice types available for MarySpeech, 
    # but to use them, you have to install them :-)
    Mouth.installComponentsAcceptLicense("cmu-bdl-hsmm")
    Mouth.installComponentsAcceptLicense("dfki-obadiah-hsmm")
    Mouth.installComponentsAcceptLicense("dfki-spike-hsmm")
    #Mouth.setVoice("cmu-bdl-hsmm") # Mark
    Mouth.setVoice("cmu-rms-hsmm") # Henry
    #Mouth.setVoice("dfki-obadiah-hsmm") # Obadiah
    #Mouth.setVoice("dfki-spike-hsmm") # Spike
    Mouth.setVolume(100.0)

# MimicSpeech TTS
# before you can use this on the Raspberry Pi, you first need to install it.
# By default this is not installed for the ARM based computer like the Raspberry Pi
# for detailed instructions on installing this please watch my video
# https://youtu.be/OSbqlRWYBkQ
if UseMimicSpeech == True:
    # start the service
    Mouth = Runtime.start('Mouth','MimicSpeech')
    # next we need to tell the service where to find our executable
    Mouth.setMimicExecutable("/home/pi/mimic1/mimic")
    # the next command wil get a list of voices we can use
    # note, thesetVoice command does not work until after you have list of voices.
    print Mouth.getVoices()
    # The next line will allow you to select which voice we use. The default appears to be "slt"
    Mouth.setVoice("rms")
    # the set the volume that your robot will speak at use the setVolume command, the value is a float, so remember the .0
    Mouth.setVolume(100.0)


#######################################################
#                                                     #
# Speech To Text (STT) services                       #
#                                                     #
#######################################################

# create ear Speech Recognition Service using Sphinxs
# Sphinx is locally run service that does not require access to the internet to work
# The down side is that is doesn't recognise anywhere near as many words.
if UseSphinx == True:
    Ear = Runtime.createAndStart("Ear","Sphinx")
    # start listening for the words we are interested in
    Ear.addComfirmations("yes","correct","ya")
    Ear.addNegations("no","wrong","nope","nah")
    Ear.startListening("hello world|happy monkey|go forward|stop")

# create ear Speech Recognition Service using WebkitSpeechRecognition
# WebkitSpeechRecognition is a very capable service recognising most spoken 
# words with a number of different accents.
# The down side is it does require an Internet access to reach the cloud.
if UseWebKit == True:
    # The Web Kit Speech Recognition (Ear) service is a web based system, 
    # in order to use it we will need to create the WebGui service running first
    # If we haven't already started it, start it now.
    if RunWebGUI == False:
        # But we don't want to start it just yet so we just use the create command
        # GUI in case you didn't know stands for Graphical User Interface.
        # All service are created by the Runtime Service so the command is run from there.
        # It returns an object that is the WebGui service.
        WebGui = Runtime.create("WebGui","WebGui")
        # The next this we need to do is prevent the Web Browser starting up on a page we don't need.
        # by default when the WebGui service is started it will launce the local web browser for a runtime GUI
        # We will prevent this behaveiour by setting the autoStartBrowser to false.
        WebGui.autoStartBrowser(False)
        # Now we have the web browser disabled from auto starting lets start the WebGui service
        # with the startService command
        WebGui.startService()
    # now that we klnow the WebGUI system is up and running
    # We need to create and start the WebKitSpeechRecognition Service
    # As with all service, it is created from the Runtime Service and can be started from there
    Ear = Runtime.start("Ear","WebkitSpeechRecognition")
    # Now that we have the WebGui service and the WebKitSpeechRecognition Service running we can 
    # start the Web Browser sending it to a service page we just created.
    # It is very inportant that the part of the path after the service is the same 
    # name that you give your WebKitSpeechRecognition service in this case Ear
    WebGui.startBrowser("http://localhost:8888/#/service/Ear")
    # Now I'm an English speaker in Australia, so i will set the language to "en-AU"
    # with the setLanguage command.
    # for a full list of supported languages visit: https://cloud.google.com/speech/docs/languages
    Ear.setLanguage("en-AU")
    # If setAutoListen is True, webkitspeech red microphone will auto rearm. 
    # microphone will shutdown too if mouth is activated. 
    # Careful if this is set to True : You cannot control red microphone from webgui anymore
    # You need to control it from SwinGui, or usually from code
    Ear.setAutoListen(True)
    # If setContinuous is False, this speeds up recognition processing 
    # If setContinuous is True, you have some time to speak again, in case of error
    # in this case we will use False
    Ear.setContinuous(False)

# prevent infinite loop - this will suppress the
# recognition when speaking - default behavior
# by attaching an Ear to a Mouth :)
Ear.attach(Mouth)
