# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 14:48
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : Tensorflow.Tensorflow
# @Software: PyCharm
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

### 导入时尚MNIST数据集
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_lables), (test_images, test_labels) = fashion_mnist.load_data()

class_name = [
    'T-shirt/top', 'Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot'
]
# train_images.shape
# len(train_lables)
# train_lables
# test_images.shape
# len(test_labels)

# 检查像素大小
# plt.figure()
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

# 缩小像素0-1之间
train_images = train_images / 255.0
test_images = test_images / 255.0

# 检查格式是否正确，输出前25个
# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary)
#     plt.xlabel(class_name[train_lables[i]])
# plt.show()

model = keras.Sequential([
    keras.layers.Flatten(input_shape =(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_lables, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('\nTest accuracy: ', test_acc)

# 预测一些图像
predictions = model.predict(test_images)
print(predictions[0])


# 预测自信度最高的
print(np.argmax(predictions[0]))

print(test_labels[0])

def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    prediced_label = np.argmax(predictions_array)
    if prediced_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_name[prediced_label],
                                         100*np.max(predictions_array),
                                         class_name[true_label]),
                                        color = color)
def plot_value_array(i, predictions_arry, true_label):
    predictions_arry, true_label = predictions_arry[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_arry, color="#777777")
    plt.ylim([0,1])
    predicted_label = np.argmax(predictions_arry)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

# 第0张图片的预测
# i = 0
# plt.figure(figsize=(6, 3))
# plt.subplot(1,2,1)
# plot_image(i, predictions, test_labels, test_images)
# plt.subplot(1, 2, 2)
# plot_value_array(i, predictions, test_labels)
# plt.show()
#
# i = 12
# plt.figure(figsize=(6, 3))
# plt.subplot(1, 2, 1)
# plot_image(i, predictions, test_labels, test_images)
# plt.subplot(1, 2, 2)
# plot_value_array(i, predictions, test_labels)
# plt.show()
#
# num_rows = 5
# num_cols = 3
# num_images = num_rows * num_cols
# plt.figure(figsize=(2*2*num_cols, 2*num_rows))
# for i in range(num_images):
#     plt.subplot(num_rows, 2*num_cols, 2*i+1)
#     plot_image(i, predictions, test_labels, test_images)
#     plt.subplot(num_rows, 2*num_cols, 2*i+2)
#     plot_value_array(i, predictions, test_labels)
# plt.show()

img = test_images[0]
print(img.shape)

#添加到批处理列表中
img = (np.expand_dims(img, 0))
print(img.shape)

predictions_single = model.predict(img)
print(predictions_single)

plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_name, rotation=45)

np.argmax(predictions_single[0])