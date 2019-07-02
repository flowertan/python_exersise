# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/2 21:46
# @file    : reverse.py
# @desc    : 将输入的的整数反着输出
#

def reverse(str):
    temp = []
    for i in range(0, len(str)):
        # 从头部将字符串插入列表
        temp.insert(0, str[i])
    # print(int("".join(temp)))
    # 将列表转换为字符串，再转换为整型输出
    result = int("".join(temp))
    return result

def main():
    str = input('请输入一个整数：\n')
    result = reverse(str)
    print(result)

if __name__ == '__main__':
    main()
