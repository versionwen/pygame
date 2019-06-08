import pygame
from plane_sprites import *
class PlaneGame(object):
    #飞机大战主游戏
    def __init__(self):
        print("游戏初始化")
        #窗口，时钟，私有方法
        self.screen=pygame.display.set_mode(SCREEN_RECT.size)
        self.clock=pygame.time.Clock()
        self._creat_sprites()
        #创建敌人飞机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)
    def _creat_sprites(self):
        #创建背景精灵和精灵组
        bg1=Background()
        bg2 = Background(True)
        self.back_group=pygame.sprite.Group(bg1,bg2)
        self.enemy_group=pygame.sprite.Group()
        self.hero=Hero()
        self.hero_group=pygame.sprite.Group(self.hero)
    def start_game(self):
        print("游戏开始")
        while True:
            #刷新帧，事件监听，碰撞检测，绘制精灵组，更新显示
            self.clock.tick(FRAME_PER_SEC)
            self._event_handler()
            self._check_collide()
            self._update_sprites()
            pygame.display.update()
    def _event_handler(self):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    PlaneGame._game_over()
                elif event.type==CREATE_ENEMY_EVENT:
                    print("敌人飞机")
                    enemy=Enemy()
                    self.enemy_group.add(enemy)
                # elif event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
                #     print("向右移动")
                elif event.type==HERO_FIRE_EVENT:
                    self.hero.fire()
            key_pressed=pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                self.hero.speed=3
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed=-3
            else:
                self.hero.speed=0
    def _check_collide(self):
            pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
            enemies= pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
            if len(enemies)>0:
                self.hero.kill()
                PlaneGame._game_over()
    def _update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
    @staticmethod
    def _game_over():
        print("游戏结束")
        pygame.quit()
        exit()
if __name__ == '__main__':
    game=PlaneGame()
    game.start_game()
