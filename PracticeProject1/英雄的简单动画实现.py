import pygame

#   初始化
pygame.init()

#创建时钟对象
clock = pygame.time.Clock()

#   创建游戏窗口
screen = pygame.display.set_mode((480,700))

#   绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

#   绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

#   在绘制工作完成后，统一调用update方法
pygame.display.update()

#   1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)

#   游戏循环 >>> 意味着正式的游戏开始
while True:
    #   可以在循环体内部的代码执行的频率
    clock.tick(1)

    #   修改飞机位置
    hero_rect.y -= 50

    #   调用blit方法绘制图像
    screen.blit(hero, hero_rect)

    #   调用update方法更新显示
    pygame.display.update()

#   结束
pygame.quit()

