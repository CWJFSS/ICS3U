#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel
#uses hash function with 3 users to show assignments A and B
#ASSINGMENT 2 First encryption method
#gets needed modules
import pygame
from math import pi
import random
pygame.init()
import random



#defined color
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#define evertying with variables
largeCircleXPos=200
largeCircleYPos= 225
bigRadius=70
size = [400, 300]
screen = pygame.display.set_mode(size)
#this sets size of screen
pygame.display.set_caption("circlesbyClarkwang")
 
done = False
clock = pygame.time.Clock(10)

#game loop
 
while not done:
 
   
    clock.tick(10)
     #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done=True 
        #causes it to expand 50 times per run
    radiusHoriz=1
    radiusHoriz+=50

    radiusVert=1
    radiusVert+=50
#draws xpos and ypos increasing the positions each run
    for xpos in range(0,450,20):
      

                

                pygame.draw.circle(screen, (xpos), [xpos, 150], int(xpos/5))
                
    for ypos in range(0,300,20):
        pygame.draw.circle(screen, (ypos), [200, ypos], int(ypos/5))

    #draws the two different circles
  

    pygame.display.flip()

pygame.quit()
