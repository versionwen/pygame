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
    def _creat_sprites(self):
        #创建背景精灵和精灵组
        bg1=Background()
        bg2 = Background(True)
        self.back_group=pygame.sprite.Group(bg1,bg2)
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
    def _check_collide(self):
            pass
    def _update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
    @staticmethod
    def _game_over():
        print("游戏结束")
        pygame.quit()
        exit()
if __name__ == '__main__':
    game=PlaneGame()
    game.start_game()
