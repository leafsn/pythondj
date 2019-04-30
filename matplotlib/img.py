# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 13:29
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : img.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 定义figure
fig = plt.figure()

# 将figure变为3d
ax = Axes3D(fig)

# 数据数目
n = 256

x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)

# 生成网格数据
x,y = np.meshgrid(x, y)


# 计算每个点对的长度
R = np.sqrt(x**2 + y**2)

# 计算z轴的高度
z = np.sin(R)

# 绘制3d曲面
ax.plot_surface(x, y, z, rstride= 1, cstride= 1, cmap= plt.get_cmap('rainbow'))

# 绘制从3d曲面到底部的投影
ax.contour(x, y, z, zdim = 'z', offset= -2, cmap = 'rainbow')

# 设置z轴的维度
ax.set_zlim(-2, 2)

plt.show()


# #定义图像数据
# a= np.linspace(0, 1, 9).reshape(3, 3)
#
# # 显示图像数据
# plt.imshow(a, interpolation = 'nearest', cmap = 'bone', origin = 'lower')
#
# # 添加颜色条
# plt.colorbar()
#
# #去掉坐标轴
# plt.xticks(())
# plt.yticks(())

# plt.show()
