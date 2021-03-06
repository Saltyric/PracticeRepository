#!usr/bin/env python
# *-*coding:utf-8*-*
import pygame
from plane_sprites import *


class PlanGame(object):
    """皇牌空战？？主游戏"""

    def __init__(self):
        print("游戏初始化")
        pygame.init()

        #   设置得分与暂停变量
        self.score = 0
        self.pause = False

        #   创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #   设置程序标题
        pygame.display.set_caption("Ace Combat？？ ———— By Saltyric")

        #   初始化音乐
        pygame.mixer.init()
        self.__bgm()

        #   创建游戏时钟
        self.clock = pygame.time.Clock()
        #   调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        #   设置定时器事件 -创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(CREATE_ENEMY_ELITE_EVENT, 5000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 150)
        pygame.time.set_timer(ENEMY_FIRE_EVENT, 3000)

    def __create_sprites(self):
        #   创建背景精灵与精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_ground = pygame.sprite.Group(bg1, bg2)

        #   创建敌机精灵与精灵组
        self.enemy_group = pygame.sprite.Group()
        self.enemy_elite_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()

        #   创建英雄精灵与精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        self.destroy_group = pygame.sprite.Group()

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
            #   更新文本面板
            self.__text_display()
            #   更新显示
            pygame.display.update()

    def __event_handler(self):

        key_press = pygame.key.get_pressed()
        for event in pygame.event.get():
            #   判断是否退出游戏
            if event.type == pygame.QUIT:
                PlanGame.__game_over()
                # self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                #   创建敌机
                self.enemy_group.add(Enemy())
            elif event.type == CREATE_ENEMY_ELITE_EVENT:
                self.enemy_elite_group.add(EnemyElite())
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            elif event.type == ENEMY_FIRE_EVENT:
                for each in self.enemy_elite_group:
                    for i in (0, 1, 2):
                        self.enemy_bullet_group.add(EnemyBullet(each.rect.centerx, each.rect.bottom+i*15))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.pause = True
                self.__game_pause()
            #   使用空格切换两种攻击模式
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.hero.bullets_mod = not self.hero.bullets_mod
            #   press B to ANLA-AHM-AKBAR!!!!
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                self.hero.destroied()
                for enemies in self.enemy_group.sprites():
                    enemies.destroied()
                for enemies_elite in self.enemy_elite_group.sprites():
                    enemies_elite.destroied()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.__init__()

        #   使用键盘提供的方法获取键盘按键 - 按键元组
        if key_press[pygame.K_RIGHT] or key_press[pygame.K_d]:
            # print("向右移动")
            self.hero.speed = 2
        elif key_press[pygame.K_LEFT] or key_press[pygame.K_a]:
            self.hero.speed = -2
        elif key_press[pygame.K_UP] or key_press[pygame.K_w]:
            self.hero.speed2 = -3
        elif key_press[pygame.K_DOWN] or key_press[pygame.K_s]:
            self.hero.speed2 = 2
        else:
            self.hero.speed = 0
            self.hero.speed2 = 0

        # if key_press[pygame.K_SPACE]:
        #     self.hero.fire()

        # 判断英雄是否已经被销毁，如果是，游戏结束
        if self.hero.can_destroied:
            PlanGame.__game_over()

    def __check_collide(self):
        #   子弹摧毁敌机
        enemies = pygame.sprite.groupcollide(self.enemy_group, self.hero.bullets, False, True)

        for enemy in enemies:
            enemy.life -= 1

            if enemy.life <= 0:
                enemy.add(self.destroy_group)
                enemy.remove(self.enemy_group)
                self.score += 1

            enemy.destroied()

        elite = pygame.sprite.groupcollide(self.enemy_elite_group, self.hero.bullets, False, True)

        for enemy2 in elite:
            enemy2.life -= 1

            if enemy2.life <= 0:
                enemy2.add(self.destroy_group)
                enemy2.remove(self.enemy_elite_group)
                self.score += 3
            enemy2.destroied()

        #   判断子弹是否对撞
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_bullet_group, True, True)

        #   敌机撞毁英雄
        for hit in pygame.sprite.spritecollide(self.hero, self.enemy_group, True):
            self.hero.life -= 1

            if self.hero.life <= 0:
                print("Aircraft Crashed!!")
                self.hero.destroied()

        for hit2 in pygame.sprite.spritecollide(self.hero, self.enemy_bullet_group, True):
            self.hero.life -= 1

            if self.hero.life <= 0:
                self.hero.destroied()

    def __update_sprites(self):

        for group in [self.back_ground,
                      self.enemy_group,
                      self.enemy_elite_group,
                      self.hero_group,
                      self.hero.bullets,
                      self.destroy_group,
                      self.enemy_bullet_group]:
            group.update()
            group.draw(self.screen)

    def __game_pause(self):
        #   暂停功能实现
        pygame.mixer.music.set_volume(0.2)

        #   设置文本
        self.text_font = pygame.font.SysFont("comicsansms", 80)
        self.pause_text = self.text_font.render("PAUSE", False, (0, 0, 0))

        self.pause_image = pygame.image.load(PAUSE_IMAGE)
        self.pause_image_rect = self.pause_image.get_rect()
        self.pause_image_rect.centerx = SCREEN_RECT.centerx
        self.pause_image_rect.centery = SCREEN_RECT.centery
        self.screen.blit(self.pause_image, (self.pause_image_rect.x, self.pause_image_rect.y))

        while self.pause:
            self.screen.blit(self.pause_text, (SCREEN_RECT.width / 2 - 130, SCREEN_RECT.height / 2 - 140))
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.__game_over()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.pause = False
                    pygame.mixer.music.set_volume(0.5)

    def __text_display(self):
        #   文本更新实现
        self.score_font = pygame.font.SysFont("comicsansms", 20)
        self.score_font.set_bold(True)
        self.score_text = self.score_font.render("Score: %d" % self.score, True, COLOR_WHITE)
        self.screen.blit(self.score_text, (0, 0))

        self.life_font = pygame.font.SysFont("comicsansms", 20)
        self.life_font.set_bold(True)
        self.life_text = self.score_font.render("Life: %d" % self.hero.life, True, COLOR_WHITE)
        self.screen.blit(self.life_text, (0, 20))

        self.help_font = pygame.font.SysFont("comicsansms", 20)
        self.help_text = self.help_font.render("Press (P) Pause", True, COLOR_WHITE)
        self.screen.blit(self.help_text, (0, SCREEN_RECT.bottom-30))

    @staticmethod
    def __bgm():

        pygame.mixer.music.load("./Charge Assault.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':
    #   启动游戏
    PlanGame().start_game()
