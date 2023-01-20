import string
import serial
import json
import time

import matplotlib.pyplot as plt
from fileConstants import *

ARDUINO_CONFIG_FILE = r".vscode\arduino.json" 

def getComPort() -> string:
    f = open(ARDUINO_CONFIG_FILE)
    data = json.load(f)
    comPort =  data["port"]
    f.close()
    return comPort

BAUDE_RATE = 115200
PORT = getComPort()

ser = serial.Serial(
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

print("Hold Still!")
for i in range(5):
    try:
        data = ser.readline().strip().split(b",")
    except:
        print("minor error found, attempting again....")
    time.sleep(.1)

input("Press [SPACE] to continue")

total = 0
passes = 0
times = []
previous = time.time()
while total < DATA_LENGTH:
    total += 1
    try:
        print("a")
        data = ser.readline().strip().split(b",")
        print("b")
        now = time.time()
        times.append(now - previous)
        previous = now
        passes += 1
    except:
        print("FFFFFFFFFFailure")

plt.plot(range(len(times)), times)
plt.show()

print( f"Success Rate of {passes / total}")