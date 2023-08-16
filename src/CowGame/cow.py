import pygame
import params


class Spray(pygame.sprite.Sprite):
    def __init__(self):
        super(Spray, self).__init__()
        self.image = pygame.image.load(params.COW_FILEPATH_SPRAY)
        self.image = pygame.transform.scale(self.image, params.COW_SPRAY_SIZE)
        self.rect = self.image.get_rect()

    def update(self, surf, attacking, facing_left, player_x, player_y):
        """Update the position based on the position of player.

        Args:
            surf (pygame.Surface): The pygame Surface object
            attacking (bool): If player is attacking
            facing_left (bool): If player is facing left
            player_x (int): The player's x-coordinate position
            player_y (int): The player's x-coordinate position
        """
        
        if attacking:
            if facing_left:
                tmp_image = pygame.transform.rotate(self.image, 90)
                self.rect.x = player_x-params.COW_SPRAY_OFFSET_X
                self.rect.y = player_y+params.COW_SPRAY_OFFSET_Y
                surf.blit(tmp_image, (player_x-params.COW_SPRAY_OFFSET_X,
                          player_y+params.COW_SPRAY_OFFSET_Y))
            else:
                tmp_image = pygame.transform.rotate(self.image, -90)
                self.rect.x = player_x+params.COW_SPRAY_OFFSET_X
                self.rect.y = player_y+params.COW_SPRAY_OFFSET_Y
                surf.blit(tmp_image, (player_x+params.COW_SPRAY_OFFSET_X,
                          player_y+params.COW_SPRAY_OFFSET_Y))
        else:
            self.kill()


class Cow(pygame.sprite.Sprite):
    def __init__(self):
        super(Cow, self).__init__()
        self.image = pygame.image.load(params.COW_FILEPATH_NORMAL)
        self.image = pygame.transform.scale(self.image, params.COW_SIZE)
        self.rect = self.image.get_rect(
            center=(
                params.SCREEN_WIDTH/2,
                params.SCREEN_HEIGHT/2,
            )
        )
        self.facing_left = True # indicates whether cow is facing left (used to draw the spray attack)
        self.attacking = False  # indicates whether the cow is in attack mode

    def movement(self, pressed_keys):
        """Move player based on keyboard input

        Args:
            pressed_keys (list): list of all pushed buttons from pygame.key.get_pressed()
        """

        # Move Based On User Input
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            print("[COW] UP")
            self.rect.move_ip(0, -params.COW_SPEED_UP)
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            print("[COW] DOWN")
            self.rect.move_ip(0, params.COW_SPEED_DOWN)
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            print("[COW] RIGHT")
            if self.facing_left:
                self.image = pygame.transform.flip(
                    self.image, flip_x=True, flip_y=False)
                self.facing_left = not self.facing_left
            self.rect.move_ip(params.COW_SPEED_RIGHT, 0)
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            print("[COW] LEFT")
            if not self.facing_left:
                self.image = pygame.transform.flip(
                    self.image, flip_x=True, flip_y=False)
                self.facing_left = not self.facing_left
            self.rect.move_ip(-params.COW_SPEED_LEFT, 0)

        # Keep on Screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= params.SCREEN_HEIGHT:
            self.rect.bottom = params.SCREEN_HEIGHT
        if self.rect.right > params.SCREEN_WIDTH:
            self.rect.right = params.SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def attack_position(self):
        """Assume the position."""
        
        if self.attacking:
            if self.facing_left:
                self.image = pygame.transform.rotate(self.image, -90)
            else:
                self.image = pygame.transform.rotate(self.image, 90)
        else:
            if self.facing_left:
                self.image = pygame.transform.rotate(self.image, 90)
            else:
                self.image = pygame.transform.rotate(self.image, -90)


if __name__ == "__main__":
    print("[TEST] COW MAN")
