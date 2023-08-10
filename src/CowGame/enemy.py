import pygame
import params
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(params.ENEMY_FILEPATH_NORMAL)
        self.image = pygame.transform.scale(self.image, params.ENEMY_SIZE)
        self.facing_left = bool(random.getrandbits(1))
        self.rect = self.image.get_rect(
            center=(
                random.randint(params.SCREEN_WIDTH + 2, params.SCREEN_WIDTH + 10) if self.facing_left else random.randint(2, 10),
                random.randint(0, params.SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(1, 5)

    def update(self):
        if self.facing_left == True:
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                self.kill()
        elif self.facing_left == False:
            self.rect.move_ip(self.speed, 0)
            if self.rect.left > params.SCREEN_WIDTH+20:
                self.kill()

if __name__ == "__main__":
    print("ENEMY MONEY")
