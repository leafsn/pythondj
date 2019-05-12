# coding: utf-8
# @Time    : 2019/5/5 14:29
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : MyThread.py
# @Software: PyCharm

# 多线程
import threading
from time import sleep, ctime

class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def super_play(file, time):
    for i in range(2):
        print('Start playing: {}! {}'.format(file, ctime()))
        sleep(time)


list = {'abc.mp3':3, 'abcd.mp4':5}

threads = []
files = range(len(list))

for k,v in list.items():
    t = MyThread(super_play, (k,v), super_play.__name__)
    threads.append(t)

if __name__ == '__main__':
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

    print('end: {}'.format(ctime()))
