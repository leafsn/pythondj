# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 10:32
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : artist.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
# ax = fig.add_subplot(2,1,1)

fig.subplots_adjust(top=0.8)
ax1 = fig.add_subplot(211)
ax1.set_ylabel('volts')
ax1.set_title('a sine wave')

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax1.plot(t, s, color='blue', lw=2)


np.random.seed(19680801)
ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])

n, bins, patches = ax2.hist(np.random.randn(1000), 50,
                            facecolor='yellow', edgecolor='yellow')

ax2.set_xlabel('time(s)')




# 删除一行
# del ax.lines[0]

xtext = ax1.set_xlabel('my xdata')
ytext = ax1.set_ylabel('my ydata')

fig, ax = plt.subplots()
axis = ax.xaxis
axis.get_ticklocs()
axis.get_ticklines(minor=True)

fig = plt.figure()
rect = fig.patch
rect .set_facecolor('lightgoldenrodyellow')

ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')

for label in ax1.xaxis.get_ticklabels():
    label.set_color('red')
    label.set_rotation(45)
    label.set_fontsize(16)

for line in ax1.yaxis.get_ticklines():
    line.set_color('green')
    line.set_markersize(25)
    line.set_markeredgewidth(3)




plt.show()






