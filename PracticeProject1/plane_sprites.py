import random
import pygame

#   屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#   刷新屏幕帧率的常量
FRAME_PER_SECOND = 60
#   创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#   英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


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

    @staticmethod
    def image_names(prefix, count):
        names = []
        for i in range(1, count + 1):
            names.append("./images/" + prefix + str(i) + ".png")
        return names


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


class PlaneSprite(GameSprite):

    def __init__(self, image_names, destroy_names, life, speed):

        image_name = image_names[0]
        super().__init__(image_name, speed)

        #   生命值
        self.life = life

        #   正常图像列表
        self.__life_images = []
        for file_name in image_names:
            image = pygame.image.load(file_name)
            self.__life_images.append(image)

        #   被摧毁的图像列表
        self.__destroy_images = []
        for file_name in destroy_names:
            image = pygame.image.load(file_name)
            self.__destroy_images.append(image)

        #   默认播放生存图像列表
        self.images = self.__life_images
        #   显示图像索引
        self.show_image_index = 0
        #   是否循环播放
        self.is_loop_show = True
        #   是否可以被删除
        self.can_destroied = False

    def update(self):
        self.update_image()
        super().update()

    def update_image(self):
        """更新图像"""

        pre_index = int(self.show_image_index)
        self.show_image_index += 0.05
        count = len(self.images)

        #   判断是否循环播放
        if self.is_loop_show:
            self.show_image_index %= len(self.images)
        elif self.show_image_index > count - 1:
            self.show_image_index = count - 1
            self.can_destroied = True

        current_index = int(self.show_image_index)

        if pre_index != current_index:
            self.image = self.images[current_index]

    def destroied(self):
        #   飞机摧毁

        #   默认播放生存图片
        self.images = self.__destroy_images
        #   显示图像索引
        self.show_image_index = 0
        #   是否循环
        self.is_loop_show = False


class Enemy(PlaneSprite):
    """敌机精灵"""

    def __init__(self):
        #   调用父类方法，实现敌人的创建
        images_name = ["./images/enemy1.png"]
        destroy_names = GameSprite.image_names("enemy1_down", 4)
        super().__init__(images_name, destroy_names, 1, 1)
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

        #   判断敌机是否已经销毁
        if self.can_destroied:
            self.kill()

    def __del__(self):
        # print("敌机消失 %s" % self.rect)\
        pass


class Hero(PlaneSprite):
    """英雄精灵"""

    def __init__(self):
        #   调用父类方法, 设置img&speed
        images_name = GameSprite.image_names("me", 2)
        destroy_names = GameSprite.image_names("me_destroy_", 4)

        super().__init__(images_name, destroy_names, 3, 0)

        #   设定英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom
        self.speed2 = 0

        #   创建子弹的精灵组
        self.bullets = pygame.sprite.Group()
        self.bullets_mod = False

    def update(self):

        self.update_image()
        #   英雄的方向移动
        self.rect.x += self.speed
        self.rect.y += self.speed2

        #   控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
        elif self.rect.y < 350:
            self.rect.y = 350

    def fire(self):

        if self.bullets_mod:
            pygame.time.set_timer(HERO_FIRE_EVENT, 600)

            #   子弹双联三连发模式
            for i in (0, 1, 2):
                #   创建子弹精灵
                bullet = Bullet()
                bullet2 = Bullet()
                #   设置精灵位置
                bullet.rect.bottom = self.rect.y + i * 25
                bullet.rect.centerx = self.rect.centerx - 32

                bullet2.rect.bottom = self.rect.y + i * 25
                bullet2.rect.centerx = self.rect.centerx + 32

                self.bullets.add(bullet, bullet2)
            return

        #   子弹单发模式
        pygame.time.set_timer(HERO_FIRE_EVENT, 200)
        bullet3 = Bullet()
        bullet3.rect.bottom = self.rect.y
        bullet3.rect.centerx = self.rect.centerx

        self.bullets.add(bullet3)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        #   调用父类方法
        image_name = "./images/bullet1.png"
        super().__init__(image_name, -5)

    def update(self, *args):
        #   调用父类方法，让子弹垂直飞行
        super().update(*args)
        #   判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹被销毁...")
        pass
