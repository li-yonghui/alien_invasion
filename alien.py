import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ 表示单个外星人的类 """

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()

        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """ 在指定位置绘制外星人 """
        self.screen.blit(self.image, self.rect)

