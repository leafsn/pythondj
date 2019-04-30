# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 14:13
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : qiantaofig.py
# @Software: PyCharm

import matplotlib.pyplot as plt

fig = plt.figure()

x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5, 6]

# figure的百分比， 从figure 10%的位置开始绘制， 宽高是figure 的80%
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8

# 绘制的句柄
ax1 = fig.add_axes([left, bottom, width, height])

# 绘制点
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Test')

# 嵌套方法一
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25

# 获得绘制的句柄
ax2 = fig.add_axes([left, bottom, width, height])

# 绘制点
ax2.plot(x, y, 'r')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('part1')

# 嵌套方法二
plt.axes([bottom, left, width, height])
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('part2')

plt.show()



