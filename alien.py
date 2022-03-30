import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klass Alien (tulnukas)"""
    def __init__(self, game_settings, screen):
        """Valmistab tulnuka asukoha ja kuju"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        # laeb tulnuka seaded
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # tulnuka asukoht
        self.x = float(self.rect.x)
    def blitme(self):
        """Loob tulnuka teatud asukohale"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        """Värskendab tulnuka asukohta"""
        self.x += self.game_settings.alien_speed_factor * self.game_settings.fleet_direction
        self.rect.x = self.x
    def check_edges(self):
        """Kontrollib ekraani"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True