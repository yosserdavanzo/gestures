import string
import serial
import time
import os

import json
import csv
import uuid

from src.utils.serialProvider import gestureSerial
from fileConstants import *


class Scraper:
    def __init__(self, folderPath:str,fileNamePrefix:str, dataCount:int = DATA_LENGTH):
        self.HEARTBEAT_FREQ = 10
        self.BACKOFF = 20/1000 # 20 ms as seconds
        self.filePrefix = fileNamePrefix
        self.dataCount = dataCount

        if os.path.isdir(folderPath):
            raise Exception("Scrapper Path is not a folder")
        self.folderPath = folderPath

        print("Flushing Serial...")
        gestureSerial.flush()
        time.sleep(1)
        print("...Flushed!")

        self.calibrate()

    def calibrate(self):
        print("Hold Still!")
        for i in range(5):
            try:
                # throw away data
                _ = gestureSerial.readline().strip().split(b",")
            except:
                print("minor error found, attempting again....")
            time.sleep(.1)
        input("Press [ENTER] to continue")

    def createFileName(self):
        name = self.filePrefix + str(uuid.uuid4())
        return os.path.join( self.folderPath, name)

    def writeSingleFile(self) -> str:
        fileName = self.createFileName()
        with open(fileName, 'x', newline='') as f:
            writ = csv.writer(f, delimiter=",")
            writ.writerow(KEYS)
            for i in range(self.dataCount):
                if i%self.HEARTBEAT_FREQ == 0 : print(i)
                try:
                    data = gestureSerial.readline().strip().split(b",")
                    data_spl = [float(x) for x in data]
                    if len(data_spl) == KEY_COUNT:
                        writ.writerow([time.time(), *data_spl])
                except:
                    print("failed loop")
                    time.sleep(self.BACKOFF)
        return fileName
        
    def writeMultiFile(self, totalFileCount:int):
        rejectStr = '.'

        count = 0
        while count < totalFileCount:
            print(f"\nFiles So Far: {count}\n")
            file = self.writeSingleFile()
            feedback = input(f"Keep the file?\n[{rejectStr}] for No, anything for yes")

            if feedback.find(rejectStr) != -1:
                os.remove(file)
            else:
                count += 1
