import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ship, ai_settings, screen, bullets, sb, aliens):
    """response to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    elif event.key in (pygame.K_1, pygame.K_KP1):
        ai_settings.set_stage(1)
        sb.prep_stage()
    elif event.key in (pygame.K_2, pygame.K_KP2):
        ai_settings.set_stage(2)
        sb.prep_stage()
    elif event.key in (pygame.K_3, pygame.K_KP3):
        ai_settings.set_stage(3)
        sb.prep_stage()
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """response to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ship, ai_settings, screen, bullets, sb=None, aliens=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets, sb, aliens)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.y = float(alien.rect.height + 2 * alien.rect.height * row_number)
    alien.rect.y = alien.y
    aliens.add(alien)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    ship_height = ship.rect.height if ship else 50
    number_rows = get_number_rows(ai_settings, ship_height, alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_aliens_bottom(ai_settings, screen, aliens):
    """Check if any aliens have reached the bottom of the screen and wrap them back to top."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.top >= screen_rect.bottom:
            alien.y = -float(alien.rect.height)
            alien.rect.y = alien.y


def show_game_over(screen):
    """Display GAME OVER on screen and terminate game."""
    font = pygame.font.SysFont('Arial', 64, bold=True)
    text_image = font.render("GAME OVER", True, (255, 30, 30))
    shadow_image = font.render("GAME OVER", True, (0, 0, 0))

    rect = text_image.get_rect()
    rect.center = screen.get_rect().center

    shadow_rect = shadow_image.get_rect()
    shadow_rect.center = (screen.get_rect().centerx + 3, screen.get_rect().centery + 3)

    screen.blit(shadow_image, shadow_rect)
    screen.blit(text_image, rect)
    pygame.display.flip()

    # Pause for 2 seconds before exiting
    pygame.time.wait(2000)
    sys.exit()


def update_aliens(ai_settings, screen, ship, aliens):
    """
    Update the positions of all aliens in the fleet moving smoothly top to bottom.
    End game if an alien hits the ship body.
    """
    aliens.update()
    check_aliens_bottom(ai_settings, screen, aliens)

    # Check if any alien hit the ship body
    if pygame.sprite.spritecollideany(ship, aliens):
        show_game_over(screen)


def update_screen(ai_setting, screen, ship, aliens, bullets, sb):
    screen.blit(ai_setting.bg, (0, 0))
    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    sb.show_score()
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets, sb):
    """Update position of bullets and get rid of old bullets & hit aliens."""
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens_hit in collisions.values():
            sb.score += ai_settings.alien_points * len(aliens_hit)
        sb.prep_score()

    if len(aliens) == 0:
        # Destroy existing bullets, advance stage, and create new fleet.
        bullets.empty()
        next_stage = (ai_settings.stage % 3) + 1
        ai_settings.set_stage(next_stage)
        sb.prep_stage()
        create_fleet(ai_settings, screen, ship, aliens)