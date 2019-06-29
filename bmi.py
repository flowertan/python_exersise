# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/6/29 22:54
# @file    : bmi.py
# @desc    : BMI 指数（即身体质量指数，简称体质指数，英文为Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字
#
height = float(input('请输入你的身高(m):\n'))
weight = float(input('请输入你的体重(Kg):\n'))
bmi = weight / (height * height)
print('你的BMI指数为%.2f' % bmi)

