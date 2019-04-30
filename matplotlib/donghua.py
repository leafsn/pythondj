# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 14:47
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : donghua.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import animation

# 定义figure
fig, ax = plt.subplots()

# 定义数据
x = np.arange(0, 2 * np.pi,0.01)

# line， 表示只取返回值中的第一个元素
line, = ax.plot(x, np.sin(x))

# 定义动画的更新
def update(i):
    line.set_ydata(np.sin(x + i/10))
    return line,

# 定义动画的初始值
def init():
    line.set_ydata(np.sin(x))
    return line


# 创建动画
ani = animation.FuncAnimation(fig = fig, func=update, init_func=init, interval=10, blit=False)

# 展示动画
plt.show()

ani.save('sin.html', writer='imagemagick', fps=30, dpi=100)



import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()

ax = plt.axes(xlim =(0,2), ylim = (-2, 2))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line

anim = animation.FuncAnimation(fig=fig, func=animate, init_func=init,
                               frames=200, interval=20, blit=True)

plt.show()

