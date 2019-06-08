import random
import pygame
#定义屏幕大小的常量
SCREEN_RECT=pygame.Rect(0,0,480,800)
#刷新帧
FRAME_PER_SEC=60
#敌人飞机定时器
CREATE_ENEMY_EVENT=pygame.USEREVENT
#发射子弹
HERO_FIRE_EVENT=pygame.USEREVENT+1
class GameSprite(pygame.sprite.Sprite):
    #定义对象属性
    def __init__(self,image_name,speed=1):
        super().__init__()
        self.image=pygame.image.load(image_name)
        self.rect=self.image.get_rect()
        self.speed=speed
    def update(self):
        #在屏幕的垂直方向上移动
        self.rect.y+=self.speed
class Background(GameSprite):
    #游戏背景精灵
    def __init__(self,is_alt=False):
        #精灵创建
        super().__init__("./Resources/bg_01.png")
        #判断是否是交替图像
        if is_alt:
            self.rect.y=-self.rect.height
    def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y=-self.rect.height
class Enemy(GameSprite):
    #敌人飞机精灵
    def __init__(self):
        super().__init__("./Resources/enemy-1.png")
        self.speed=random.randint(1,3)
        self.rect.bottom=0
        max_x=SCREEN_RECT.width-self.rect.width
        self.rect.x=random.randint(0,max_x)
    def update(self):
        super().update()
        if self.rect.y>SCREEN_RECT.height:
            print("敌人飞机飞出去了")
            self.kill()
    def __del__(self):
        print("enemy is over")
class Hero(GameSprite):
    def __init__(self):
        super().__init__("./Resources/hero.png",0)
        self.rect.center=SCREEN_RECT.center
        self.rect.bottom=SCREEN_RECT.bottom-120
        self.bullets=pygame.sprite.Group()
    def update(self):
        self.rect.x+=self.speed
        #控制移动不能离开屏幕
        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.right>SCREEN_RECT.right:
            self.rect.right=SCREEN_RECT.right
    def fire(self):
        for i in (0,1,2):
            bullet=Bullet()
            bullet.rect.bottom=self.rect.y-i*20
            bullet.rect.center=self.rect.center
            self.bullets.add(bullet)
class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./Resources/bullet-3.png",-3)
    def update(self):
        super().update()
        if self.rect.bottom<0:
            self.kill()
    def __del__(self):
        print("子弹被销毁")