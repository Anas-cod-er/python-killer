#import file
import pygame
import game_fuction as gf

#from file
from settings import Settings
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group
from alien import Alien
from scoreboard import Scoreboard


def run_game():
    # #for initialize pygame
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # make the scoreboard
    sb = Scoreboard(ai_settings, screen)

    # make the ship
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in.
    bullets = Group()
    # make an alien
    aliens = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #start the game loop
    while True:
        gf.check_events(ship, ai_settings, screen, bullets, sb, aliens)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets, sb)
        gf.update_aliens(ai_settings, screen, ship, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, sb)


run_game()

