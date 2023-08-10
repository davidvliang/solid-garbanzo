import pygame
import params

class GameLogic():
    pass

class MilkMeter():
    def __init__(self):
        super(MilkMeter, self).__init__()
        # self.image = pygame.image.load(params.COW_FILEPATH_SPRAY)
        # self.image = pygame.transform.scale(self.image, params.COW_SPRAY_SIZE)
        # self.rect = self.image.get_rect()
        self.milk_count = params.LOGIC_MILKMETER_MAX
    
    def update(self, active):
        if active:
            if self.milk_count > 0:
                self.milk_count -= 1
        else:
            if self.milk_count < params.LOGIC_MILKMETER_MAX:
                self.milk_count += 1  


class ScoreBoard():
    pass

