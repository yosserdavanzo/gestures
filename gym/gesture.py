import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Dense, LSTM, Input
from tensorflow.keras.preprocessing import sequence

import random

random.seed(420)

data_dim = 3
timestep = 10

## Simplest LSTM + Dense
gestureReader = Sequential()
gestureReader.add(LSTM(10, input_shape=(timestep, data_dim)))
gestureReader.add(Dense(3, activation="sigmoid"))
gestureReader.compile(loss='...', optimizer='adam', metrics=['accuracy'])



print(gestureReader.summary())