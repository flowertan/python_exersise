# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/14 20:58
# @file    : Hero.py
# @desc    : 英雄与小兵的游戏，面向对象的思想
#

import random

class roleplay(object):
    # 定义英雄与小兵的共同属性
    def __init__(self, name, hp, dmg, mov):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.mov = mov


    def __str__(self):
        return ('生命值：%d 攻击力：%d 移动速度：%d' % (self.hp, self.dmg, self.mov))


    def attack(self, role):
        # 士兵攻击
        if isinstance(role, hero):
            role.hp -= self.dmg
            print('%d生命值：%d' % (self.name, self.hp))
            print('%d生命值：%d' % (role.name, role.hp))
        elif isinstance(role, soldier):
            role.hp -= self.dmg
            print('%d生命值：%d' % (self.name, self.hp))
            print('%d生命值：%d' % (role.name, role.hp))


    def islive(self):
        if self.hp <= 0:
            return 0
        else:
            return 1

    def movto(self):
        pass


class hero(roleplay):
    '''
    hero
    生命值：500
    攻击力：50
    移动速度：20
    魔法值：200
    '''

    def __init__(self, mp=200):
        super(hero, self).__init__('hero', 500, 50, 20)
        self.mp = mp

    def __str__(self):
        return ('生命值：%d 攻击力：%d 移动速度：%d' % (self.hp, self.dmg, self.mov))

    def cast_attack(self, role):
        # 使用魔法攻击别人时，自身魔法值会减少，魔法攻击/40mp
        role.hp -= self.dmg * 1.5
        print('英雄发动魔法攻击啦！')
        self.mp -= 40

class soldier(roleplay):
    '''
    小兵
    生命值：150
    攻击力：25
    移动速度：10
    '''

    def __init__(self):
        super(soldier, self).__init__('soldier', 150, 25, 10)

def main():
    option = input('请选择你的角色：1 英雄 2 小兵（回车退出）:')
    while option in set(['1', '2', '']):
        if option == '1':
            player = hero()
            computer = soldier()
            print('初始化状态')
            print('英雄', player)
            print('小兵', computer, '\n', '==' * 20)
            play_times = 1
            while player.hp != 0 and computer.hp != 0:
                print('==' * 10, '第%d回合' % play_times, '==' * 10)
                if player.mp >= 40 and player.hp > 0:
                    attack_option = input('1:普通攻击 2:魔法攻击(默认普通攻击)')
                    if attack_option == '' or attack_option == '':
                        player.attack(computer)
                    else:
                        player.cast_attack(computer)

                    if computer.islive():
                        if random.randint(1, 2) == 1:
                            computer.attack(player)
                        else:
                            computer.movto()

                        if player.islive():
                            play_times += 1
                        else:
                            print('英雄死翘翘了')

                    else:
                        print('小兵死了')
                if player.mp < 40 and player.hp > 0:
                    attack_option = input('1:攻击 2:移动(默认攻击)')
                    if attack_option == '1' or attack_option == '':
                        player.attack(computer)
                    elif attack_option == '2':
                        player.movto()

                    if computer.islive():
                        if random.randint(1, 2) == 1:
                            computer.attack(player)
                        else:
                            computer.movto()

                        if player.islive():
                            play_times += 1
                        else:
                            print('英雄死翘翘了')

                    else:
                        print('小兵死了')

                print('生命值：%d 魔法值：%d' % (player.hp, player.mp))
                print('生命值：%d' % computer.hp)
            option = input('要继续吗，1 英雄 2 小兵（回车退出）:')

        elif option == '2':
            pass
            break
        elif option == '':
            print('游戏结束')
            break
    else:
        print('无效值')


if __name__ == '__main__':
    main()
