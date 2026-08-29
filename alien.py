import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # load the image and scale to a larger size (90x90)
        self.image = pygame.image.load('py.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()

        # start each new alien near top left of screen rect.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien smoothly from top to bottom."""
        self.y += self.ai_settings.alien_speed_factor
        self.rect.y = self.y

    def blitme(self):
        """ Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)