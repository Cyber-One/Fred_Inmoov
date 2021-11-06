# Setup a keypad reader
# Keypad is a 4 x 4 matrix type

# Before we start we need an I2C bus to connect to.
# This could be via a Raspberry Pi or an Arduino
raspi = Runtime.start("raspi","RasPi")
#arduino = Runtime.start("arduino","Arduino")
#arduino.setBoardMega()
#arduino.connect("COM3")


KeyColumn = 0
LastKeyPress = 0
KeyPad = Runtime.start("KeyPad","Pcf8574")
# Before we can use this, 
# we need to configure the I2C Bus 
#KeyPad.setBus("1")
# and address then connect it.
#KeyPad.setAddress("0x20")
#KeyPad.attachI2CController(raspi)
KeyPad.attach(raspi, "1", "0x20")
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
    global KeyColumn
    global LastKeyPress
    KeyPress = 0
    if KeyColumn == 0:
        if KeyPad.read(4) == 0:
            KeyPress = 14   # "D"
        elif KeyPad.read(5) == 0:
            KeyPress = 13   # "C"
        elif KeyPad.read(6) == 0:
            KeyPress = 12   # "B"
        elif KeyPad.read(7) == 0:
            KeyPress = 11   # "A"
        KeyPad.write(0,1)
        KeyPad.write(1,0)
        KeyPad.write(2,1)
        KeyPad.write(3,1)
        KeyColumn = 1
    elif KeyColumn == 1:
        if KeyPad.read(4) == 0:
            KeyPress = 16 # "#"
        elif KeyPad.read(5) == 0:
            KeyPress = 9 # "9"
        elif KeyPad.read(6) == 0:
            KeyPress = 6 # "6"
        elif KeyPad.read(7) == 0:
            KeyPress = 3    # "3"
        KeyPad.write(0,1)
        KeyPad.write(1,1)
        KeyPad.write(2,0)
        KeyPad.write(3,1)
        KeyColumn = 2
    elif KeyColumn == 2:
        if KeyPad.read(4) == 0:
            KeyPress = 10   # "0"
        elif KeyPad.read(5) == 0:
            KeyPress = 8    # "8"
        elif KeyPad.read(6) == 0:
            KeyPress = 5    # "5"
        elif KeyPad.read(7) == 0:
            KeyPress = 2
        KeyPad.write(0,1)
        KeyPad.write(1,1)
        KeyPad.write(2,1)
        KeyPad.write(3,0)
        KeyColumn = 3
    elif KeyColumn == 3:
        if KeyPad.read(4) == 0:
            KeyPress = 15   # "*"
        elif KeyPad.read(5) == 0:
            KeyPress = 7    # "7"
        elif KeyPad.read(6) == 0:
            KeyPress = 4    # "4"
        elif KeyPad.read(7) == 0:
            KeyPress = 1    # "1"
        KeyPad.write(0,0)
        KeyPad.write(1,1)
        KeyPad.write(2,1)
        KeyPad.write(3,1)
        KeyColumn = 0
    if KeyPress <> LastKeyPress:
        LastKeyPress = KeyPress
        if KeyPress > 0:
            print ("KeyPress: ", KeyPress)
    
KeyScanTimer = Runtime.start("KeyScanTimer", "Clock")
KeyScanTimer.addListener("pulse", python.name, "ScanKeyPad")
KeyScanTimer.setInterval(100)
KeyScanTimer.startClock(False)
