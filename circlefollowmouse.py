# Import a library of functions called 'pygame'
import pygame
from math import pi
import random

# Initialize the game engine
pygame.init()
import random


# Define the colors we will use in RGB format



# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")
WHITE=(255,255,255)
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# rand_color=random(1,30)


while not done:
    screen.fill(WHITE)
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    x, y = pygame.mouse.get_pos()

    for xpos in range(0, x, 10):
        for ypos in range(0, y, 10):
            col1 = (xpos + ypos )%255
            col2 = (xpos * ypos )%255
            col3 = (xpos + 2* ypos) %255
            pygame.draw.circle(screen, (col1, col2, col3), [xpos, ypos], 5)
    pygame.display.update()

# Be IDLE friendly
pygame.quit()



