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
# OpenCV.py                                                  #
# This file is to give our robots the ability to see         #
# OpenCV stands for Open Computer Vision.
#                                                            #
##############################################################
import math
import time
import random

print "Creating the various life simulation functions"
# Load the configuration for the Open Computer Vision.
execfile(RuningFolder+'/1_Configuration/D_OpenCV_Config.py')

if EnableOpenCV:
    opencv = Runtime.start("opencv","OpenCV")
    # call back - all data from opencv will come back to 
    # this method
    def onOpenCVData(data):
        # check for a bounding box
        if data.getBoundingBoxArray() != None:
            for box in data.getBoundingBoxArray():
                print("bounding box:", box.x, box.y, box.width, box.height, (box.width/2)+box.x)
            print("----")
    python.subscribe("opencv", "publishOpenCVData")
    opencv.setCameraIndex(0)
    opencv.capture()
    opencv.addFilter("FaceDetect")
    opencv.addOptionFindBiggestObject(
    opencv.setDisplayFilter("FaceDetect")
