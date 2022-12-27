import string
import serial
import time

import json
import csv

def getComPort() -> string:
    f = open(ARDUINO_CONFIG_FILE)
    data = json.load(f)
    comPort =  data["port"]
    f.close()
    return comPort

ARDUINO_CONFIG_FILE = r".vscode\arduino.json"
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

HEARTBEAT_FREQ = 50
looper = 0
print("Flushing Serial...")
ser.flush()
print("...Flushed!")

with open('temp.csv', 'a', newline='') as f:
    writ = csv.writer(f, delimiter=",")
    writ.writerow(["t", "aa.x", "aa.y", "aa.z", "aReal.x", "aReal.y", "aReal.z"])
    for i in range(200):
        if i%HEARTBEAT_FREQ == 0 : print(i)
        try:
            data = ser.readline().strip().split(b",")
            data_spl = [float(x) for x in data]
            if len(data_spl)>5:
                writ.writerow([time.time(), *data_spl])
            else:
                print("failed loop")
        except:
            time.sleep(.06)
