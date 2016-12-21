#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        井字游戏
        By Yanxingfei(1139),2016.09.10
"""


def print_board():
    """打印棋盘

    :return: None
    """
    for i in range(0, 3):
        for j in range(0, 3):  # 依次输出
            print(game_map[i][j], end="")  # py3如果要默认不换行，可通过end=""（空）来设置
            if j != 2:
                print("|", end="")
        print("")


def check_if_over():
    """检查是否游戏结束（出现三连珠获胜或盘满平局）

    :return: Bool
    """
    for i in range(0, 3):
        if game_map[i][0] == game_map[i][1] == game_map[i][2] != " " \
                or game_map[0][i] == game_map[1][i] == game_map[2][i] != " ":  # 三纵三横有相同
            print(turn, "won!!!")
            return True

    if game_map[0][0] == game_map[1][1] == game_map[2][2] != " " \
            or game_map[0][2] == game_map[1][1] == game_map[2][0] != " ":  # 斜向有相同
        print(turn, "won!!!")
        return True

    if " " not in game_map[0] and " " not in game_map[1] and " " not in game_map[2]:  # 棋盘下满了
        print("Draw")
        return True

    return False


if __name__ == '__main__':
    game_map = [  # 棋盘落子区，首先是第一行X的三列Y
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
    turn = "X"  # 该谁走棋
    game_over = False  # 游戏结束标志
    print("Please select position by typing in a number between 1 and 9, see below:")
    print("7|8|9")
    print("4|5|6")
    print("1|2|3")

    while not game_over:  # 进行游戏
        print_board()
        print(turn, "'s turn")

        player_moved = False  # 轮到某个人还未走棋
        while not player_moved:  # 走棋
            try:
                pos = int(input("Select:"))  # 玩家输入的落棋点，str强制转化到int
                if 1 <= pos <= 9:  # 如果输入有效，让键盘输入和棋盘位置对应起来
                    X = pos // 3  # 第一步行对应：12结果为0，45结果为1，78结果为2，369结果为比同行大1（需调整）
                    Y = pos % 3 - 1  # 第一步列对应：147结果为0，258结果为1，369结果为-1（需调整）
                    if Y == -1:  # 对应第2列
                        Y += 3  # 369的列值调整为2
                        X -= 1  # 369的行值调整为与同行相同
                    if X == 0:
                        X += 2
                    elif X == 2:
                        X -= 2

                    if game_map[X][Y] == " ":  # 如果没放棋子就放
                        game_map[X][Y] = turn
                        player_moved = True  # 已走棋
                        game_over = check_if_over()  # 检查是否结束游戏
                        if not game_over:  # 转换棋手
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
            except:
                print("Warning! You need to add a numeric value")
