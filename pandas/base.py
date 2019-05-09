# coding: utf-8
# @Time    : 2019/5/7 16:35
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : base.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

index = pd.date_range('1/1/2000', periods=8)
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])
# wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
#               major_axis=pd.date_range('1/2/2000', periods=5),
#               minor_axis=['A', 'B', 'C', 'D'])
# print(wp)

long_series = pd.Series(np.random.randn(1000))

# 开头的五行数据
print(long_series.head())

# 取倒数的三行数据
print(long_series.tail(3))

df.columns = [x.lower() for x in df.columns]
print(df)

# 使用.array
print(s)
print(s.index.array)
print(s.array)

# 转为numpy数组
print(s.to_numpy())
print(np.asarray(s))

ser = pd.Series(pd.date_range('2000', periods=2, tz='CET'))
print(ser.to_numpy(dtype=object))

print(ser.to_numpy(dtype='datetime64[ns]'))

print(df.to_numpy())

pd.set_option('compute.use_bottleneck', False)
pd.set_option('compute.use_numexpr', False)

df = pd.DataFrame({
     'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
     'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
     'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})

## 比较类似数组的对象
print(pd.Series(['foo', 'bar', 'baz']) == 'foo')

## 处理相同长度的不同类数组对象之间的比较,比较不同长度的会引发错误
print(pd.Series(['foo', 'bar', 'baz']) == np.array(['foo', 'bar', 'qux']))

print(pd.Series(['foo', 'bar', 'baz']) == pd.Index(['foo', 'bar', 'qux']))

print(np.array([1, 2, 3]) == np.array([1, 2]))

# 组合重叠数据集,没数据的换成有数据的进行组合，成为一个新的组合
df1 = pd.DataFrame({'A': [1., np.nan, 3., 5., np.nan],
                    'B': [np.nan, 2, 3, np.nan, 6]})

df2 = pd.DataFrame({'A': [5., 2., 4., np.nan, 3., 7.],
                    'B': [np.nan, np.nan, 3., 4., 6., 8.]})

print(df1)
print(df2)

print(df1.combine_first(df2))

print(df)

### 描述性统计