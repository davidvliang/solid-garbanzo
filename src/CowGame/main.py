import pygame
import sys
import random

import params
import cow
import enemy
import game_logic


if __name__ == "__main__":

    # SETUP
    pygame.init()
    screen = pygame.display.set_mode(
        (params.SCREEN_WIDTH, params.SCREEN_HEIGHT))
    pygame.display.set_caption(params.GAME_TITLE)
    clock = pygame.time.Clock()
    game_running = True
    attacking = False

    backdrop = pygame.image.load(params.DISPLAY_FILEPATH_BACKDROP)
    backdropbox = screen.get_rect()

    player = cow.Cow()
    spray = cow.Spray()
    enemy = enemy.Enemy()

    # GAME LOOP
    while game_running:

        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # event - quit game
                print("[EVENT] QUIT")
                game_running = False

            elif event.type == pygame.KEYDOWN:  # event - handle input
                if event.key == pygame.K_ESCAPE:
                    print("[EVENT] ESCAPE")
                    game_running = False
                if event.key == pygame.K_SPACE:  # event - attack
                    print("[EVENT] SPACEBAR")
                    attacking = True
                    player.squirt(attacking)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:  # event - stop attack
                    print("[EVENT] KEYUP SPACE")
                    attacking = False
                    player.squirt(attacking)

        # Fill Background White
        screen.blit(backdrop, backdropbox)

        # Draw Player
        screen.blit(player.image, player.rect)

        # Get Player Input
        pressed_keys = pygame.key.get_pressed()

        # Update Player Input
        player.movement(pressed_keys)
        
        # Handle Attack
        spray.attack(screen, attacking, player.facing_left, player.rect.x, player.rect.y)
  
        # Draw Enemy
        screen.blit(enemy.image, (params.SCREEN_WIDTH/2, params.SCREEN_HEIGHT/2))
        
  
        # Lock FPS to 60
        clock.tick(params.FRAME_RATE)

        # Refresh Display
        pygame.display.flip()

    # EXIT
    print("[MAIN] EXITED")
    pygame.quit()
    sys.exit()
