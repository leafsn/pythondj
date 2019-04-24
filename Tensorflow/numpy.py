# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 13:53
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : numpy.py
# @Software: PyCharm

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
model = tf.keras.Sequential()
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

layers.Dense(64, activation = 'sigmoid')
layers.Dense(64, activation = tf.sigmoid)
layers.Dense(64, kernel_regularizer = tf.keras.regularizers.l2(0.01))
layers.Dense(64, bias_regularizer=tf.keras.regularizers.l2(0.01))
layers.Dense(64, kernel_initializer='orthogonal')
layers.Dense(64, bias_initializer=tf.keras.initializers.constant(2.0))

model = tf.keras.Sequential([
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax'),
])
data = np.random.random((100, 32))
labels = np.random.random((100, 10))

model.fit(data, labels, epochs=10, batch_size=32)