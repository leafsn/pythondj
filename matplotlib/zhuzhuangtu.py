# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 11:08
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : zhuzhuangtu.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

n = 10
x = np.arange(n)

y1 = (1 - x/float(n)) * np.random.uniform(0.5, 1.0, n)
y2 = (1 - x/float(n)) * np.random.uniform(0.5, 1.0, n)

## 绘制柱状图
plt.bar(x, y1, facecolor = 'blue', edgecolor = 'white')
plt.bar(x, -y2, facecolor = 'red', edgecolor = 'white')

temp = zip(x, y2)

for x, y in zip(x, y1):
    plt.text(x + 0.05, y + 0.1, '%.2f' %y, ha = 'center', va = 'bottom')

for x, y in temp:
    plt.text(x + 0.05, -y -0.1, '%.2f' %y, ha = 'center', va = 'bottom')

plt.xlim(-1, n)
plt.ylim(-1.5, 1.5)

plt.xticks(())
plt.yticks(())

plt.show()


