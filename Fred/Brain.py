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
# Brain.py
# This is where the AI functions will live.
# In the short term, we will use ProgramAB.
#                                                     #
#######################################################
print "Creating the AI"
# need to set this up using the ProgramAB service to start with.
# later we could add other things like a neural network interpreter :-)

# create a ProgramAB service and start a session
# ProgramAB is the Program that runs the Alice Bot Artificial Inteligence Mark Languale (AIML)
Brain = Runtime.start("Brain", "ProgramAB")

# We can setup the ProgramAB to work with different people
# to do that, we need to start the session for the individual user.
# At this point in time, it only support one user session at a time.
Brain.startSession("Builder")

# create a route which sends published Responses to the
# mouth.speak(String) method, The addTextListener is sort of the internal way of doing this :-)
Brain.addTextListener(Mouth)

# Next lets create a route that sends the speech our 
# robot has heard to the ProgramAB, but only if we satarted one of the STT services. :-)
if UseSphinx == True or UseWebKit == True:
    Ear.addTextListener(Brain)

