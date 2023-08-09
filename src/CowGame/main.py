import pygame
import cow
import game_logic

# Display Constants
(WIN_WIDTH, WIN_HEIGHT) = (1280, 720)
game_title = "Cash Cow I: The Cashening"
background_color = "green"
locked_frame_rate = 60


if __name__ == "__main__":

    # Setup
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption(game_title)
    clock = pygame.time.Clock()
    game_running = True
    
    player = cow.Cow()
    

    # Main Loop
    while game_running:

        # Fill Background White
        screen.fill(background_color)

        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # event - quit game
                running = False

            # event - player input

        # Lock FPS to 60
        clock.tick(locked_frame_rate)

        # Refresh Display
        pygame.display.flip()
