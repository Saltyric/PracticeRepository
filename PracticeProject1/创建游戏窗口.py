import pygame

#   初始化
pygame.init()

#   创建游戏窗口
screen = pygame.display.set_mode((480,700))

#   绘制背景图像
#   1.加载图像数据
bg = pygame.image.load("./images/background.png")
#   2.blit 绘制图像
screen.blit(bg, (0, 0))
#   3.更新图像
# pygame.display.update()

#   绘制英雄图像
#   1.加载图像数据
hero = pygame.image.load("./images/me1.png")
#   2.blit 绘制图像
screen.blit(hero, (200, 500))
#   3.更新图像
pygame.display.update()

while True:
    for event in pygame.event.get():
        #   判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏")

            #   quit卸载所以模块
            pygame.quit()

            #   退出系统
            exit()


#   结束
pygame.quit()