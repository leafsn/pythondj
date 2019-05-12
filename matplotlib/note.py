# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 10:06
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : note.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure()
plt.plot(x, y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2 * x0 + 1

plt.scatter(x0, y0, s = 50, color = 'blue')
plt.plot([x0, x0], [y0, 0], 'k--', lw = 2.5)

plt.annotate(r'$ 2*x+1 = %s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords = 'offset points', fontsize =16, arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad = .2'))

plt.text(-3, 3, r'$Test\ text. \mu \sigma_i, \alpha_i$', fontdict = {'fontsize':12, 'color':'red'})

plt.show()


