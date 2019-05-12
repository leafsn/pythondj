# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 11:28
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : dtype.py
# @Software: PyCharm

import numpy as np
x = np.array([(1,2,3), (4,5,6)], dtype='i8, f4, f8')
x[1] = (7,8,9)
print(x)

a = np.zeros(3, dtype=[('a','i4'),('b','i4'),('c','f4')])
result = a[['a','b']]
print(result)

a = np.zeros(2, dtype=[('a', 'i4'),('b','i4')])
b = np.ones(2, dtype=[('a', 'i4'),('b','i4')])
print(a == b)

recordarr = np.rec.array([(1,2,'hello'),(2,3,'world')],
                         dtype=[('foo', 'i4'),('bar','f4'),('baz','S10')])
print(recordarr.bar)

arr = np.array([(1,2,'hello'),(2,3,'world')],
               dtype=[('foo','i4'),('bar','f4'),('baz','S10')])
recordarr = np.rec.array(arr)
print(recordarr)

arr = np.array([(1,2,'hello'),(2,3,'world')],
               dtype=[('foo','i4'),('bar','f4'),('baz','a10')])
recordarr = arr.view(dtype=np.dtype((np.record, arr.dtype)),
                     type=np.recarray)
print(recordarr)

recordarr = arr.view(np.recarray)
re = recordarr.dtype
print(re)

recordarr = np.rec.array([('hello',(1,2)),('world',(3,4))],
                         dtype=[('foo','S6'),('bar',[('A',int),('B',int)])])
print(type(recordarr.foo))
print(type(recordarr.bar))

# Recarray Helper函数
from numpy.lib import recfunctions as rfn
a = np.array([(1,(2,3.0)),(4,(4,6.0))],
              dtype= [('a',np.int64),('b',[('ba',np.double), ('bb',(np.int64))])])

print(rfn.drop_fields(a,'a'))
print(rfn.drop_fields(a,'ba'))
print(rfn.drop_fields(a, ['ba', 'bb']))


ndtype = [('a', int)]
a = np.ma.array([1,1,1,2,2,3,3],
                mask=[0,0,1,0,0,0,1]).view(ndtype)

print(rfn.find_duplicates(a,ignoremask=True,return_index=True))

# class C(np.ndarray):
#     pass
#
# arr = np.zeros((3,))
# c_arr = arr.view(C)
# print(type(c_arr))

class C(object):
    def __new__(cls, *args):
        print('Cls in __new__:', cls)
        print('Args in __new__:',args)
        return object.__new__(cls, *args)

    def __init__(self,*args):
        print('type(self) in __init__',type(self))
        print('Args in __init__:', args)


class C(np.ndarray):
    def __new__(cls, *args, **kwargs):
        print('In __new__ with class %s' % cls)
        return super(C, cls).__new__(cls, *args, *kwargs)

    def __init__(self, *args, **kwargs):
        print('In __init__ with class %s' % self.__class__)

    def __array_finalize__(self, obj):
        print('In array_finalize: ')
        print(' self type is %s' %type(self))
        print('obj type is %s' % type(obj))


## 向ndarray添加额外属性
import  numpy as np

class InfoArray(np.ndarray):

    def __new__(subtype, shape, dtype=float, buffer=None, offset=0,
                strides=None, order=None, info=None):
        obj = super(InfoArray, subtype).__new__(subtype, shape,dtype,
                                                buffer, offset, strides, order)
        obj.info = info
        return obj

    def __array_finalize(self, obj):

        if obj is None :
            return
        self.info = getattr(obj, 'info', None)

print(type(InfoArray(shape=(3,))))

class RealisticInfoArray(np.ndarray):
    def __new__(cls, input_array, info = None):
        obj = np.asarray(input_array).view(cls)
        obj.info = info
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.info = getattr(obj, 'info', None)

class A(np.ndarray):
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        args = []
        in_no = []
        for i, input_ in enumerate(inputs):
            if isinstance(input_, A):
                in_no.append(i)
                args.append(input_.view(np.ndarray))
            else:
                args.append(input_)

        outputs = kwargs.pop('out', None)
        out_no = []
        if outputs:
            out_args=[]
            for j, output in enumerate(outputs):
                if isinstance(output, A):
                    out_no.append(j)
                    out_args.append(output.view(np.ndarray))
                else:
                    out_args.append(output)
            kwargs['out'] = tuple(out_args)
        else:
            outputs = (None,) * ufunc.nout

        info = {}
        if in_no:
            info['inputs'] = in_no
        if out_no:
            info['outputs'] = out_no

        results = super(A, self).__array_ufunc__(ufunc, method, *args, **kwargs)

        if result is NotImplemented:
            return NotImplemented

        if method == 'at':
            if isinstance(inputs[0], A):
                inputs[0].info = info
            return

        if ufunc.nout == 1:
            results = (results,)

        results = tuple((np.asarray(result).view(A)
                         if output is None else output)
                        for result, output in zip(results. outputs))

        if results and isinstance(results[0], A):
            results[0].info = info

        return results[0] if len(results) == 1 else results

a = np.arange(5).view(A)
b = np.sin(a)
print(b.info)


class MuSubClass(np.ndarray):

    def __new__(cls, input_array, info=None):
        obj = np.asarray(input_array).view(cls)
        obj.info = info
        return obj

    def __array_finalize__(self, obj):
        if obj is None : return
        self.info = getattr(obj, 'info', None)

    def __array_wrap__(self, out_arr, context =None):
        return super(MuSubClass, self).__array_warp__(self,out_arr, context)

### 浮点特殊值
x = np.arange(10.)
x[3] = np.nan
print(x.sum())
print(np.nansum)







