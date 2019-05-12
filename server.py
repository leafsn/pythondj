# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 13:46
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : server.py
# @Software: PyCharm

import socket

s = socket.socket()

host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c.addr = s.accept()
    print('链接地址： ', addr)
    c.sed('welcome')
    c.close