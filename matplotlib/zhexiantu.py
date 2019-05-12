# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 11:20
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : zhexiantu.py
# @Software: PyCharm

import matplotlib.ticker as ticker
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680802)
fig, ax = plt.subplots()
ax.plot(100*np.random.rand(20))

formatter = ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(formatter)

for tick in ax.yaxis.get_major_ticks():
    tick.label1On = False
    tick.lanle2On = True
    tick.label2.set_color('green')


plt.show()
