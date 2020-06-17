import pygame
from plane_sprites import *

#   屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)


class PlanGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        #   创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #   创建游戏时钟
        self.clock = pygame.time.Clock()
        #   调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("游戏开始...")
        while True:
            for event in pygame.event.get():
                #   判断用户是否点击了关闭按钮
                if event.type == pygame.QUIT:
                    print("退出游戏")

                    #   quit卸载所以模块
                    pygame.quit()

                    #   退出系统
                    exit()


if __name__ == '__main__':
    #   创建游戏对象
    game = PlanGame()
    #   启动游戏
    game.start_game()
