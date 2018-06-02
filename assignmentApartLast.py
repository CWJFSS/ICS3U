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
screen.fill(WHITE)
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#rand_color=random(1,30)


 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # Draw a circle
 
   # colora=0
   # while colora<200:
   #   colora=colora+30
    for redBig in range(1,80,2):
        for  greenBig in range(3,250,5):
            for blueBig in range(30, 200,20):
                for bigRadius in range (1,70,2):
                    pygame.draw.circle(screen, (redBig,greenBig,blueBig), [largeCircleXPos, largeCircleYPos], bigRadius)
 
    """colur = (  color,   color,   color)
    color+=30"""
    
    """ypos=50"""

    smallColor=0
    for xpos in range(0,450,20):
            for ypos in range(0,150,20):
                if smallColor== 200:
                    change=-1
                elif smallColor==0:
                
                    change=1
                
                smallColor+=change
                pygame.draw.circle(screen, (smallColor), [xpos, ypos], 10)


    """color*=20"""
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
