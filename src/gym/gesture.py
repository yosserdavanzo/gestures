import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Dense, LSTM, Input

from src.gym.dataLoader import getDataAndLabels
from src.dataCollection.fileConstants import *

import random
random.seed(420)

train_path = r"C:\Users\ydava\gestures\data\train"

x_train, y_train = getDataAndLabels(train_path)

print(x_train.shape)
print(y_train.shape)
## Simplest LSTM + Dense
gestureReader = Sequential()
gestureReader.add(LSTM(2, input_shape=(DATA_LENGTH, STANDARD_KEY_COUNT)))
gestureReader.add(Dense(2, activation="sigmoid"))
gestureReader.compile(loss=tf.keras.losses.CategoricalCrossentropy(), optimizer='adam', metrics=['accuracy'])

history = gestureReader.fit(x_train, y_train, epochs=1)

print(gestureReader.call( tf.reshape(x_train[0], [1, DATA_LENGTH, STANDARD_KEY_COUNT] )))