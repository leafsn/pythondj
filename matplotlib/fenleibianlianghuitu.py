# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 17:04
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : fenleibianlianghuitu.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
'''
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(1, figsize=(9,3))

# 柱状图
plt.subplot(131)
plt.bar(names, values)

# 散点图
plt.subplot(132)
plt.scatter(names, values)

# 线性图
plt.subplot(133)
line, = plt.plot(names, values, linewidth=2.0)
line.set_antialiased(False)
plt.setp(line, color='r', linewidth=2.0)


# title
plt.suptitle('Categorical Plotting')
plt.show()



# 使用多个图形和轴

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.show()

'''

mu, sigma = 100, 15

