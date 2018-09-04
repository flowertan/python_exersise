# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2018/9/4 17:59
# @file    : analysis_friends.py
# @desc    : use wxpy to analysis friends simply
#

from wxpy import *
import matplotlib.pyplot as plt

# create a bot object
my_bot = Bot(cache_path='/Users/flower/python/workspace/python_exersise/wx/wxpy.pkl')

my_friends = my_bot.friends()
print(my_friends.stats_text())

sex_dic = {'boy':0, 'girl':0, 'other':0}
for friend in my_friends:
    if friend.sex == 1:
        sex_dic['boy'] += 1
    elif friend.sex == 2:
        sex_dic['girl'] += 1
    else:
        sex_dic['other'] += 1
print('男生{}个，女生{}个，未知性别{}个'.format(sex_dic['boy'], sex_dic['girl'], sex_dic['other']))
labels = ['boy', 'girl', 'other']
colors = ['red', 'yellow', 'green']
explode = (0.1, 0, 0)
plt.figure(figsize=(8, 5), dpi=80)
plt.axes(aspect=1)
print(list(sex_dic.values()))
plt.pie(list(sex_dic.values()), explode=explode, labels=labels,autopct='%1.2f%%', colors=colors, labeldistance=1.1, shadow=True, startangle=90, pctdistance=0.6)

plt.title('SEX ANALYSIS', bbox=dict(facecolor='g', edgecolor='blue', alpha=0.65 ))
plt.savefig('sex_analysis.jpg')
plt.show()