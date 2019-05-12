# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 9:42
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : zidingyi.py
# @Software: PyCharm
import numpy as np
import  matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use('ggplot')
data = np.random.randn(50)

# 黑色背景，圆点
# with plt.style.context(('dark_background')):
#     plt.plot(np.sin(np.linspace(1, 2*np.pi)), 'r-o')

# 波浪图
# mpl.rcParams['lines.linewidth'] = 2
# mpl.rcParams['lines.color'] = 'r'
mpl.rc('lines', linewidth=4, color='g')

# 恢复默认设置
mpl.rcdefaults()

plt.plot(data)

plt.show()