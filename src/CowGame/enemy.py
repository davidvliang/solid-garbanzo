import pygame
import params

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(params.ENEMY_FILEPATH_NORMAL)
        self.image = pygame.transform.scale(self.image, params.ENEMY_SIZE)
        self.rect = self.image.get_rect()
        self.facing_left = True

    def update(self):
        pass

if __name__ == "__main__":
    print("ENEMY MONEY")
