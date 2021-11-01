# Setup a keypad reader
# Keypad is a 4 x 4 matrix type
KeyCount = 0
LastKeyPress = 0
KeyPad = Runtime.createAndStart("KeyPad","Pcf8574")
# Set four pins as output. 
KeyPad.pinMode(0,"OUTPUT")
KeyPad.pinMode(1,"OUTPUT")
KeyPad.pinMode(2,"OUTPUT")
KeyPad.pinMode(3,"OUTPUT")
KeyPad.pinMode(4,"OUTPUT")
KeyPad.pinMode(5,"OUTPUT")
KeyPad.pinMode(6,"OUTPUT")
KeyPad.pinMode(7,"OUTPUT")
# Set outputs hi or low
KeyPad.write(0,0)
KeyPad.write(1,1)
KeyPad.write(2,1)
KeyPad.write(3,1)
KeyPad.write(4,1)
KeyPad.write(5,1)
KeyPad.write(6,1)
KeyPad.write(7,1)
sleep(1)

def ScanKeyPad(timedata):
    global KeyCount
    global LastKeyPress
    KeyPress = 0
    if KeyCount == 0:
        if KeyPad.read(4) == 0:
            KeyPress = 1
        elif KeyPad.read(5) == 0:
            KeyPress = 2
        elif KeyPad.read(6) == 0:
            KeyPress = 3
        elif KeyPad.read(7) == 0:
            KeyPress = 11
        KeyPad.write(0,1)
        KeyPad.write(1,0)
        KeyPad.write(2,1)
        KeyPad.write(3,1)
        KeyCount = 1
    elif KeyCount == 1:
        if KeyPad.read(4) == 0:
            KeyPress = 4
        elif KeyPad.read(5) == 0:
            KeyPress = 5
        elif KeyPad.read(6) == 0:
            KeyPress = 6
        elif KeyPad.read(7) == 0:
            KeyPress = 12
        KeyPad.write(0,1)
        KeyPad.write(1,1)
        KeyPad.write(2,0)
        KeyPad.write(3,1)
        KeyCount = 2
    elif KeyCount == 2:
        if KeyPad.read(4) == 0:
            KeyPress = 7
        elif KeyPad.read(5) == 0:
            KeyPress = 8
        elif KeyPad.read(6) == 0:
            KeyPress = 9
        elif KeyPad.read(7) == 0:
            KeyPress = 13
        KeyPad.write(0,1)
        KeyPad.write(1,1)
        KeyPad.write(2,1)
        KeyPad.write(3,0)
        KeyCount = 3
    elif KeyCount == 3:
        if KeyPad.read(4) == 0:
            KeyPress = 15
        elif KeyPad.read(5) == 0:
            KeyPress = 10
        elif KeyPad.read(6) == 0:
            KeyPress = 16
        elif KeyPad.read(7) == 0:
            KeyPress = 14
        KeyPad.write(0,0)
        KeyPad.write(1,1)
        KeyPad.write(2,1)
        KeyPad.write(3,1)
        KeyCount = 0
    if KeyPress <> LastKeyPress:
        LastKeyPress = KeyPress
        if KeyPress > 0:
            print ("KeyPress: ", KeyPress)
    
KeyScanTimer = Runtime.createAndStart("KeyScanTimer", "Clock")
KeyScanTimer.addListener("pulse", python.name, "ScanKeyPad")
KeyScanTimer.setInterval(100)
KeyScanTimer.startClock(False)
