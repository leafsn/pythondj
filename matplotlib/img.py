
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('bb.jpg', True)

# print(img)

imgplot = plt.imshow(img)

lum_img = img[:, :, 0]
plt.imshow(lum_img)

plt.imshow(lum_img, cmap='hot')

imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')


plt.colorbar()
imgplot = plt.imshow(lum_img, clim=(0.0, 0.7))
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

fig = plt.figure()
a = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(lum_img)
a.set_title('Before')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

a = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.1, 0.7)
a.set_title('After')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')



from PIL import  Image
# 降低图像像素
img = Image.open('bb.jpg')
img.thumbnail((64,64), Image.ANTIALIAS)


# imgplot = plt.imshow(img)
# imgplot = plt.imshow(img, interpolation='nearest')

#模糊处理
imgplot = plt.imshow(img, interpolation='bicubic')


plt.show()
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

