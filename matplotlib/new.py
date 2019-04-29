# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 14:43
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : new.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
import pandas

fig = plt.figure()
fig.suptitle('No axes on this figure')

fig, ax_lst = plt.subplots(2,2)

a = pandas.DataFrame(np.random.rand(4,5), columns=list('abcde'))
a_asndarray = a.values

b = np.matrix([[1,2],[3,4]])
b_asarray = np.asarray(b)

x = np.linspace(0,2,100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratoc')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple Plot')

plt.legend()
plt.show()

x = np.arange(0,10,0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()

## 绘图函数
def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4,100)
fig, ax = plt.subplots(1,1)
my_plotter(ax, data1, data2, {'marker':'x'})

fig, (ax1, ax2) = plt.subplots(1,2)
my_plotter(ax1, data1, data2, {'marker':'x'})
my_plotter(ax2, data3, data4, {'marker':'o'})

import matplotlib as mpl

y = np.random.rand(100000)
y[50000:] *= 2
y[np.logspace(1,np.log10(50000),400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['path.simplify_threshold'] = 0.0
plt.plot(y)
plt.show()

mpl.rcParams['path.simplify_threshold'] = 1.0
plt.plot(y)
plt.show()


