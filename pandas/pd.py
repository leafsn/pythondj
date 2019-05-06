# coding: utf-8
# @Time    : 2019/5/5 16:36
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : pd.py
# @Software: PyCharm

import numpy as np
import pandas as pd

# 创建nan 数组
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# 创建时间数组
dates = pd.date_range('20130101', periods=6)
print(dates)

# 添加头部
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20140304'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})

print(df2)
print(df2.dtypes)

print(df.head())
print(df.tail(3))
print(df.index)
print(df.columns)

# 转换为numpy数组
print(df.to_numpy())

# 显示数据的快速统计摘要
print(df.describe())

# 按轴排序
df.sort_index(axis=1, ascending=False)

# B列的值进行排序
df.sort_values(by='B')

''' 按标签选择'''
# 选择一个列
print(df['A'])


# 对行进行切片
print(df[0:3])
print(df['20130102': '20130105'])


# 获取横截面
print(df.loc[dates[0]])

# 按标签选择多轴
print(df.loc[:, ['A', 'B']])

# 标签切片
print(df.loc['20130102': '20130104', ['A', 'B']])

# 返回对象的值 20130102 A B 的值
print(df.loc['20130102', ['A', 'B']])

# 获取标量值
print(df.loc[dates[0], 'A'])
print(df.at[dates[0], 'A'])

'''按位置选择'''
print(df.iloc[3])

# 整数切片
print(df.iloc[3:5, 0:2])

# 切片行
print(df.iloc[1:3, :])

# 切片列
print(df.iloc[:, 1:3])

# 明确获取值
print(df.iloc[1, 1])
print(df.iat[1, 1])

'''布尔索引'''

print(df[df.A > 0])

print(df[df > 0])

# isin() 过滤方法
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

print(df2)
print(df2[df2['E'].isin(['two', 'four'])])

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print(s1)

df['F'] = s1

# 按标签设置值
df.at[dates[0], 'A'] = 0

# 按位置设置值
df.iat[0, 1] = 0

df.loc[:, 'D'] = np.array([5] * len(df))

print(df)

df2 = df.copy()
df2[df2>0] = -df2
print(df2)

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1

print(df1)

# 删除任何缺少数据的行
print(df1.dropna(how ='any'))

# 填写缺失的数据
print(df1.fillna(value=5))

# 获取值所在与nan的布尔值
print(pd.isna(df1))

# 执行描述性统计
print(df.mean())

# 一个轴的操作
df.mean(1)

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)

print(df.sub(s, axis='index'))

## 将函数应用于数据
print(df.apply(np.cumsum))

print(df.apply(lambda x: x.max() - x.min()))


### 直方图
s = pd.Series(np.random.randint(0, 7, size=10))

print(s)

print(s.value_counts())

## 字符串方法

s = pd.Series(['A', 'B', 'C', 'Aaba', np.nan, 'CABA','dog', 'cat'])

# 字符串全部小写
print(s.str.lower())

## 合并
df = pd.DataFrame(np.random.randn(10, 4))
print(df)