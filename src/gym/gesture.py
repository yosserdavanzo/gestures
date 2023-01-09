import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Dense, LSTM, Input
from tensorflow.keras.preprocessing import sequence


import random
random.seed(420)

### Reader

import os
import pandas as pd
import numpy as np

FILE_NAME = 'temp.csv'
keys = ["t","aa.x","aa.y","aa.z","aReal.x","aReal.y","aReal.z"]
standardKeys = ["t","aa.x","aa.y","aa.z"]
standardCount = len(standardKeys)

if not os.path.isfile(FILE_NAME):
    raise Exception("Missing Data file!")

df = pd.read_csv(FILE_NAME, names = standardKeys, nrows=400, skiprows=1)

x_train = np.array(df)
y_train = [1,0]

x_val = np.array(df)
y_val = [1,0]


x_train = tf.reshape(x_train, [1, 400, standardCount])
y_train = tf.reshape(y_train, [1, 2])

### End reader


## Simplest LSTM + Dense
gestureReader = Sequential()
gestureReader.add(LSTM(2, input_shape=(400, 4)))
gestureReader.add(Dense(2, activation="sigmoid"))
gestureReader.compile(loss=tf.keras.losses.CategoricalCrossentropy(), optimizer='adam', metrics=['accuracy'])

gestureReader.fit(x_train, y_train, epochs=2)


# print(gestureReader.summary())

# history = gestureReader.fit(
#     a,
#     y_train,
#     batch_size = 1,
#     epochs = 2,
#     validation_data = (a, y_val)
# )




# print(gestureReader.summary())