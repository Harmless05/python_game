class GameStats():
    """Klass GameStats (mängu andmed)"""
    def __init__(self, game_settings):
        """Valmistab andmed"""
        self.game_settings = game_settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """Taastab algsed andmed"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1