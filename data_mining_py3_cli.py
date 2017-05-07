#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        整体CLI入口
        By Yanxingfei(1139),2016.09.10
"""

# build-in
import os


def call(sys_type, command):  # 与操作系统解耦
    if sys_type == "win":  # windows系统下的命令
        os.system("cmd /k " + command)
    elif sys_type == "unix":  # unix类系统下的命令
        os.system(command)


def main(sys_type):  # 主菜单
    while True:
        print('''
            #---------MENU---------#
            # 1.test               #
            # 2.test zhihu         #
            # 3.update proxy pool  #
            # 4.EXIT               #
            ''')
        try:
            s1 = int(input("请选择："))
            if s1 == 1:
                menu1(sys_type)  # 调用次级菜单
            elif s1 == 2:
                call(sys_type, "python zhihu/test_zhihu.py")
                pass
            elif s1 == 3:
                call(sys_type, "python proxy/test_proxy.py")
            elif s1 == 4:
                break  # 跳出循环即结束整个程序
        except:
            print("警告！您输入的不是有效数字！")
            pass


def menu1(sys_type):  # 次级菜单
    while True:
        print('''
            #---------MENU1_1------#
            # 1.test               #
            # 2.tic-tac-toe game   #
            # 3.rabbit game        #
            # 4.return to MENU1    #
            ''')
        try:
            s2 = int(input("请选择："))
            if s2 == 1:
                # call(sys_type, "rasdial 校园网宽带 18861824721@cmcc 252513")  # 宽带连接。断开：rasdial 校园网宽带 /disconnect
                call(sys_type, "python test/test.py")
                pass
            elif s2 == 2:
                call(sys_type, "python test/tic-tac-toe_game.py")
                pass
            elif s2 == 3:
                call(sys_type, "python test/rabbit_game.py")
                pass
            elif s2 == 4:
                break  # 跳出循环即返回菜单1
        except:
            print("警告！您输入的不是有效数字！")
            pass


if __name__ == '__main__':  # 程序入口
    main("win")  # 调用主菜单
