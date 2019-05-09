# coding: utf-8
# @Time    : 2019/5/8 9:30
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : pd2.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 组合重叠数据集
df1 = pd.DataFrame({'A': [np.nan, 3., 5., np.nan],
                    'B': [np.nan, 2, 3, np.nan, 6]})

df2 = pd.DataFrame({'A': [5., 2., 4., np.nan, 3., 7.],
                    'B': [np.nan, np.nan, 3., 4., 6., 8.]})

