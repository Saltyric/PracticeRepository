import random
import pygame

#   屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#   刷新屏幕帧率的常量
FRAME_PER_SECOND = 60
#   创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT


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

    def __init__(self, is_alt=False):
        #   调用父类方法，实现background的创建(image/rect/speed)
        super().__init__("./images/background.png")
        #   判断是否为交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        #   调用父类方法实现
        super().update()

        #   判断是否移出屏幕,如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        #   调用父类方法，实现敌人的创建
        super().__init__("./images/enemy1.png")
        #   指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        #   指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        #   调用父类方法实现 保持垂直飞行
        super().update()
        #   判断是否飞出屏幕，如果是，需要从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要删除")
            #   kil方法可以将精灵从所以精灵组中移出，精灵会被自动销毁
            self.kill()

    def __del__(self):
        # print("敌机消失 %s" % self.rect)\
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        #   调用父类方法, 设置img&speed
        super().__init__("./images/me1.png", 0)
        #   设定英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.speed2 = 0

    def update(self):
        #   英雄在水平方向移动
        self.rect.x += self.speed
        self.rect.y += self.speed2

    def fire(self):
        pass


class Bullet(GameSprite):

    def __init__(self):
        #   调用父类方法
        super().__init__("./images/bullet1.png")
        #   子弹初始
        self.speed = -2

    def update(self):
        super().update()
        self.rect.y += self.speed
