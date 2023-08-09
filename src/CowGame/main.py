import pygame
import cow
import game_logic

# Display Constants
(WIN_WIDTH, WIN_HEIGHT) = (1280, 720)
background_color = "white"
locked_frame_rate = 60


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:

        # Fill Background White
        screen.fill(background_color)

        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # event - quit game
                running = False

        # Handle Player Input

        # Lock FPS to 60
        clock.tick(locked_frame_rate)

        # Refresh Display
        pygame.display.flip()
