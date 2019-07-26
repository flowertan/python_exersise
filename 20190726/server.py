# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/26 22:07
# @file    : server.py
# @desc    : 网络编程，写一个简单的服务端
#

from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():
    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient


        def run(self):
            my_dict = {}
            my_dict['filename'] = 'haha.jpg'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()
    # 1.创建套接字
    server = socket()
    # 2.绑定IP地址和端口
    server.bind(('localhost', 8001))
    # 3.开启监听--监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('haha.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')

    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()