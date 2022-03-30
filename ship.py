import pygame

class Ship():
    def __init__(self, game_settings, screen):
        """Initialize ship and define ship start position"""
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position according to moving flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        """Draw ship at this position"""
        self.screen.blit(self.image, self.rect)
    def ship_center(self):
        self.center = self.screen_rect.centerx
