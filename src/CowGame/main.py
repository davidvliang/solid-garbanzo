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
    pygame.font.init()
    screen = pygame.display.set_mode(
        (params.SCREEN_WIDTH, params.SCREEN_HEIGHT))
    pygame.display.set_caption(params.GAME_TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    game_running = True
    attacking = False

    backdrop = pygame.image.load(params.DISPLAY_FILEPATH_BACKDROP)
    backdropbox = screen.get_rect()

    # SPRITES
    player_group = pygame.sprite.Group()
    spray_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    loot_group = pygame.sprite.Group()
    
    player = cow.Cow()
    player_group.add(player)
    
    wingding = enemy.Enemy()
    
    scoreboard = game_logic.ScoreBoard()
    milk_meter = game_logic.MilkMeter()
    
    # CUSTOM EVENT
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, params.ENEMY_SPAWN_TIME)
    


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
                    if milk_meter.milk_count > 0:
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
            
        # Update Player With Input
        pressed_keys = pygame.key.get_pressed()
        player.movement(pressed_keys)
  
        # Draw Enemy
        enemy_group.update()
        for enem in enemy_group:
            screen.blit(enem.image, enem.rect)
        
        # Handle Spray Attack
        for spr in spray_group:
            # Check if milk meter is drained
            if milk_meter.milk_count == 0:
                attacking = False
            spr.update(screen, attacking, player.facing_left, player.rect.x, player.rect.y)
            # Check if Enemy is Killed
            sprayed_sprite = pygame.sprite.spritecollideany(spr, enemy_group)
            if sprayed_sprite:
                sprayed_sprite.kill()
                print("[MAIN] Enemy Killed", sprayed_sprite)
                scoreboard.update_kills()
                # Create Loot Bag
                if random.random() > params.ENEMY_DROP_RATE:
                    new_loot = enemy.Loot(sprayed_sprite.rect.x, sprayed_sprite.rect.y)
                    loot_group.add(new_loot)
                    
        # Draw Lootbags
        loot_group.update()
        for ltbg in loot_group:
            screen.blit(ltbg.image, ltbg.rect)
    
        # Handle Loot Pickup
        got_loot = pygame.sprite.spritecollideany(player, loot_group)
        if got_loot:
            got_loot.kill()
            scoreboard.update_money()
            
        # Check if Player Dies
        if pygame.sprite.spritecollideany(player, enemy_group):
            print("[MAIN] ENEMY HIT PLAYER")
            player.kill()
            game_running = False    
  
        # Draw Scoreboard
        score_text = font.render(f"Murders: {scoreboard.kill_count}      CA$H: {scoreboard.money_count}", True, (255,255,255))
        screen.blit(score_text, (10,10))
        
        # Draw MilkMeter
        milk_meter.update(attacking)
        milk_meter_sprite = font.render(f"Milk: {int((milk_meter.milk_count/params.LOGIC_MILKMETER_MAX) * 100)}%", True, (255,255,255))
        screen.blit(milk_meter_sprite, (10, params.SCREEN_HEIGHT-50))
  
        # Lock FPS to 60
        clock.tick(params.FRAME_RATE)

        # Refresh Display
        pygame.display.flip()
 
    # EXIT
    print(f"[FINAL SCORE] Murders:{scoreboard.kill_count}\t CA$H:{scoreboard.money_count}")
    print("[MAIN] EXITED")
    pygame.quit()
    sys.exit()
