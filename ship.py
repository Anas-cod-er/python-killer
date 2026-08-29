import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        #intialize the ship and set the position
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start ship position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store decimal values for the ship's center.
        #vertical
        self.center = float(self.rect.centerx)
        #horizontal
        self.center_y = float(self.rect.centery)

        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor  
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        #update rect object from the ship's center values
        self.rect.centerx = self.center
        self.rect.centery = self.center_y


    def blitme(self):
        #draw the ship
        self.screen.blit(self.image, self.rect)
        