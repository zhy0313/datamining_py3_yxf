#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        整体CLI入口
        By Yanxingfei(1139),2016.09.10
"""

import os


def call(system, command):
    """
    与操作系统解耦
    :param system: 系统类型
    :param command: 命令
    :return:
    """
    if system == "win":  # windows系统下的命令
        os.system("cmd /k " + command)
    elif system == "unix":  # unix类系统下的命令
        os.system(command)


def menu1():
    """
    主菜单
    :return:
    """
    while True:
        print('''
            #---------MENU1--------#
            # 1.test douban        #
            # 2.test zhihu         #
            # 3.test baidu tieba   #
            # 4.test weibo         #
            # 5.test wechat        #
            # 6.test               #
            # 7.EXIT               #
            ''')
        try:
            s1 = int(input("Select:"))
            if s1 == 1:
                call("win","python douban/test/test_douban.py")
                pass
            elif s1 == 2:
                call("win","python zhihu/test/test_zhihu.py")
                pass
            elif s1 == 3:
                call("win","python baidu_tieba/test/test_baidu_tieba.py")
                pass
            elif s1 == 4:
                call("win","python weibo/test/test_weibo.py")
                pass
            elif s1 == 5:
                call("win","python wechat/test/test_wechat.py")
                pass
            elif s1 == 6:
                menu2()  # 调用菜单2
            elif s1 == 7:
                break  # 跳出循环即结束整个程序
        except:
            print("Warning! You need to add a numeric value")
            menu2()


def menu2():
    """
    次菜单
    :return:
    """
    while True:
        print('''
            #---------MENU2--------#
            # 1.test               #
            # 2.tic-tac-toe game   #
            # 3.rabbit game        #
            # 4.return to MENU1    #
            ''')
        try:
            s2 = int(input("Select:"))
            if s2 == 1:
                call("win", "python test/test.py")
                pass
            elif s2 == 2:
                call("win", "python test/tic-tac-toe_game.py")
                pass
            elif s2 == 3:
                call("win", "python test/rabbit_game.py")
                pass
            elif s2 == 4:
                break  # 跳出循环即返回菜单1
        except:
            print("Warning! You need to add a numeric value")


if __name__ == '__main__':  # 程序入口2
    menu1()  # 调用菜单1
