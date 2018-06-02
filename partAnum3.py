# Import a library of functions called 'pygame'
import pygame
from math import pi
import random
# Initialize the game engine
pygame.init()
import random
#col = random.randint(0, 200)
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


# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")
screen.fill(WHITE)
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:

    clock.tick(30)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        
    x, y = pygame.mouse.get_pos()    




    bgr = (random.randint(0,255), random.randint(0,255), random.randint(0,255))   
    circe=pygame.draw.circle(screen,(y), [x, y], 25)
    #circe.fill(bgr)

    #if pygame.time.get_ticks()-timer>1000:
    #    timer=pg.time.get_ticks()
    #    bgr=(random.randint(0,255), random.randint(0,255),random.randint(0,255))


    #circe=pygame.draw.circle(screen,(COLR), [x, y], 25)

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
