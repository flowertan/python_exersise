# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/6/29 00:09
# @file    : round.py
# @desc    : 根据圆的半径计算周长和面积
#
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius

print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)