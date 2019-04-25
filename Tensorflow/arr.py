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
plt.show()



