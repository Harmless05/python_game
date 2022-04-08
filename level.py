import pygame.font
class Level():
    def __init__(self, game_settings, screen, stats):
        """Init taseme atribuutid"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        # taseme seadmed
        self.text_color = (220, 220, 220)
        self.font = pygame.font.SysFont(None, 40)
        # valmistab taseme
        self.prepare_level()

    def prepare_level(self):
        """Paneb taseme ekraanile"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render("Level " + level_str, True, self.text_color, self.game_settings.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.screen_rect.right - 1080
        self.level_image_rect.top = 15

    def draw_level(self):
        """Näitab tulemust"""
        self.screen.blit(self.level_image, self.level_image_rect)