# coding: utf-8
# @Time    : 2019/5/9 9:25
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : pdmap.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

s = pd.Series(['six', 'seven', 'six', 'seven', 'six'],
              index=['a', 'b', 'c', 'd', 'e'])

t = pd.Series({'six': 6., 'seven': 7.})
print(s)
# 链接映射二级系列定义的值，与合并相关
print(s.map(t))

## 重新索引和更改标签 reindex()
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)

# 重新排序现有数据以匹配一组新标签, f标签未在此系列中，值为nan
print(s.reindex(['e', 'b', 'f', 'd ']))

# DataFrame 重新索引行和列
df = pd.DataFrame({
     'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
     'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
     'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})


print(df)
print(df.reindex(index=['c', 'f', 'b'], columns=['three', 'two', 'one']))

# 使用reindex 和 axis关键字
print(df.reindex(['c', 'f', 'b'], axis='index'))

# index包含实际轴标签的对象可以在对象之间共享
rs = s.reindex(df.index)
print(s)
print(rs)

# reindex 支持对轴样式调用约定  指定单个label参数并axis应用于该参数
print(df.reindex(['c', 'f', 'b'], axis='index'))
print(df.reindex(['three', 'two', 'one'], axis='columns'))

df2 = pd.DataFrame(np.random.randn(3, 2),
                   index=['a', 'b', 'c'],
                   columns=['one', 'two'])

print(df2)

## 获取一个对象并重新索引其轴标记与另一个对象相同 reindex_like()

print(df.reindex_like(df2))

# 对象相互对齐 align()
'''
    join='outer' 取索引的并集 （默认）
    join='left'  使用调用对象的索引，左对齐
    join='right' 使用传递的对象的索引
    join='inner'  索引相交,交集
'''

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s1 = s[:4]
s2 = s[1:]
print(s1)
print(s2)
print(s1.align(s2))

print(s1.align(s2, join='inner'))
print(s1.align(s2, join='left'))
print(s1.align(s2, join='outer'))

# DataFrames索引和列

print(df.align(df2, join='inner'))

# axis选项以仅在指定的 轴上对齐 列
print(df.align(df2, join='inner', axis=0))
# 行
print(df.align(df2.iloc[0], axis=1))

### 重建索引时填充, reindex()采用可选参数method，该参数选择填充值

rng = pd.date_range('1/1/2019', periods=8)
ts = pd.Series(np.random.randn(8), index=rng)
ts2 = ts[[0, 3, 6]]
print(ts)
print(ts2)
print(ts2.reindex(ts.index))
''' nan填充    要求索引按递增或者递减,如果不是会引发ValueError
    ffill 向前填充值
    bfill 向后填充值
    nearest 从最近的索引值填写
'''
print(ts2.reindex(ts.index, method='ffill'))
print(ts2.reindex(ts.index, method='bfill'))
print(ts2.reindex(ts.index, method='nearest'))
# 使用fillna实现相同的效果
print(ts2.reindex(ts.index).fillna(method='ffill'))

## 重建索引是填充的限制
## 限制指定连续匹配的最大数量
print(ts2.reindex(ts.index, method='ffill', limit=1))

# 指定索引和索引器值之间的最大距离
print(ts2.reindex(ts.index, method='ffill', tolerance='1 day'))

## 从轴中删除标签 drop
# 删除ad行
print(df.drop(['a', 'd'], axis=0))

# 删除 one 列
print(df.drop(['one'], axis=1))

# 同样删除ad行
print(df.reindex(df.index.difference(['a', 'd'])))


### rename() 方法，允许基于某些映射或任意函数重新标记轴

print(s)

# str.upper函数轴变为大写
print(s.rename(str.upper))

# 使用字典或列表， 修改轴名称
dd = df.rename(columns={'one': 'foo', 'two': 'bar'},
          index={'a': 'apple', 'b': 'banana', 'd': 'durian'})

print(dd)

## 指定轴样式调用约定，可以在其中指定单个mapper并将该axis映射用于该约定

dd = df.rename({'one': 'foo', 'two': 'bar'}, axis='columns')
de = df.rename({'a': 'apple', 'b': 'banana', 'd': 'durian'}, axis='index')

print(dd)
print(de)

# 更改Series.name属性
print(s.rename('scalar-name'))


## rename_axis() 允许更改MultiIndex特定的名称 与标签相对

df = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6],
                   'y': [10, 20, 30, 40, 50, 60]},
                  index=pd.MultiIndex.from_product([['a', 'b', 'c'], [1, 2]],
                                                   names=['let', 'num']))
print(df)
print(df.rename_axis(index={'let': 'abc'}))
print(df.rename_axis(index=str.upper))

## 迭代
df = pd.DataFrame({'col1': np.random.randn(3),
                   'col2': np.random.randn(3)},
                  index=['a', 'b', 'c'])

for col in df:
    print(col)

df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})
for index, row in df.iterrows():
    row['a'] = 10
print(df)

for item, frame in df.iteritems():
    print(item)
    print(frame)

for row_index, row in df.iterrows():
    print(row_index, row, sep='\n')

df_orig = pd.DataFrame([[1, 1.5]], columns=['int', 'float'])
print(df_orig.dtypes)

row = next(df_orig.iterrows())[1]
print(row)


print(row['int'].dtype)
print(df_orig['int'].dtype)

df2 = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
print(df2)

print(df2.T)

df2_t = pd.DataFrame({idx: values for idx, values in df2.iterrows()})
print(df2_t)

# itertuples()返回一个迭代器，为DataFrame中的每一行产生一个namedtuple
for row in df.itertuples():
    print(row)

# .dt 返回日期时间的特定值
s = pd.Series(pd.date_range('20100101 09:10:11', periods=4))
print(s)

# 返回小时
print(s.dt.hour)
# 返回分钟
print(s.dt.second)
# 返回天
print(s.dt.day)

# 返回特定天数的
print(s[s.dt.day == 2])

stz = s.dt.tz_localize('US/Eastern')
print(stz)

print(s.dt.tz_localize('UTC').dt.tz_convert('US/Eastern'))

s = pd.Series(pd.date_range('20130101', periods=4))
print(s)

print(s.dt.strftime('%Y/%m/%d'))

s = pd.Series(pd.period_range('20130101', periods=4, freq='D'))
print(s)

# 返回年
print(s.dt.year)
print(s.dt.day)

# 连续时间，一秒增长
s = pd.Series(pd.timedelta_range('1 day 00:00:05', periods=4, freq='s'))
print(s)
print(s.dt.days)
print(s.dt.seconds)
# 返回时间的组成
print(s.dt.components)


### 矢量化字符串方法 str.
s = pd.Series(['A', 'B', 'C', 'Abca', np.nan, 'CABA', 'dog', 'cat',])
print(s.str.lower( ))


df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})

unsorted_df = df.reindex(index=['a', 'b', 'c', 'd'],
                         columns=['three', 'two', 'one'])

print(unsorted_df)
# 行轴编号进行排序
print(unsorted_df.sort_index())
print(unsorted_df.sort_index(ascending=False))
# 列轴编号排序
print(unsorted_df.sort_index(axis=1))

print(unsorted_df['three'].sort_index())


# 按值  Series.sort_values()方法用于按系列值进行排序，列值和行值
df1 = pd.DataFrame({'one': [2, 1, 1, 1],
                    'two': [1, 3, 2, 4],
                    'three': [5, 4, 3, 2]})

print(df1.sort_values(by='two'))

# by参数采用列名列表
print(df1[['one', 'two', 'three']].sort_values(by=['one', 'two']))

# na_position参数对na值进行特殊处理
s[2] = np.nan
print(s.sort_values())

# 操作把nan值放在前面
print(s.sort_values(na_position='first'))

# 引用列或索引级别名称
idx = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('a', 2),
                                 ('b', 2), ('b', 1), ('b', 1)])

idx.names = ['first', 'second']

df_multi = pd.DataFrame({'A': np.arange(6, 0, -1)},
                        index=idx)
print(df_multi)

print(df_multi.sort_values(by=['second', 'A']))

### 搜索 searchsorted() 与 numpy.ndarray.searchsorted()

ser = pd.Series([1, 2, 3])
print(ser.searchsorted([0, 3]))
print(ser)

print(ser.searchsorted([0, 4]))
print(ser.searchsorted([1, 3], side='right'))
print(ser.searchsorted([1, 3], side='left'))
ser = pd.Series([3, 1, 2])
print(ser.searchsorted([0, 3], sorter=np.argsort(ser)))

## 最大值和最小值 Series
s = pd.Series(np.random.permutation(10))
print(s)

print(s.sort_values())
# 返回最小的三个
print(s.nsmallest(3))
# 返回最大的三个
print(s.nlargest(3))

## 最大值和最小值  DataFrame
df = pd.DataFrame({'a': [-2, -1, 1, 10, 8, 11, -1],
                   'b': list('abdceff'),
                   'c': [1.0, 2.0, 3.0, 4.0, np.nan, 3.0, 2.5]})
# a列的最大值三个
print(df.nlargest(3, 'a'))

print(df.nlargest(5, ['a', 'c']))
# 取a列的最新值
print(df.nsmallest(3, 'a'))
print(df.nsmallest(5, ['a', 'c']))

df1.columns = pd.MultiIndex.from_tuples([('a', 'one'),
                                         ('a', 'two'),
                                         ('b', 'three')])

dd = df1.sort_values(by=('a', 'two'))
print(dd)

## 复制 copy()

# dtype
dft = pd.DataFrame({'A': np.random.rand(3),
                    'B': 1,
                    'C': 'foo',
                    'D': pd.Timestamp('20010102'),
                    'E': pd.Series([1.0]*3).astype('float32'),
                    'F': False,
                    'G': pd.Series([1] * 3, dtype='int8')})

print(dft)
print(dft.dtypes)
print(dft['A'].dtype)

print(pd.Series([1, 2, 3, 4, 5, 6.]))
print(pd.Series([1, 2, 3, 6., 'foo']))

# 返回dft的类型数量
print(dft.get_dtype_counts())

df1 = pd.DataFrame(np.random.randn(8, 1), columns=['A'], dtype='float32')
print(df1)
print(df1.dtypes)

df2 = pd.DataFrame({'A': pd.Series(np.random.randn(8), dtype='float16'),
                    'B': pd.Series(np.random.randn(8)),
                    'C': pd.Series(np.array(np.random.randn(8),
                                   dtype='uint8'))})

print(df2)
print(df2.dtypes)

# 默认值
print(pd.DataFrame([1,2], columns=['a']).dtypes)
print(pd.DataFrame({'a': [1, 2]}).dtypes)
print(pd.DataFrame({'a': 1}, index=list(range(2))).dtypes)

frame = pd.DataFrame(np.array([1, 2]))

# 向上转换
df3 = df1.reindex_like(df2).fillna(value=0.0) + df2
print(df3)

# 指定类型 astype()
dft = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
dft[['a', 'b']] = dft[['a', 'b']].astype((np.uint8))
print(dft)
print(dft.dtypes)

# 通过传递字典将某些列转换为特定的dtype
dft1 = pd.DataFrame({'a': [1, 0, 1], 'b':[4, 5, 6], 'c': [7, 8, 9]})
dft1 = dft1.astype({'a': np.bool, 'c': np.float64})
print(dft1)
print(dft1.dtypes)

dft = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
print(dft.loc[:, ['a', 'b']].astype(np.uint8).dtypes)

dft.loc[:, ['a', 'b']] = dft.loc[:, ['a', 'b']].astype(np.uint8)
print(dft.dtypes)
'''
### 使用函数将object强制转换为其他类型
'''
import datetime
df = pd.DataFrame([[1, 2],
                   ['a', 'b'],
                   [datetime.datetime(2016,2,3),
                    datetime.datetime(2016,3,2)]])
df = df.T
print(df)
print(df.dtypes)

print(df.infer_objects().dtypes)

## to_numeruc() 转换为数字类型
m = ['1.1', 2, 4]
print(pd.to_numeric(m))

# to_datetime() 转化为datetime对象
m = ['2016-07-09', datetime.datetime(2016,1,2)]
print(pd.to_datetime(m))

# to_timedelta() 转换为timedelta对象
m = ['apple', datetime.datetime(2016, 3, 2)]
# errors='coerce' 转换错误忽略, 转换为pd.NaT（datetime,timedelta） 或 np.nan(数字)
print(pd.to_datetime(m, errors='coerce'))

m = ['apple', 2, 3]
print(pd.to_numeric(m, errors='coerce'))

m = ['apple', pd.Timedelta('1day')]
print(pd.to_timedelta(m, errors='coerce'))

# errors='ignore' 如果在转换为所需数据类型是遇到任何错误，返回传入的的数据

m = ['apple', datetime.datetime(2016,3,2)]
print(pd.to_datetime(m, errors='ignore'))

m = ['apple', 2, 3]
print(pd.to_numeric(m, errors='ignore'))

m = ['apple', pd.Timedelta('1day')]
print(pd.to_timedelta(m, errors='ignore'))

# to_numeric() 的参数 downcast, 将新的数字数据向下转换为较小的dtype,节省内存
m = ['1', 2, 3]
# 适用于以为数组，列表或标量
print(pd.to_numeric(m, downcast='integer')) # 最小的有符号整数
print(pd.to_numeric(m, downcast='signed')) # 最小的有符号整数类型
print(pd.to_numeric(m, downcast='unsigned')) # 最小的无符号整数
print(pd.to_numeric(m, downcast='float'))  # 最小的浮点数类型

df = pd.DataFrame([['2016-07-09', datetime.datetime(2016, 3, 2)]] * 2, dtype='O')
print(df)

print(df.apply(pd.to_datetime))

df = pd.DataFrame([['1.1', 2, 3]] * 2, dtype='O')
print(df)
print(df.apply(pd.to_numeric))

df = pd.DataFrame([['5us', pd.Timedelta('1day')]] * 2, dtype='O')
print(df)
print(df.apply(pd.to_timedelta))

# 根据dtype选择列
df = pd.DataFrame({
    'string': list('abc'),
    'int64': list(range(1, 4)),

})
