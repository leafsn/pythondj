# coding: utf-8
# @Time    : 2019/5/5 16:13
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : matplo.py
# @Software: PyCharm

# sphinx_gallery_thumbnail_number = 18
#import matplotlib
#matplotlib.use('Qt5Agg')

import warnings

import matplotlib.pyplot as plt
import  numpy as np
import matplotlib.colors as mcolors
import matplotlib._layoutbox as layoutbox

plt.rcParams['savefig.facecolor'] = '0.8'
plt.rcParams['figure.figsize'] = 4.5, 4

def example_plot(ax, fontsize=12, nodec=False):
    ax.plot([1, 2])

    ax.locator_params(nbins=3)
    if not nodec:
        ax.set_xlabel('x-label', fontsize=fontsize)
        ax.set_ylabel('y-label', fontsize=fontsize)
        ax.set_title('Title', fontsize=fontsize)
    else:
        ax.set_xticklabels('')
        ax.set_yticklabels('')

fig, ax = plt.subplots(constrained_layout=False)
example_plot(ax, fontsize=24)

plt.show()

