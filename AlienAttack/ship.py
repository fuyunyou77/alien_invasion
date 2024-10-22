###
 # @Author: fuyunyou
 # @Date: 2024-10-12 11:51:14
 # @LastEditors: fuyunyou
 # @LastEditTime: 2024-10-17 11:45:36
 # @Description: 
 # @FilePath: \PythonCode\alien_invasion\AlienAttack\ship.py
###
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船的类"""
    
    def __init__(self,ai_game):
        """初始化飞船并设置其位置"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screeen_rect=ai_game.screen.get_rect()

        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('../images/ship.bmp')
        self.rect=self.image.get_rect()

        #每个新飞船都始化在屏幕底部
        self.rect.midbottom=self.screeen_rect.midbottom

        #飞船的x属性，表示飞船的水平位置，其中存放float值，使其能获取更精细的位置变化
        self.x=float(self.rect.x)

        #移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """根据移动标志调整飞船的位置"""
        #每次移动更新飞船的x而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screeen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x-=self.settings.ship_speed

        #根据self.x更新rect对象
        self.rect.x=self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船在屏幕底部居中"""
        self.rect.midbottom=self.screeen_rect.midbottom
        self.x=float(self.rect.x)