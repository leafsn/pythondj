# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 8:58
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : zuhe.py
# @Software: PyCharm

import numpy as np
from matplotlib import figure

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

plt.rcParams.update({'figure.autolayout':True})

fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',title='Company Revenue')

plt.style.use('fivethirtyeight')

# 格式化
def currency(x, pos):
    if x >= 1e6:
        s = '${:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
    return s

formatter = FuncFormatter(currency)

ax.xaxis.set_major_formatter(formatter)

# 添加一条垂直线
ax.axvline(group_mean, ls='--', color='r')

# 注释新的
for group in [3, 5, 8]:
    ax.text(145000, group, 'New Company', fontsize=10, verticalalignment='center')

# 上移标题
ax.title.set(y = 1.05)

ax.set(xlim=[-10000, 140000], xlabel='Total Tevenue', ylabel='Company', title='Company Revenue')
ax.set_xticks([0, 24e3, 50e3, 75e3, 100e3, 125e3])
fig.subplots_adjust(right=.1)

# 保存文件
figure.Figure.savefig(fig,fname='a.pdf')
plt.show()