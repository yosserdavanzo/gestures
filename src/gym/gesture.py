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

df = pd.read_csv(FILE_NAME, names = standardKeys, nrows=400)


x_train = [np.array(df)]
y_train = [[1,0]]

x_val = [np.array(df)]
y_val = [[1,0]]


print(x_train[0].shape)
# print(y_train[0].shape())

# data_dim = 3
# timestep = len(x_train[0])
### End reader



## Simplest LSTM + Dense
gestureReader = Sequential()
gestureReader.add(LSTM(5, input_shape=(4,400)))
gestureReader.add(Dense(2, activation="sigmoid"))
gestureReader.compile(loss=tf.keras.losses.CategoricalCrossentropy(), optimizer='adam', metrics=['accuracy'])

a = tf.random.normal([standardCount, 400])
a = tf.reshape(a, [1, standardCount, 400])
# b = tf.random.normal([timestep, data_dim+1])
l = [1,0]
l = tf.reshape(l, [1, 2, 1])

data = tf.data.Dataset.from_tensor_slices((a, l))

gestureReader.fit(data, epochs=2)


# d = tf.reshape(a, [1, timestep, data_dim+1])
# y = gestureReader([d])
# print(y)

# Works
# a = tf.random.normal([timestep, data_dim+1])
# a = tf.reshape(a, [1, timestep, data_dim+1])
# b = gestureReader([a])

# print("woop")
# print(a)

# print(b)


print(gestureReader.summary())

# history = gestureReader.fit(
#     a,
#     y_train,
#     batch_size = 1,
#     epochs = 2,
#     validation_data = (a, y_val)
# )




# print(gestureReader.summary())