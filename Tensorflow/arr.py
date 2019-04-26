# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 11:41
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : arr.py
# @Software: PyCharm
import numpy as np

array = np.arange(27).reshape(3,3,3)
print(array)

print(array.shape)

print(np.empty((2,3)))

A = np.array([[1,-1,2],[3,2,0]])
print(A)

V = np.array([[2],[1],[3]])
print(V)
print(V.T)

v = np.transpose(np.array([[2,1,3]]))
print(v)
print(A[1,2])
print(A[:,1:2])

w = np.dot(A, v)
print(w)

A = np.array([[2,1,-1],[3,0,1],[1,1,-1]])
b = np.transpose(np.array([[-3,5,-2]]))
x = np.linalg.solve(A, b)
print(x)
print('-----------------------')
import csv
import numpy as np

def readDate():
    x = []
    y = []
    with open('Housing.csv','r',encoding='utf-8') as f:
        rdr = csv.reader(f)
        next(rdr)
        for line in rdr:
            xline = [1.0]
            for s in line[:-1]:
                xline.append(float(s))
            x.append(xline)
            y.append(float(line[-1]))
    return (x,y)

x0,y0 = readDate()
d = len(x0) - 10
x = np.array(x0[:d])
y = np.transpose(np.array([y0[:d]]))

xt = np.transpose(x)
xtx = np.dot(xt,x)
xty = np.dot(xt,y)

beta = np.linalg.solve(xtx, xty)
print(beta)

for data, actual in zip(x0[d:], y0[d:]):
    x = np.array([data])
    prediction = np.dot(x, beta)
    print('prediction = ' + str(prediction[0,0]) + 'actual = ' + str(actual))

import matplotlib.pyplot as plt

def mandelbrot(h,w,maxit=20):
    y,x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime
plt.imshow(mandelbrot(400, 400))
# plt.show()

stus_score = np.array([[80,88],
                       [82,81],
                       [84,75],
                       [86,83],
                       [75,81]])
# 每一列的最大值
result = np.amax(stus_score, axis=0)
print(result)

#每一行的最大值
result = np.amax(stus_score, axis=1)
print(result)

#每一列的最小值
result = np.amin(stus_score, axis=0)
print(result)

# 每一列的最大值
result = np.amin(stus_score, axis=1)
print(result)

#每一列的平均值
result = np.mean(stus_score, axis=0)
print(result)

#每一行的平均值
result = np.mean(stus_score, axis=1)
print(result)

# 每一列的方差
result = np.std(stus_score, axis=0)
print(result)

# 每一行的方差
result = np.std(stus_score, axis=1)

#第一列加5
stus_score[:,0] = stus_score[:,0]+5
print(stus_score)

# 第一列*0.5
stus_score[:,0] = stus_score[:,0]*0.5
print(stus_score)

stus_score = np.array([[80,88],
                       [82,81],
                       [84,75],
                       [86,83],
                       [75,81]])
# 平时成绩占40% 期末成绩占60%, 计算结果
q = np.array([[0.4],[0.6]])
result = np.dot(stus_score, q)
print(result)


# 矩阵垂直拼接
v1 = [[88, 82, 84, 86, 81],[89, 82, 84, 86, 81]]
v2 = [[88, 82, 84, 86, 81],[89, 82, 84, 86, 81]]

result = np.vstack((v1,v2))
print(result)

# 矩阵水平拼接
result = np.hstack((v1, v2))
print(result)

# 读取数据
result = np.genfromtxt('123.csv',encoding='utf-8', delimiter=',')
print(result)

# IO
from io import StringIO

data = u'1,2,3\n4,5,6'
print(np.genfromtxt(StringIO(data), delimiter=','))

# data = u'1 2 3\n 4 5 67\n890123 4'
# print(np.genfromtxt(StringIO(data), delimiter=3))

data = u"123456789\n   4  7 9\n   4567 9"
print(np.genfromtxt(StringIO(data), delimiter=(4,3,2)))

## 去掉空格
data = u"1, abc , 2\n 3, xxx, 4"
print(np.genfromtxt(StringIO(data), delimiter=',', dtype='|U5', autostrip=True))

## 去掉注释
data = u"""# # Skip me ! # Skip me too !
 1, 2
 3, 4
 5, 6 #This is the third line of the data
 7, 8
 # And here comes the last line
 9, 0
"""
print(np.genfromtxt(StringIO(data), comments="#", delimiter=","))

# 文件开始跳过几个，文件结束跳过几个
data = u"\n".join(str(i) for i in range(10))
print(np.genfromtxt(StringIO(data)))
print(np.genfromtxt(StringIO(data), skip_header=3, skip_footer=4))

## 只导入列
data = u'1 2 3\n4 5 6'
#通过列索引
print(np.genfromtxt(StringIO(data), usecols =(0,-1)))
#通过列名称
print(np.genfromtxt(StringIO(data), names='a,b,c', usecols=('a','c')))

data = StringIO('1 2 3\n 4 5 6')
#非每列分配一个名称
result = np.genfromtxt(data, dtype=[(int) for _ in 'abc'])
print(result)

data = StringIO('1 2 3\n 4 5 6')
result = np.genfromtxt(data, names='a, b,c')
print(result)

data = StringIO('so it goes\n#a b c\n1 2 3\n 4 5 6')
print(np.genfromtxt(data, skip_header=1, names=True))

data = StringIO('1 2 3\n 4 5 6')

# 默认使用f0 f1 f2...名字
result = np.genfromtxt(data, dtype=(int, float, int))
print(result)

# 修改默认名字
data = StringIO('1 2 3\n 4 5 6')
result = np.genfromtxt(data, dtype=(int, float, int), defaultfmt='var_%02i')

# 带百分号的转换为0-1之间的浮点数
data = u'1, 2.3%, 45.\n6,78.9%,0'
name = ('i', 'p', 'n')
result = np.genfromtxt(StringIO(data), names=name, delimiter=',')
print(result)

data = u'1, 2.3%, 45.\n6,78.9%,0'
convertfunc = lambda x: float(x.strip())
#字符串转换为浮点数    convertfunc转换器
result = np.genfromtxt(StringIO(data), delimiter=',', names=name, converters={1 : convertfunc})
print(result)

data = u'1, , 45.\n6,8,0'
# 如果为0 给默认值
convert = lambda x: float(x.strip() or -999)
result = np.genfromtxt(StringIO(data), names=name, delimiter=',', converters={1: convert})
print(result)


### 缺少值处理
data = u"N/A, 2, 3\n4, ,???"
keargs = dict(delimiter=',',
              dtype=int,
              names = 'a, b, c',
              missing_values={0:'N/A', 'b':'', 2:'???'},
              filling_values={0:0, 'b':0, 2:-99})
result = np.genfromtxt(StringIO(data), **keargs)
print(result)

### 索引
x = np.arange(10,1,-1)
result= x[np.array([[1,1],[2,3]])]
print(result)

y = np.arange(35).reshape(5,7)
#多维数组
result = y[np.array([0,2,4]), np.array([0,1,2])]
print(result)

#索引数组与其他标量进行组合
result = y[np.array([0,2,4]), 1]
print(result)

# 带一个数组索引。索引行
result = y[np.array([0,2,4])]
print(result)

# 布尔索引与mask索引
b = y>20
result = y[b]
print(result)
# y是多维情况，得到的值也是多维的
b = b[:,5]
result = y[b]
print(result)

# 索引数组与切片使用
result = y[np.array([0,2,4]), 1:3]
print(result)

#增加维度
x = np.arange(5)
result = x[:,np.newaxis] + x[np.newaxis,:]
print(result)

#省略号表示所有未指定的维度
z = np.arange(81).reshape(3,3,3,3)
result = z[1,...,2]
print(result)

#等同于上面
result = z[1,:,:,2]
print(result)

x = np.arange(0, 50, 10)
x[np.array([1,2,1,1])] +=1
print(x)
print(z)
# 用元组作为索引
indices = (1,1,1,1)
result = z[indices]
print(result)

# 使用slice定义切片
#四个就找四维对象
indices = (1,1,1,slice(0,2))
result = z[indices]
print(result)

# 使用Ellipsis省略号对象指定省略号
# 三维就找三维对象
indices = (1,Ellipsis,1)
result = z[indices]
print(result)

### 广播

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
b = 2.0
print(a*b)

x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
z = np.ones((3,4))

print(xx + y)
print(x+z)

a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([1.0, 2.0, 3.0])
result = a[:,np.newaxis] + b
print(result)



## 文件格式
big_end_buffer = bytearray([0,1,2,3])
import numpy as np
big_end_arr = np.ndarray(shape=(2,),dtype='>i2', buffer=big_end_buffer)
print(big_end_arr[0])
print(big_end_arr[1])
print(big_end_arr)


# 结构化数组
x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],
             dtype=[('name', 'U10'),('age', '<i4'),('weight','<f4')])
print(x)