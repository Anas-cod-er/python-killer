import pygame.font

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.score = 0

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.shadow_color = (0, 0, 0)
        self.font = pygame.font.SysFont('Arial', 40, bold=True)

        # Prepare the initial score & stage image.
        self.prep_score()
        self.prep_stage()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = f"Score: {self.score}"
        
        # Render main text and shadow for clear visibility
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.shadow_image = self.font.render(score_str, True, self.shadow_color)

        # Display the score at the top center of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20

        self.shadow_rect = self.shadow_image.get_rect()
        self.shadow_rect.centerx = self.screen_rect.centerx + 2
        self.shadow_rect.top = 22

    def prep_stage(self):
        """Turn the current stage into a rendered image."""
        stage_name = self.ai_settings.stage_names.get(self.ai_settings.stage, "Easy")
        stage_str = f"Stage {self.ai_settings.stage}: {stage_name}"

        self.stage_image = self.font.render(stage_str, True, (255, 220, 0)) # Golden yellow
        self.stage_shadow = self.font.render(stage_str, True, self.shadow_color)

        # Display the stage at top left of screen.
        self.stage_rect = self.stage_image.get_rect()
        self.stage_rect.left = 30
        self.stage_rect.top = 20

        self.stage_shadow_rect = self.stage_shadow.get_rect()
        self.stage_shadow_rect.left = 32
        self.stage_shadow_rect.top = 22

    def show_score(self):
        """Draw score and stage to the screen."""
        self.screen.blit(self.shadow_image, self.shadow_rect)
        self.screen.blit(self.score_image, self.score_rect)

        self.screen.blit(self.stage_shadow, self.stage_shadow_rect)
        self.screen.blit(self.stage_image, self.stage_rect)
