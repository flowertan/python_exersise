# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/6/29 00:02
# @file    : fahrenheit.py
# @desc    : 华氏温度转换为摄氏温度
#            F = 1.8C + 32
#

f = float(input('please input a F: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %1.f摄氏度' % (f, c))
