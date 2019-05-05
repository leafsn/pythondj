# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 11:29
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : yongli.py
# @Software: PyCharm
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

# 红色条目
# red_patch = mpatches.Patch(color='red', label='The red data')
# plt.legend(handles=[red_patch])

# 带标记的蓝色星星
blue_line = mlines.Line2D([], [], color='blue', marker='*',
                          markersize=15, label='Blue stars')
plt.legend(handles=[blue_line])

plt.subplot(211)
plt.plot([1,2,3], label='test1')
plt.plot([3,2,1], label='test2')

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode='expand', borderaxespad=0.)

plt.subplot(223)
plt.plot([1,2,3], label='test1')
plt.plot([3,2,1], label='test2')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

from matplotlib.legend_handler import HandlerLine2D

line1, = plt.plot([1, 2, 3], label='Line 1', marker='o', linestyle='--')
line2, = plt.plot([3, 2, 1], label='Line 2', marker='o', linewidth=4)


first_legend = plt.legend(handles=[line1], loc='upper right')

plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})

ax = plt.gca().add_artist(first_legend)

plt.legend(handles=[line2], loc='lower right')

z = np.random.randn(10)
red_dot, = plt.plot(z, 'ro', markersize=15)
white_cross, = plt.plot(z[:5], 'w+', markeredgewidth=3, markersize=15)

plt.legend([red_dot, (red_dot, white_cross)], ['Attr A', 'Attr A+B'])

plt.show()