# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 16:43
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : dian.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np


# 散点
data = {
    'a': np.arange(100),
    'c': np.random.randint(0, 50, 100),
    'd': np.random.randn(5)}

data['b'] = data['a'] + 10 * np.random.randn(100)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data= data)
plt.xlabel('entry a')
plt.ylabel('entry b')

plt.show()




