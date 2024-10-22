###
 # @Author: fuyunyou
 # @Date: 2024-10-12 11:17:45
 # @LastEditors: fuyunyou
 # @LastEditTime: 2024-10-22 10:19:31
 # @Description: 
 # @FilePath: \alien_invasion\AlienAttack\settings.py
###
class Settings:
    """存储游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width=800
        self.screen_height=600
        self.bg_color=(230,230,230)

        #飞船设置
        self.ship_limit=4

        #子弹设置
        self.bullet_width=3
        self.bullet_height=20
        self.bullet_color=(60,60,60)
        self.bullet_allowed=6

        #外星人设置
        self.alien_speed=1.0
        self.fleet_drop_speed=10
        
        #加快游戏节奏的速度
        self.speedup_scale=1.05
        self.score_scale=1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随着游戏进行而变化的设置"""
        self.ship_speed=1.5
        self.bullet_speed=2.0
        self.alien_speed=1.0
        self.alien_points=50

        #fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction=1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale

        self.alien_points=int(self.alien_points * self.score_scale)