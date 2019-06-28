# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/6/29 00:14
# @file    : leap.py
# @desc    : 输入年份，如果是闰年输出True, 否则输出False
#

year = int(input('请输入年份： '))
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
