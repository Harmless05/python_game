import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Klass Bullet (kuul)"""
    def __init__(self, game_setting, screen, ship):
        """Valmistab (laseb) kuuli laeva asukohast"""
        super().__init__()
        self.screen = screen
        # valmistab kuuli
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0, 0, game_setting.bullet_width, game_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # kuuli asukoht
        self.y = float(self.rect.y)
        # kuuli seaded
        self.color = game_setting.bullet_color
        self.speed_factor = game_setting.bullet_speed_factor
    def update(self):
        """Värskendab kuuli asukohta"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        """Valmistab kuuli ekraanile"""
        pygame.draw.rect(self.screen, self.color, self.rect)