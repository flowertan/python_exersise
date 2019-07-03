# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/3 21:03
# @file    : number_insert.py
# @desc    : 输入一个正整数，把数字的每一位用0隔开
#


def add_zero(num):
    new_num = "0".join(num)
    # print(new_num)
    return new_num


def main():
    num = input('请输入数字：\n')
    print(add_zero(num))


if __name__ == '__main__':
    main()
