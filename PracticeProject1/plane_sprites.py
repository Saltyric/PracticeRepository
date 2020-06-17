import pygame

#   屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#   刷新屏幕帧率的常量
FRAME_PER_SECOND = 60


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        #   调用父类的初始化方法
        super().__init__()
        #   定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        #   在屏幕的垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def update(self):
        #   调用父类方法实现
        super().update()

        #   判断是否移出屏幕,如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
    #
    # def __init__(self, is_alt):
    #     super().__init__()