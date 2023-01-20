import string
import serial
import time
import os

import json
import csv
from src.utils.serialProvider import gestureSerial
from fileConstants import KEYS

HEARTBEAT_FREQ = 10
DURATION=500
BACKOFF = 20/1000 # 20 ms as seconds
FILE_NAME = 'temp.csv'

print("Flushing Serial...")
gestureSerial.flush()
time.sleep(1)
print("...Flushed!")

if os.path.isfile(FILE_NAME):
    os.remove(FILE_NAME)
    print("Deleted old temp file")

print("Hold Still!")
for i in range(5):
    try:
        data = gestureSerial.readline().strip().split(b",")
    except:
        print("minor error found, attempting again....")
    time.sleep(.1)
input("Press [ENTER] to continue")

with open(FILE_NAME, 'x', newline='') as f:
    writ = csv.writer(f, delimiter=",")
    writ.writerow(KEYS)
    for i in range(DURATION):
        if i%HEARTBEAT_FREQ == 0 : print(i)
        try:
            data = gestureSerial.readline().strip().split(b",")
            data_spl = [float(x) for x in data]
            if len(data_spl)>5:
                writ.writerow([time.time(), *data_spl])
        except:
            print("failed loop")
            time.sleep(BACKOFF)
