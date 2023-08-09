import pygame

# Parameters
background_color = (255, 255, 255)
(width, height) = (500, 500)

# Initialization
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


running = True
while running:

    # Click Window Close Button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Closing Window")

    # Fill Background White
    screen.fill(background_color)

    # Draw solid blue circle
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    
    # limit FPS to 60
    clock.tick(60)
    
    # Flip Display
    pygame.display.flip()
    
    

pygame.quit()
