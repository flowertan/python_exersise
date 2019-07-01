# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/1 22:07
# @file    : odd.py
# @desc    : 计算1～100的奇数之和
#

sum = 0

for index in range(1, 100, 2):
    sum += index

print('1~100的奇数之和为：%d' % sum)



