import pygame
from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from level import Level
from ship import Ship
#from alien import Alien
import game_functions as gf

def run_game():
    """Paneb mängu tööle"""
    # init game and create display object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Space game")
    # mängu START nupp
    play_button = Button(game_settings, screen, "START")
    # mängu statistika
    stats = GameStats(game_settings)
    # mängu tulemus
    sb = Scoreboard(game_settings, screen, stats)
    #mängu tase (alustab 1.)
    lvl = Level(game_settings, screen, stats)

    # Loob laeva
    ship = Ship(game_settings, screen)
    bullets = Group()
    # Loob tulnuka gruppi
    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)

    while True:
        gf.check_events(game_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, sb, lvl, ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(game_settings, screen, stats, sb, lvl, ship, aliens, bullets, play_button)
run_game()