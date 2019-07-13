# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/12 22:22
# @file    : contact.py
# @desc    : 用数据库来保存通讯录，实现的功能包含「录入」,「查找」,「全部显示」,删除」,「保存」
#

import sqlite3

person_id = 0
person = []


def add():
    global person_id
    name = input('姓名: ')
    tel = input('手机：')
    email = input('邮箱: ')
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM person')
    res = cursor.fetchall()
    for index in res:
        person_id = index[0]
    person_id += 1
    # person.append((person_id, name, tel, email))
    # 插入变量的格式要这样写，踩了好多坑，不能直接在问号处填变量的值，搞了好久，真的迷
    sql = "INSERT INTO person (id, name, tel, email) VALUES (?, ?, ?, ?)"
    try:
        cursor.execute(sql, (person_id, name, tel, email))
    except Exception as e:
        print(e)
    else:
        pass
        print('联系人添加成功')
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def find():
    key = input('查询关键值: ')
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM person')
    res = cursor.fetchall()
    # print(res)
    for one in res:
        # print(one)
        if key in one:
            print(one[0], one[1], one[2], one[3])

    cursor.close()
    conn.close()


def show():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM person')
    res = cursor.fetchall()
    for index in res:
        print(index[0], index[1], index[2], index[3])

    cursor.close()
    conn.close()


def delete():
    id = input('联系人ID: ')
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM person WHERE id=?', id)
    res = cursor.fetchall()
    print(res[0][0], res[0][1], res[0][2], res[0][3])
    option = input('确认删除此联系人？(y/[n])')
    if option == 'y':
        cursor.execute('DELETE FROM person WHERE id=?', id)
        conn.commit()
        cursor.close()
        conn.close()
        print('删除联系人成功')
    else:
        cursor.close()
        conn.close()
        print('不需要删除')

def init():
    try:
        print('start')
        conn = sqlite3.connect("contact.db")
        cursor = conn.cursor()
        sql = '''
              CREATE TABLE person (id INT PRIMARY KEY , name VARCHAR(20), tel VARCHAR(11), email VARCHAR(30) )
            '''
        cursor.execute(sql)
        cursor.close()
        conn.commit()
    except:
        print('数据库已经存在啦!')
    else:
        print("数据库创建成功\n")
    finally:
        conn.close()


def main():
    init()
    while True:
        option = input("请选择：1.录入 2.查找 3.全部显示 4.删除(回车退出)\n")
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
        else:
            print('无效值！！！')

    print("exit")


if __name__ == '__main__':
    main()