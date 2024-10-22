###
 # @Author: fuyunyou
 # @Date: 2024-10-17 11:27:29
 # @LastEditors: fuyunyou
 # @LastEditTime: 2024-10-21 15:06:51
 # @Description: 
 # @FilePath: \alien_invasion\AlienAttack\game_stats.py
###
class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings=ai_game.settings
        self.reset_stats()
        self.high_score=0
        self.level=1

        #游戏刚启动时,处于活跃状态
        self.game_active=False

    def reset_stats(self):
        """初始化在游戏期间可能变化的统计信息"""
        self.ships_left=self.settings.ship_limit
        self.score=0