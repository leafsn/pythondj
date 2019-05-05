# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 13:55
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : plt.py
# @Software: PyCharm
from matplotlib import gridspec

import  matplotlib.pyplot as plt

plt.figure()

# figure分为三行三列面去的第一个子图的句柄， 第一个子图的跨度是一行三列，起点是表格(0,0)
ax1 = plt.subplot2grid((3,3), (0,0), colspan = 3, rowspan = 1)
ax1.plot([0, 1], [0, 1])
ax1.set_title('Test')

ax2 = plt.subplot2grid((3,3), (1,0), colspan = 2, rowspan = 1)
ax2.plot([0, 1], [0, 1])

ax3 = plt.subplot2grid((3,3), (1,2), colspan = 1, rowspan = 1)
ax2.plot([0, 1], [0, 1])

ax4 = plt.subplot2grid((3,3), (2,0), colspan = 3, rowspan = 1)
ax4.plot([0, 1], [0, 1])

plt.show()


plt.figure()

# 分割figure
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, 0:2])
ax3 = plt.subplot(gs[1, 2])
ax4 = plt.subplot(gs[2, :])

# 绘制图像
ax1.plot([0,4], [0,4])
ax1.set_title('Test')

ax2.plot([1,4], [0,3])
ax3.plot([1,6], [2,7])
ax4.plot([1,3], [0,2])

plt.show()



