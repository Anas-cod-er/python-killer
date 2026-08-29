import pygame
class Settings():
    #a class where store all setting 

    def __init__(self):
        #screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230 , 230, 230)
        self.bg = pygame.image.load('bg-image.png')
        self.bg = pygame.transform.scale(
            self.bg, (self.screen_width, self.screen_height)
        )
        self.ship_speed_factor = 1.5

        #bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0,0,0
        self.bullet_allowed = 3

        #alien setting
        self.stage = 1
        self.stage_names = {1: "Easy", 2: "Medium", 3: "Hard"}
        self.stage_speeds = {1: 0.5, 2: 1.0, 3: 1.8}
        self.alien_speed_factor = self.stage_speeds[self.stage]
        self.alien_points = 50

    def set_stage(self, stage_num):
        """Set game stage and update alien speed."""
        if stage_num in self.stage_speeds:
            self.stage = stage_num
            self.alien_speed_factor = self.stage_speeds[self.stage]