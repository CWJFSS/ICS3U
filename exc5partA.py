#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel


import pygame
from math import pi
import random
pygame.init()
import random




largeCircleXPos=200
largeCircleYPos= 225
bigRadius=70

size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

done = False
clock = pygame.time.Clock()


while not done:

    clock.tick(10)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # 
            done=True # 


    rad=20

    for xpos in range( 0,400  ,20):            
        for ypos in range(0,300,20):
            pygame.draw.circle(screen, (ypos+100), [xpos+int(ypos/6), ypos], 10)

   
    pygame.display.flip()

pygame.quit()
