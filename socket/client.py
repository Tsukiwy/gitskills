# -*- coding: UTF-8 -*-
# 文件名：client.py
'''
接下来我们写一个简单的客户端实例连接到以上创建的服务。端口号为 12345。

socket.connect(hosname, port) 方法打开一个 TCP 连接到主机为 hostname 端口为 port 的服务商。

连接后我们就可以从服务端获取数据，记住，操作完成后需要关闭连接。
'''

import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口号

s.connect((host, port))
print s.recv(1024)
s.close()  