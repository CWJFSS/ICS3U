import pygame
from math import pi
import random
pygame.init()
import random

COLORS = [(0, 0, 0), 
          (0, 200, 0),
          (0, 0, 200),
          (200,200,200),
          (200,0,200)
          ,(200,200,0),
         ( 200,0,0)]



WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


largeCircleXPos=200
largeCircleYPos= 225
bigRadius=70
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")
 
done = False
clock = pygame.time.Clock(10)


 
while not done:
 
   
    clock.tick(10)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done=True 
    radiusHoriz=1
    radiusHoriz+=50

    radiusVert=1
    radiusVert+=50

    for xpos in range(0,450,20):
      

                

                pygame.draw.circle(screen, (xpos), [xpos, 150], int(xpos/5))
                
    for ypos in range(0,300,20):
        pygame.draw.circle(screen, (ypos), [200, ypos], int(ypos/5))

    
  

    pygame.display.flip()

pygame.quit()
