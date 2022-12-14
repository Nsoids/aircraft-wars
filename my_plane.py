"""我方飞机"""
import pygame
from pygame.sprite import Sprite
import constans


class MyPlane(Sprite):
    """我方飞机类"""

    def __init__(self, window) -> None:
        """初始化我方飞机"""

        # 调用父类sprite的特殊方法__init__()
        super().__init__()
        
        # 我方飞机每次移动时的偏移量
        self.offset = 20

        # 切换我方飞机的计数器
        self.switch_counter = 0

        # 获得窗口对象
        self.window = window

        #加载我方飞机第一张图片
        self.image1 = pygame.image.load("images/my_plane1.png")

         # 我方飞机的初始化图片为第一张图片
        self.image = self.image1

        #加载我方飞机第二张图片
        self.image2 = pygame.image.load("images/my_plane2.png")

        # 获得我方飞机矩形
        self.rect = self.image.get_rect()

        # 获得窗口矩形
        self.window_rect = self.window.get_rect()

        # 设置我方飞机的矩形的初始位置为：窗口的底部居中位置
        self.rect.midbottom = self.window_rect.midbottom

        # 标记我方飞机不向上移动
        self.is_move_up = False
        # 标记我方飞机不向下移动
        self.is_move_down = False
        # 标记我方飞机不向左移动
        self.is_move_left = False
        # 标记我方飞机不向右移动
        self.is_move_right = False
        
    def update(self):
        """更新我方飞机位置"""

        if self.is_move_up and self.rect.top - self.offset > 0:           
            # 减少我方飞机的矩形的属性top以向上移动
            self.rect.top -= self.offset 
        if self.is_move_down and self.rect.bottom + self.offset < self.window_rect.height:         
            # 增大我方飞机的矩形的属性bottom以向下移动
            self.rect.bottom += self.offset
        if self.is_move_left and self.rect.left - self.offset > 0:          
            # 减少我方飞机的矩形的属性left以向左移动
            self.rect.left -= self.offset
        if self.is_move_right and self.rect.right + self.offset < self.window_rect.width:           
            # 增大我方飞机的矩形的属性right以向右移动
            self.rect.right += self.offset
       
    def draw(self):
        """在窗口中绘制我方飞机"""

        # 在指定坐标位置加载图片
        self.window.blit(self.image, self.rect)
        
    def switch_image(self):
        """切换我方飞机图片"""

        # 切换我方飞机的计数器加1
        self.switch_counter += 1

        # 如果计数器加到指定值 切换一次图片
        if self.switch_counter == constans.MY_PLANE_SWITCH_IMAGE_FREQUENCY:

            # 如果是第一张图片
            if self.image == self.image1:
                # 切换为第二张图片
                self.image = self.image2
            # 如果是第一张图片
            elif self.image == self.image2:
                # 切换为第一张图片
                self.image = self.image1
            # 计数器归零
            self.switch_counter = 0
        