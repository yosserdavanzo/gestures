import serial
import struct
import time

import csv

BAUDE_RATE = 115200
PORT = 'COM3'

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
ser.flush()
for i in range(200):
    if i%HEARTBEAT_FREQ == 0 : print(i)

    with open('temp.csv', 'a', newline='') as f:
        writ = csv.writer(f, delimiter=",")
        try:
            data = ser.readline().strip().split(b",")
            data_spl = [float(x) for x in data]
            if len(data_spl)>5:
                writ.writerow([time.time(), *data_spl])
            else:
                print("failed loop")
        except:
            time.sleep(.06)
