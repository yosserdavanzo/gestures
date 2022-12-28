import serial
import string
import json

ARDUINO_CONFIG_FILE = r".vscode\arduino.json"

def getComPort() -> string:
    f = open(ARDUINO_CONFIG_FILE)
    data = json.load(f)
    comPort =  data["port"]
    f.close()
    return comPort

BAUDE_RATE = 115200
PORT = getComPort()

gestureSerial = serial.Serial(
        # Serial Port to read the data from
        port=PORT,
 
        #Rate at which the information is shared to the communication channel
        baudrate = BAUDE_RATE,
   
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
 
       # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
     
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
 
        # Number of serial commands to accept before timing out
        timeout=1
)
