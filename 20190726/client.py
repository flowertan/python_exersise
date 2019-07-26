# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/26 22:07
# @file    : client.py
# @desc    : 网络编程套接字写一个客户端
#

from socket import socket, SOCK_STREAM, AF_INET
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(('localhost', 8001))
    in_data = bytes()
    # 不不知道服务发送的数据每次有多大，定义每次接收1024 byte
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)

    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/Users/flower/' + filename, 'wb') as f:
        f.write(b64decode(filedata))
    print('图片已保存')

if __name__ == '__main__':
    main()