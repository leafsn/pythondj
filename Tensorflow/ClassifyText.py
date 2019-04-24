# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 17:07
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : ClassifyText.py
# @Software: PyCharm

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras
import numpy as np

print(tf.__version__)

imdb = keras.datasets.imdb
(train_data, train_labels),(test_data, test_labels) = imdb.load_data(num_words=10000)

# print("Training entries: {}, labels: {}".format(len(train_data), len(train_labels)))