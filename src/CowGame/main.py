import pygame
import sys

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
    wingding = enemy.Enemy()
    
    player_group = pygame.sprite.Group()
    spray_group = pygame.sprite.Group()
    player_group.add(player)
    enemy_group = pygame.sprite.Group()
    
    # CUSTOM EVENT
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 1000)
    
    
    # LOGIC
    kill_count = 0

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
                    player.attack_position(attacking)
                    spray = cow.Spray()
                    spray_group.add(spray)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:  # event - stop attack
                    print("[EVENT] KEYUP SPACE")
                    attacking = False
                    player.attack_position(attacking)
                    spray.kill()

            elif event.type == ADDENEMY:
                print("[EVENT] ADD ENEMY")
                new_enemy = enemy.Enemy()
                enemy_group.add(new_enemy)
                

        # Fill Background White
        screen.blit(backdrop, backdropbox)

        # Draw Player
        for entity in player_group:
            screen.blit(entity.image, entity.rect)
            
        # Get Player Input
        pressed_keys = pygame.key.get_pressed()

        # Update Player Input
        player.movement(pressed_keys)
  
        # Draw Enemy
        enemy_group.update()
        for enem in enemy_group:
            screen.blit(enem.image, enem.rect)
        
        # Handle Spray Attack
        for spr in spray_group:
            spr.update(screen, attacking, player.facing_left, player.rect.x, player.rect.y)
            # Check if Enemy is Killed
            sprayed_sprite = pygame.sprite.spritecollideany(spr, enemy_group)
            if sprayed_sprite:
                sprayed_sprite.kill()
                print("[EVENT] Enemy Killed", sprayed_sprite)
                kill_count += 1
            
        
        # Check if Player Dies
        if pygame.sprite.spritecollideany(player, enemy_group):
            print("[MAIN] ENEMY HIT PLAYER")
            player.kill()
            game_running = False    
  
        # Lock FPS to 60
        clock.tick(params.FRAME_RATE)

        # Refresh Display
        pygame.display.flip()

    # EXIT
    print("[MAIN] EXITED")
    pygame.quit()
    sys.exit()
