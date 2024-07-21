# Import the pygame module
import pygame

# Background color 
background_color = (234, 212, 252)

# Screen object (width, height)
screen = pygame.display.set_mode((300,300))

# Caption of the screen
pygame.display.set_caption('Pygame')

# Fill the backgound color to the screen
screen.fill(background_color)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running 
running = True

# Game loop
while running:

# For loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.event.get():
            running = False