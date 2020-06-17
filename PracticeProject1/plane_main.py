import pygame
from plane_sprites import *

#   屏幕大小的常量
SCREEN_RECT = pygame(0, 0, 480, 700)

class PlanGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        #   创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT)
        #   创建游戏时钟
        self.clock = pygame.time.Clock()
        #   调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("游戏开始...")


if __name__ == '__main__':
    #   创建游戏对象
    game = PlanGame()
    #   启动游戏
    game.start_game()
