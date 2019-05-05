# coding: utf-8
# @Time    : 2019/5/5 14:15
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : thread.py
# @Software: PyCharm
from time import sleep, ctime
import threading

def super_player(file, time):
    for i in range(3):
        print('Start playing: {}! {}'.format(file, ctime()))
        sleep(time)

list = {'aiqing.mp3':3, 'a.mp4':5, 'abc.mp3':4}

threads = []
files = range(len(list))

for file, time in list.items():
    t = threading.Thread(target=super_player, args=(file, time))
    threads.append(t)

if __name__ == '__main__':
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

    print('end: {}'.format(ctime()))

