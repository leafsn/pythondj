# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 13:50
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : client.py
# @Software: PyCharm

import socket

s = socket.socket()
host = socket.gethostname()

port = 12345

s.connect((host, port))
print(s.recv(1024))
s.close()
