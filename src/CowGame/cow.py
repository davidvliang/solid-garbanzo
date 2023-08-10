import pygame
import params

class Spray(pygame.sprite.Sprite):
    def __init__(self):
        super(Spray, self).__init__()
        self.image = pygame.image.load(params.COW_FILEPATH_SPRAY)
        self.image = pygame.transform.scale(self.image, params.COW_SPRAY_SIZE)
        # self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        
    def attack(self, surf, active, facing_left, player_x, player_y):
        if active:
            if facing_left:
                tmp_image = pygame.transform.rotate(self.image, 90)
                surf.blit(tmp_image, (player_x-params.COW_SPRAY_OFFSET_X,player_y+params.COW_SPRAY_OFFSET_Y))
            else:
                tmp_image = pygame.transform.rotate(self.image, -90)
                surf.blit(tmp_image, (player_x+params.COW_SPRAY_OFFSET_X,player_y+params.COW_SPRAY_OFFSET_Y))


class Cow(pygame.sprite.Sprite):
    def __init__(self):
        super(Cow, self).__init__()
        self.image = pygame.image.load(params.COW_FILEPATH_NORMAL)
        self.image = pygame.transform.scale(self.image, params.COW_SIZE)
        self.rect = self.image.get_rect()
        self.facing_left = True

    def movement(self, pressed_keys):

        # Move Based On User Input
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            print("[EVENT] UP")
            self.rect.move_ip(0, -params.COW_SPEED_UP)
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            print("[EVENT] DOWN")
            self.rect.move_ip(0, params.COW_SPEED_DOWN)
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            print("[EVENT] RIGHT")
            if self.facing_left:
                self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
                self.facing_left = not self.facing_left
            self.rect.move_ip(params.COW_SPEED_RIGHT, 0)
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            print("[EVENT] LEFT")
            if not self.facing_left:
                self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
                self.facing_left = not self.facing_left
            self.rect.move_ip(-params.COW_SPEED_LEFT, 0)

        # Keep on Screen

    def squirt(self, space_pressed):
        if space_pressed:
            if self.facing_left:
                self.image = pygame.transform.rotate(self.image,-90)
            else:
                self.image = pygame.transform.rotate(self.image,90)
        else:
            if self.facing_left:
                self.image = pygame.transform.rotate(self.image,90)
            else:
                self.image = pygame.transform.rotate(self.image,-90)  

if __name__ == "__main__":
    print("COW MAN")
