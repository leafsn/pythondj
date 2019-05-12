# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 11:44
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : denggao.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return (1 - x/2 + x**5 + y**3) * np.exp(- x**2 - y**2)

n = 356

x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

## 生成网格数据
x, y = np.meshgrid(x, y)


# 填充等高线颜色
plt.contourf(x, y, f(x, y), 8, alpha = 0.75, cmap = plt.cm.hot)

# 绘制等高线
C = plt.contour(x, y, f(x, y), 8, colors = 'black', linewidth = 0.5)

# 绘制等高线数据
plt.clabel(C, inline = True, fontsize = 10)

plt.xticks(())
plt.xticks(())

plt.show()

