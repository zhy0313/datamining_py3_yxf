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
            # 3.test baidu tieba   #
            # 4.test weibo         #
            # 5.test wechat        #
            # 6.test douban        #
            # 7.update proxy pool  #
            # 8.EXIT               #
            ''')
        try:
            s1 = int(input("Select:"))
            if s1 == 1:
                menu1(sys_type)  # 调用次级菜单
            elif s1 == 2:
                call(sys_type, "python zhihu/test/test_zhihu.py")
                pass
            elif s1 == 3:
                call(sys_type, "python baidu_tieba/test/test_baidu_tieba.py")
                pass
            elif s1 == 4:
                call(sys_type, "python weibo/test/test_weibo.py")
                pass
            elif s1 == 5:
                call(sys_type, "python wechat/test/test_wechat.py")
                pass
            elif s1 == 6:
                call(sys_type, "python douban/test/test_douban.py")
                pass
            elif s1 == 7:
                call(sys_type, "python common/proxy.py")
            elif s1 == 8:
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
            s2 = int(input("Select:"))
            if s2 == 1:
                if sys_type == "win":
                    call(sys_type, "rasdial 校园网宽带 18861824721@cmcc 252513")  # 宽带连接。断开：rasdial 校园网宽带 /disconnect
                    pass
                else:
                    print("Warning! It's only a windows command!")
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
