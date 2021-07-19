
REG ADD HKCU\Console /v CodePage /t REG_DWORD /d 0xfde9 /f
REG ADD HKCU\Console /v FaceName /t REG_SZ /d "Lucida Console" /f
@chcp 65001>nul
@echo off
echo ------------------------------------------------------
echo 			Fred_InMoov Batch Launcher 0.1 Nixie - 1.1.500+
echo ------------------------------------------------------
echo KILL JAVA to clean reborn

taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
taskkill.exe /F /IM chrome.exe
if exist %cd%\mrlNeedReinstall del mrlNeedReinstall

echo ------------------------------------------------------
echo Rotate log files for clean no worky

del myrobotlab.log.1 > NUL
move /y myrobotlab.log myrobotlab.log.1

echo "Done."
echo ------------------------------------------------------
COLOR 0F
cls
echo ------------------------------------------------------
echo START MRL AND Fred_InMoov
echo ------------------------------------------------------

REM This is the command to start up the agent jar, specify the memory and run the default InMoov script
REM start the FRED script
REM Let look at this line and break it down a bit.
REM We start the line with the executable "java"
REM the -jar myrobotlab.jar is the name of the java file to be 
REM run by java when it starts.
REM -m 4g tell the java system to allocate 4 Giga bytes of 
REM Random Access Memory (RAM) to the java system.
REM --service python Python is passes to the myrobotlab.jar 
REM program, telling it to sert the Python service and name it python
REM --invoke python execFile ./Fred/Start.py thells the myrobotlab.jar 
REM program to use the python service and execute the file with the 
REM path starting in the current directory look in the sub 
REM directory "Fred" for the file "Start.py"
java -jar myrobotlab.jar -m 4g --service python Python --invoke python execFile ./Fred/Start.py

REM with the older Manitocre version the startup command line is a little bit different.
REM java -jar myrobotlab.jar -m 4g -service python Python -invoke python execFile ./Fred/Start.py
