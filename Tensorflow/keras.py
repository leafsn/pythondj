# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 11:40
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : keras.py
# @Software: PyCharm
import tensorflow as tf
from tensorflow.keras import layers


print(tf.version)
print(tf.keras.__version__)

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

model.compile(optimizer=tf.train.AdamOptimizer(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])