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

i = 0
#   游戏循环 >>> 意味着正式的游戏开始
while True:
    clock.tick(60)
    i += 1
    print(i)

#   结束
pygame.quit()

