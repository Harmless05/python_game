class Settings:
    """Klass Settings (seadmed)"""

    def __init__(self):
        """Mängu seaded (tulnukas, kuul, laev)"""
        # mängu/ekraanu seadmed
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (4, 26, 46)
        # laeva seadmed
        self.ship_limit = 0
        # kuuli seadmed
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 38, 90, 163
        self.bullets_allowed = 3
        # tulnuka seadmed
        self.fleet_drop_speed = 5
        # kiiruse suurendamine
        self.speedup_scale = 1.1
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.5

        # tulnukate suund
        self.fleet_direction = 1

        # punktid iga tulnuka tapmise eest (20 per kill)
        self.alien_points = 20
        self.level_points = 1

    def increase_speed(self):
        """Objektide kiiruse suurendamine (laevm kuul, tulnukas)"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
