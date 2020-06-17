import pygame
from plane_sprites import *

#   初始化
pygame.init()

# 创建时钟对象
clock = pygame.time.Clock()

#   创建游戏窗口
screen = pygame.display.set_mode((480, 700))

#   绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

#   绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

#   在绘制工作完成后，统一调用update方法
pygame.display.update()

#   1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)

#   创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

#   创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

#   游戏循环 >>> 意味着正式的游戏开始
while True:
    #   可以在循环体内部的代码执行的频率
    clock.tick(60)

    #   捕获事件
    # event_list = pygame.event.get()

    #   事件监听
    for event in pygame.event.get():
        #   判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏")

            #   quit卸载所以模块
            pygame.quit()

            #   退出系统
            exit()
        elif event.type == 'a':
            hero_rect.x -= 10

    # if len(event_list) > 0:
    #     print(event_list)

    #   修改飞机位置
    hero_rect.y -= 5

    if hero_rect.y <= -126:
        hero_rect.y = 700

    #   调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    #   让精灵组调用两个方法
    #   update - 让组中所以精灵更新位置
    enemy_group.update()
    #   draw - 在screen上绘制所有的精灵
    enemy_group.draw(screen)

    #   调用update方法更新显示
    pygame.display.update()

#   结束
# pygame.quit()
