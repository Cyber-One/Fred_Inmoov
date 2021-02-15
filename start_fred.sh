#!/bin/bash

#############################################################
# Fred Unix Start Script 
# Usage:  ./start_fred.sh
# This will launch MyRobotLab and run the Fred/Start.py 
# default startup script
#############################################################

echo "------------------------------------------------------"
echo "			FRED LAUNCHER"
echo "------------------------------------------------------"
echo "Rotate Log files for clean no worky logs"
echo "------------------------------------------------------"
rm myrobotlab.log.1
mv myrobotlab.log myrobotlab.log.1
echo "Done."
echo "------------------------------------------------------"
echo "START MRL & FRED"
echo "------------------------------------------------------"
# start the FRED script
java -jar myrobotlab.jar --service python Python --invoke python execFile ./Fred/Start.py