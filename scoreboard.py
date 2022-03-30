import pygame.font
class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        """Init tulemustabeli atribuutid"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        # tulemustabeli seadmed
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 40)
        # valmistab tulemustabeli
        self.prepare_score()

    def prepare_score(self):
        """Paneb tulemustabeli ekraanile"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 15

    def draw_score(self):
        """Näitab tulemust"""
        self.screen.blit(self.score_image, self.score_image_rect)