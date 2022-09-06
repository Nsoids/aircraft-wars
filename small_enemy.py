"""小型敌机"""
from random import randint
from pygame.sprite import Sprite
import pygame


class SmallEnemy(Sprite):
    """小型敌机类"""

    def __init__(self, window) -> None:
        """初始化小型敌机"""

        # 调用父类sprite的特殊方法__init__()
        super().__init__()

        # 获得窗口对象
        self.window = window

        #加载小型敌机图片
        self.image = pygame.image.load("images/small_enemy.png")

        # 获得小型敌机矩形
        self.rect = self.image.get_rect()

        # 获得窗口机矩形
        self.window_rect = self.window.get_rect()

        # 设置小型敌机的矩形的初始位置为：窗口的矩形的顶部一个随机的水平位置
        self.rect.bottom = self.window_rect.top
        self.rect.left = randint(0, self.window_rect.width - self.rect.width)

       # 小型敌机每次移动的偏移量
        self.offset = 6
        
    def update(self):
        """更新小型敌机位置"""

        # 增大小型敌机的矩形的属性top以向下移动
        self.rect.top += self.offset 
       
    def draw(self):
        """在窗口中绘制小型敌机"""

        # 在指定坐标位置加载图片
        self.window.blit(self.image, self.rect)
        