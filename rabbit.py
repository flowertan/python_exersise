# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2018/7/27 15:17
# @file    : rabbit.py
# @desc    : 有若干只鸡和兔同在一个笼子里，从上面数，有35个头，从下面数，有94只脚。问笼中各有              多少只鸡和兔？
#
from sympy import *
def result_output(m, n):
    c = Symbol('c')
    r = Symbol('r')
    result = solve([c + r - m, 2 *c + 4 * r - n], [c, r])
    c, r = result.values()
    if c > 0 and r > 0:
        print('cocks %d rabbits %d' % (c, r))
    else:
        print('invalid input')

def main():
    m = input('请输入头的个数：')
    n = input('请入脚的个数： ')
    result_output(int(m), int(n))

if __name__ == '__main__':
    main()