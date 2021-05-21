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
# 6_Life_Functions/7_NeoPixel_Control.py                      #
# This file is to Simulate life movements associated with    #
# the body of the robot                                      #
#                                                            #
##############################################################

print '6_Life_Functions/7_NeoPixel_Control.py Still to be programmed'

if EnableStomachNeoPixel:
    if StomachNeoPixelMode == 0:
        for Pixel in range(len(NeoPixelDiagConfig)):
            if NeoPixelDiagConfig[Pixel][0] == 0:       # Not Used
                StomachNeoPixel.setPixel(pixel, 0, 0, 0)
            elif NeoPixelDiagConfig[Pixel][0] == 1:     # Left UltraSonic Range
                if LastLeftPing < NeoPixelDiagConfig[Pixel][1]:
                    StomachNeoPixel.setPixel(pixel, NeoPixelDiagConfig[Pixel][2], NeoPixelDiagConfig[Pixel][3], NeoPixelDiagConfig[Pixel][4])
                else:
                    StomachNeoPixel.setPixel(pixel, NeoPixelDiagConfig[Pixel][5], NeoPixelDiagConfig[Pixel][6], NeoPixelDiagConfig[Pixel][7])
            elif NeoPixelDiagConfig[Pixel][0] == 2:     # Right UltraSonic Range
                if LastRightPing < NeoPixelDiagConfig[Pixel][1]:
                    StomachNeoPixel.setPixel(pixel, NeoPixelDiagConfig[Pixel][2], NeoPixelDiagConfig[Pixel][3], NeoPixelDiagConfig[Pixel][4])
                else:
                    StomachNeoPixel.setPixel(pixel, NeoPixelDiagConfig[Pixel][5], NeoPixelDiagConfig[Pixel][6], NeoPixelDiagConfig[Pixel][7])
            elif NeoPixelDiagConfig[Pixel][0] == 3:     # PIR Detection
                if not PIRstate:
                    StomachNeoPixel.setPixel(pixel, NeoPixelDiagConfig[Pixel][2], NeoPixelDiagConfig[Pixel][3], NeoPixelDiagConfig[Pixel][4])
                else:
                    StomachNeoPixel.setPixel(pixel, NeoPixelDiagConfig[Pixel][5], NeoPixelDiagConfig[Pixel][6], NeoPixelDiagConfig[Pixel][7])
            elif NeoPixelDiagConfig[Pixel][0] == 4:     # Battery Voltage
                if BatteryLevel < NeoPixelDiagConfig[Pixel][1]:
                    StomachNeoPixel.setPixel(pixel, NeoPixelDiagConfig[Pixel][2], NeoPixelDiagConfig[Pixel][3], NeoPixelDiagConfig[Pixel][4])
                else:
                    StomachNeoPixel.setPixel(pixel, NeoPixelDiagConfig[Pixel][5], NeoPixelDiagConfig[Pixel][6], NeoPixelDiagConfig[Pixel][7])
    else:
        StomachNeoPixel.setAnimation("Rainbow Cycle", 255, 0, 0, 1) #running Theater Chase with color red at full speed


    #neopixel.animationStop()
#Animations;
#"Color Wipe"
#"Larson Scanner"
#"Theater Chase"
#"Theater Chase Rainbow"
#"Rainbow"
#"Rainbow Cycle"
#"Flash Random"
#"Ironman"
 
#speed: 1-65535   1=full speed, 2=2x slower than 1, 10=10x slower than 1
#starting a animation
#neopixel.setAnimation("Animation Name", red, green, blue, speed)
#run an animation with python script

#turn off all the pixels
#for pixel in range (1,neopixel.numPixel + 1):
#  neopixel.setPixel(pixel, 0, 0, 0)  #setPixel(pixel, red, green, blue)
#neopixel.writeMatrix() #send the pixel data to the Neopixel hardware 
#for loop in range(0,10): #do 10 loop
#  for pixel in range(1, neopixel.numPixel +1):
#    neopixel.setPixel(pixel, 255, 0, 0) #set the pixel to red
#    neopixel.writeMatrix()
#    sleep(0.03) #give a bit of delay before next step
#    neopixel.setPixel(pixel, 0, 0, 0) #turn off the pixel
#neopixel.writeMatrix()
