import string
import serial
import time
import os

import json
import csv
# from ..utils.serialProvider import ser
# # import utils.serialProvider as ser

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

HEARTBEAT_FREQ = 10
DURATION=500
BACKOFF = 20/1000 # 20 ms as seconds
FILE_NAME = 'temp.csv'

print("Flushing Serial...")
ser.flush()
time.sleep(1)
print("...Flushed!")

if os.path.isfile(FILE_NAME):
    os.remove(FILE_NAME)
    print("Deleted old temp file")

print("Hold Still!")
for i in range(5):
    try:
        data = ser.readline().strip().split(b",")
    except:
        print("minor error found, attempting again....")
    time.sleep(.1)
input("Press [ENTER] to continue")

with open(FILE_NAME, 'x', newline='') as f:
    writ = csv.writer(f, delimiter=",")
    writ.writerow(["t", "aa.x", "aa.y", "aa.z", "aReal.x", "aReal.y", "aReal.z"])
    for i in range(DURATION):
        if i%HEARTBEAT_FREQ == 0 : print(i)
        try:
            data = ser.readline().strip().split(b",")
            data_spl = [float(x) for x in data]
            if len(data_spl)>5:
                writ.writerow([time.time(), *data_spl])
        except:
            print("failed loop")
            time.sleep(BACKOFF)
