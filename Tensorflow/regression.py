# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 15:11
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : regression.py
# @Software: PyCharm

import numpy as np

my_array = np.array([1,2,3,4,5])
print (my_array)

print(my_array.shape)

#创建五个长度的空数组
print(np.zeros((5)))

#创建随机数组
print(np.random.random((5)))

# 创建一个二维数组
print(np.zeros((2,3)))

print(np.full((2,2), 7))

print(np.eye(3))

# 创建一个全为1的二维数组
print(np.ones((2, 4)))

#创建二维数组
my_array = np.array([[4, 5], [6, 1]])
print(my_array)
print(my_array[0][1])
print(my_array.shape)

my_array_column = my_array[:, 1]
print(my_array_column)


## 数组操作
a = np.array([[1.0, 2.0],
              [3.0, 4.0]])
b = np.array([[5.0, 6.0],
              [7.0, 8.0]])
sum = a + b
difference = a - b
prdict = a * b
quotient = a / b

#执行矩阵乘法
matrix_product = a.dot(b)
print('Matrix Product = \n', matrix_product)

print('Sum = \n',sum)
print('Difference = \n', difference)
print('Product = \n', prdict)
print('Quotient:\n', quotient)

print(np.arange(5))
print(np.linspace(0, 2*np.pi, 5))

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

## 切片
print(a[0, 1:4])
print(a[1:4, 0])
print(a[::2, ::2])
print(a[:, 1])

# 数组属性
print(type(a),a.dtype,a.size,a.shape,a.itemsize,a.ndim,a.nbytes)

a = np.arange(10)
print(a.sum())
print(a.min())
print(a.max())
print(a.cumsum())

# 花式索引
a = np.arange(0, 100, 10)
indices = [1, 5, -1]
b = a[indices]
print(a)
print(b)

# 布尔屏蔽
import matplotlib.pyplot as plt

a = np.linspace(0, 2*np.pi, 50)
b = np.sin(a)
plt.plot(a,b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()

# 缺省索引
a = np.arange(0, 100, 10)
b = a[:5]
c = a[a>=50]
print(b)
print(c)

# where函数
a = np.where(a < 50)
# c = np.where(a > 50)
print('a',a)
print('c',c)

# 快速排序
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
print(quicksort([3, 6, 8, 10, 1, 2, 1]))

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]
print(a[0,1])
b[0,0] = 77
print(a[0,1])

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12]])
print(a)

b = np.array([0,2,0,1])
print(a[np.arange(4), b])

a[np.arange(4), b] += 10
print(a)

# 数据类型
x = np.array([1, 2])
print(x.dtype)

x = np.array([1.0, 2.0])
print(x.dtype)

x = np.array([1, 2], dtype=np.int64)
print(x.dtype)