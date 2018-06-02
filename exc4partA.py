# Import a library of functions called 'pygame'
import pygame
from math import pi
import random
# Initialize the game engine
#NOTE: xpos, ypos is the x position and y position respectively of the small circles
pygame.init()
import random

COLORS = [(0, 0, 0), 
          (0, 200, 0),
          (0, 0, 200),
          (200,200,200),
          (200,0,200)
          ,(200,200,0),
         ( 200,0,0)]

"""def random_color():
    return random.choice(COLORS)
 """
# Define the colors we will use in RGB format

WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


largeCircleXPos=200
largeCircleYPos= 225
bigRadius=70
# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock(10)

#rand_color=random(1,30)

 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    radiusHoriz=1
    radiusHoriz+=50

    radiusVert=1
    radiusVert+=50

    for xpos in range(0,450,20):
      

                

                pygame.draw.circle(screen, (xpos), [xpos, 150], int(xpos/5))
                
    for ypos in range(0,300,20):
        pygame.draw.circle(screen, (ypos), [200, ypos], int(ypos/5))

    """color*=20"""
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
  

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
