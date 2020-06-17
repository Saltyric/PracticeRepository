import pygame
from plane_sprites import *


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
        #   设置定时器事件 -创建敌机  1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):
        #   创建背景精灵与精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_ground = pygame.sprite.Group(bg1, bg2)

        #   创建敌机精灵与精灵组
        self.enemy_group = pygame.sprite.Group()

        #   创建英雄精灵与精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")
        while True:
            #   设置刷新帧率
            self.clock.tick(FRAME_PER_SECOND)
            #   事件监听
            self.__event_handler()
            #   碰撞检测
            self.__check_collide()
            #   更新/绘制精灵组
            self.__update_sprites()
            #   更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():
            #   判断是否退出游戏
            if event.type == pygame.QUIT:
                PlanGame.__game_over()
                # self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场...")
                #   创建敌机精灵
                enemy = Enemy()
                #   将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
        #   使用键盘提供的方法获取键盘按键 - 按键元组
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_RIGHT] and self.hero.rect.x <= (SCREEN_RECT.width - self.hero.rect.width):
            # print("向右移动")
            self.hero.speed = 2
        elif key_press[pygame.K_LEFT] and self.hero.rect.x >= 0:
            self.hero.speed = -2
        elif key_press[pygame.K_UP] and self.hero.rect.y >= 350:
            self.hero.speed2 = -3
        elif key_press[pygame.K_DOWN] and self.hero.rect.y <= 500:
            self.hero.speed2 = 2
        else:
            self.hero.speed = 0
            self.hero.speed2 = 0

        if self.hero.speed2 == 0 and self.hero.rect.y <= 500:
            self.hero.rect.y += 1

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_ground.update()
        self.back_ground.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':
    #   创建游戏对象
    game = PlanGame()
    #   启动游戏
    game.start_game()
