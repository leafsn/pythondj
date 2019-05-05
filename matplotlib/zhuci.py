# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 14:26
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : zhuci.py
# @Software: PyCharm\

import numpy as np
import  matplotlib.pyplot as plt

# 定义数据
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1

# 定义figure
fig, ax1 = plt.subplots()

# 得到x1的对称轴
ax2 = ax1.twinx()

# 绘制图像
ax1.plot(x, y1, 'g--')
ax2.plot(x, y2, 'b--')

ax1.set_xlabel('x data')
ax1.set_ylabel('y1', color = 'g')
ax2.set_xlabel('y2', color = 'b')

plt.show()



