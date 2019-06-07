import pygame
#定义屏幕大小的常量
SCREEN_RECT=pygame.Rect(0,0,480,800)
#刷新帧
FRAME_PER_SEC=60
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