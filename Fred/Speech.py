#############################################################
# Program Code for Fred Inmoov                              #
# Of the Cyber_One YouTube Channel                          #
# https://www.youtube.com/cyber_one                         #
#                                                           #
# This is version 5                                         #
# Divided up into sub programs                              #
#                                                           #
# Running on MyRobotLab (MRL) http://myrobotlab.org/        #
# Fred in a modified Inmmov robot, you can find all the     #
# origonal files on the Inmoov web site. http://inmoov.fr/  #
#                                                           #
# Speech.py                                                 #
# This file is to handel all the speech services            #
# Text To Speech (TTS)                                      #
# Speech To Text (STT)                                      #
#                                                           #
#############################################################
print "Creating the Text to Speech and Speech to Text functions"
# As a general rule, we define the TTS services as the mouth
# and STT services as the Ear :-)
# Load the configuration for the IO devices.
execfile(RuningFolder+'/1_Configuration/B_Speech_Config.py')

#######################################################
#                                                     #
# Sanity Checks                                       #
#                                                     #
#######################################################
# We can only have one TTS and one STT selected at the same
# time, so we will disable secondary ones if there are more
# than one selected.

# Lets start with TTS
if UseMarySpeech and UseMimicSpeech:
    UseMimicSpeech = False
if (UseMarySpeech or UseMimicSpeech) and UseEspeak:
    UseEspeak = False
# You can't use eSpeak on Windows in MRL (there is a version
# of eSpeak for Windows, but it is not supported in MRL.
if PlatformStructure.isWindows():
    UseEspeak = False
    
# Now lets check the STT services
if UseSphinx and UseWebKit:
    UseWebKit = False

#######################################################
#                                                     #
# Text To Speech (TTS) services                       #
#                                                     #
#######################################################
#
# Notes for when running on the Raspberry Pi.
#
# When using Java x OpenJDK, you may find the audio from the
# Text To Speech coming out the HDMI port instead of the
# selected 3.5mm Audio socket on the side of the Raspberry Pi.
# This is caused by Pulse Audio not following the requested
# settings and routing the audio from the Java apps to a
# different output.
# The solution is to edit the Java sound.properties file.
# When insetting up Java 11
# sudo nano /etc/java-11-openjdk/sound.properties
# You will need to add in the following lines into the config:
# javax.sound.sampled.Clip=com.sun.media.sound.DirectAudioDeviceProvider
# javax.sound.sampled.Port=com.sun.media.sound.PortMixerProvider
# javax.sound.sampled.SourceDataLine=com.sun.media.sound.DirectAudioDeviceProvider
# javax.sound.sampled.TargetDataLine=com.sun.media.sound.DirectAudioDeviceProvider
#
# Make sure you don't have the # in front of the lines.
# Reboot the Raspberry Pi.
# sudo reboot
# Make sure you selected the 3.5mm Audio jack as your output
# device:
# alsamixer
# press F6 to select the sound card you want as the output.
# Select 1 Headphones.
# now change into your MRL directory and start MRL the way you
# normally would.

# MarySpeech TTS
if UseMarySpeech == True:
    Mouth = Runtime.createAndStart("Mouth", "MarySpeech")
    print Mouth.getVoices()
    # The next line will allow you to select which voice we use. 
    # The default appears to be "slt"
    Mouth.setVoice("cmu-bdl-hsmm")
    Mouth.setVolume(100.0)

# Most of the other speech TTS engines all use the same service.
# MimicSpeech TTS
# before you can use this on the Raspberry Pi, 
# you first need to install it.
# By default this is not installed for the ARM based computer 
# like the Raspberry Pi, for detailed instructions on 
# installing this please watch my video
# https://youtu.be/OSbqlRWYBkQ
# I have also included instructions in the GitHub where this
# program is maintained

# When running MRL on the Windows Platform, MimicSpeech is
# included as part of the distribution, as such there is a
# service for it.  In Manticore, there was a command to set
# the path for the Linux version, however this was removed
# in the Nixie version, you now use the localSpeach for the
# Mimic speech in Manticore
if UseMimicSpeech and (PlatformStructure.isWindows() or (MRL == "Manticore")):
    # start the service
    Mouth = Runtime.start('Mouth','MimicSpeech')
    if PlatformStructure.isLinux():
        Mouth.setMimicExecutable("~/mimic1/mimic")
    # the next command wil get a list of voices we can use
    # note, thesetVoice command does not work until after you have list of voices.
    print Mouth.getVoices()
    # The next line will allow you to select which voice we use. The default appears to be "slt"
    Mouth.setVoice("rms")
    # the set the volume that your robot will speak at use the setVolume command, the value is a float, so remember the .0
    Mouth.setVolume(100.0)

# LocalSpeech TTS
# In windows there is only one option for local speech,
# that is TTS.exe located in the MRL\TTS directory.
# This is a suprisingly good TTS program for Windows,
# it is not however available for Mac or Linux.
# For Mac and Linux, we have a few other options :-)

# Espeak TTS
# before you can use this on the Raspberry Pi, 
# you first need to install it.
# By default this is not installed for the ARM based 
# computer like the Raspberry Pi.
# This is very easy with the command 
# "sudo apt-get install espeak"

# LocalSpeach TTS in Linux.
# By default this is not installed, but it is easy to install.
# "sudo apt-get install festival"

if UseEspeak or UseLocalSpeech or (UseMimicSpeech and MRL == "Nixie" and PlatformStructure.isLinux()):
    # start the service
    Mouth = Runtime.start('Mouth','LocalSpeech')
    # next if not running LocalSpeech we need to tell the 
    # service where to find our executable and setup a 
    # template so the MRL knows how to talk to the 
    # Speech engine
    if not UseLocalSpeech:
        if UseEspeak:
            Mouth.setTtsPath("/usr/bin/espeak")
            Mouth.setTtsCommand("espeak \"{text}\" -w {filename})
        elif UseMimicSpeech:
            Mouth.setTtsPath("~/mimic1/mimic")
            Mouth.setTtsCommand("mimic -t \"{text}\" -o \"{filename}\"")
    # the next command wil get a list of voices we can use
    # note, thesetVoice command does not work until after you have list of voices.
    print Mouth.getVoices()
    # The next line will allow you to select which voice we use. The default appears to be "slt"
    Mouth.setVoice("rms")
    # the set the volume that your robot will speak at use the setVolume command, the value is a float, so remember the .0
    Mouth.setVolume(100.0)

    #echo \"{text}\" | text2wave -o {filename}

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
    #if MRL == "Nixie":
    #    Ear.setcurrentWebkitLanguage(WebkitLanguage)
    #else:
    #    Ear.setLanguage(WebkitLanguage)
    if WebKitWakeWord == "":
        WebKitWakeWord = RobotsName
    # If setAutoListen is True, webkitspeech red microphone will auto rearm. 
    # microphone will shutdown too if mouth is activated. 
    # Careful if this is set to True : You cannot control red microphone from webgui anymore
    # You need to control it from SwinGui, or usually from code
    Ear.setAutoListen(True)
    # If setContinuous is False, this speeds up recognition processing 
    # If setContinuous is True, you have some time to speak again, in case of error
    # in this case we will use False
    Ear.setContinuous(False)
    if MRL == "Nixie":
        Ear.setWakeWord(WebKitWakeWord)

# prevent infinite loop - this will suppress the
# recognition when speaking - default behavior
# by attaching an Ear to a Mouth :-)
if (UseSphinx or UseWebKit) and (UseMarySpeech or UseMimicSpeech or UseEspeak):
    Ear.attach(Mouth)
