# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/4 22:02
# @file    : phonebook.py
# @desc    : 在控制台运行的通讯录工具，包含「录入」,「查找」,「全部显示」,删除」,「保存」
#

import csv
person = []
person_id = 0
headers = ['id', 'name', 'tel', 'email']


def save(person):
    with open("phonebook.csv", 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, headers)
        writer.writeheader()
        print(person)
        for one in person:
            print(one)
            writer.writerow(one)
    print('联系人保存成功！')



def load():
    global person
    global person_id
    person = []
    try:
        csvfile = open('phonebook.csv', 'r')
    except:
        print('文件还没有呢，别着急！！！')
    else:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person.append(row)
            person_id = int(row['id'])

    finally:
        csvfile.close()

def add():
    load()
    person_info = {}
    global person_id
    person_id += 1
    name = input('姓名: ')
    tel = input('手机：')
    email = input('邮箱: ')
    person_info['id'] = person_id
    person_info['name'] = name
    person_info['tel'] = tel
    person_info['email'] = email
    person.append(person_info)
    print('联系人添加成功')


def find():
    load()
    key = input('查询关键值: ')
    for one in person:
        for index in one.values():
            if key in index:
                print(one['id'], one['name'], one['tel'], one['email'])
                break


def show():
    load()
    for index in person:
        print(index['id'], index['name'], index['tel'], index['email'])


def delete():
    load()
    id = input('联系人ID: ')
    for one in person:
        if id in one.values():
            print(one['id'], one['name'], one['tel'], one['email'])
            break
    option = input('确认删除此联系人？(y/[n])')
    if option == 'y':
        del person[int(id) - 1]
        save(person)
        show()
        print('删除联系人成功')
    else:
        print('不需要删除')


def main():
    while True:
        option = input("请选择：1.录入 2.查找 3.全部显示 4.删除(回车退出) 5.保存\n")
        if option == 'q':
            break
        if option == '1':
            add()
        elif option == '2':
            find()
        elif option == '3':
            show()
        elif option == '4':
            delete()
        elif option == '5':
            save()
        else:
            print('无效值！！！')

    print("exit")


if __name__ == '__main__':
    main()