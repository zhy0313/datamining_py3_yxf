#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        测试
        By Yanxingfei(1139),2016.08.10
"""


print('===============start test=================')
import pygame
from pygame.locals import *
import math
import random
import os
import sys
print(os.getcwd())

print(sys.path)
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

#获取绝对路径
BASE_DIR=os.path.dirname(__file__)
file_path=os.path.join(BASE_DIR,"rabbit_game_resources/images")
# 3 - Load images
player = pygame.image.load(file_path+"/dude.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player, (100, 100))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
print('================end test==================')
