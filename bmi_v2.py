# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/6/30 20:04
# @file    : bmi_v2.py
# @desc    : 计算出BMI指数并且根据标准输出健康状态
#


health_state = ['偏廋', '正常', '过重', '肥胖', '重度肥胖', '极重度肥胖']

def output_state(bmi, index):
    print('你的BMI指数为 %.2f, 身体状态为 %s' % (bmi, health_state[index]))

def calculate_state(style, bmi):
    if style == 1:
        if bmi > 0 and bmi < 18.5:
            output_state(bmi, 0)
        elif bmi >= 18.5 and bmi < 25:
            output_state(bmi, 1)
        elif bmi >= 25 and bmi < 30:
            output_state(bmi, 2)
        elif bmi >= 30 and bmi < 35:
            output_state(bmi, 3)
        elif bmi >= 35 and bmi < 40:
            output_state(bmi, 4)
        elif bmi >= 40:
            output_state(bmi, 5)
        else:
            print("无效的值")
    elif style == 2:
        if bmi > 0 and bmi < 18.5:
            output_state(bmi, 0)
        elif bmi >= 18.5 and bmi < 23:
            output_state(bmi, 1)
        elif bmi >= 23 and bmi < 25:
            output_state(bmi, 2)
        elif bmi >= 25 and bmi < 30:
            output_state(bmi, 3)
        elif bmi >= 30:
            output_state(bmi, 4)
        else:
            print("无效的值")
    elif style == 3:
        if bmi > 0 and bmi < 18.5:
            output_state(bmi, 0)
        elif bmi >= 18.5 and bmi < 24:
            output_state(bmi, 1)
        elif bmi >= 24 and bmi < 28:
            output_state(bmi, 2)
        elif bmi >= 28:
            output_state(bmi, 3)
        else:
            print("无效的值")
    else:
        print("无效的值")

def main():
    while True:
        start = input("要开始测试吗？（Y/N）：\n")
        if start == 'N':
            break
        height = float(input('请输入你的身高（米）:\n'))
        weight = float(input('请输入你的体重(公斤):\n'))
        style = int(input('请选择标准（1.国际标准 2.亚洲标准 3.中国标准）:\n'))
        BMI = weight / (height * height)
        calculate_state(style, BMI)

if __name__ == '__main__':
    main()
