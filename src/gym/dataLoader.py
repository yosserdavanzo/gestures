import numpy as np
import pandas as pd
import os
import tensorflow as tf

from src.dataCollection.fileConstants import *


def loadSingleFile(file):
    df = pd.read_csv(file, names = STANDARD_KEYS, nrows=DATA_LENGTH, skiprows=1)
    x_train = np.array(df)
    return tf.reshape(x_train, [1, DATA_LENGTH, STANDARD_KEY_COUNT])

def getDataAndLabels(folderPath:str) -> tuple:
    if not os.path.isdir(folderPath):
        raise Exception("Invalid Folder Path!")

    # Hack around initializing the shape of _out
    # make the first example zeros, labeled as noise
    x_out = tf.zeros(shape=(1, DATA_LENGTH, STANDARD_KEY_COUNT))
    y_out = tf.reshape(NOISE_FILE_LABEL, (1, COMMAND_COUNT))

    root, _dir, files = next(os.walk(folderPath))
    for file in files:
        dataFile = os.path.join(root, file)
        if dataFile.startswith(NOISE_FILE_PREFIX):
            tf.concat( [x_out, loadSingleFile(file)], 0)
            tf.concat( [y_out, NOISE_FILE_LABEL])
        elif dataFile.startswith(FOCUS_FILE_PREFIX):
            tf.concat( [x_out, loadSingleFile(file)], 0)
            tf.concat( [y_out, FOCUS_FILE_LABEL])

    return (x_out, y_out)