#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel

#get libs
import pygame
from math import pi
import random

pygame.init()
import random




#define all cols
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#set variables
largeCircleXPos=200
largeCircleYPos= 225
bigRadius=70
size = [400, 300]
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
pygame.display.set_caption("Example code for the draw module")
 
done = False
clock = pygame.time.Clock()



 #game loop
while not done:
 

    clock.tick(10)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True
 
#for loop for the colours and the big circle
    for redBig in range(1,80,2):
        for  greenBig in range(3,250,5):
            for blueBig in range(30, 200,20):
                for bigRadius in range (1,70,2):
                    pygame.draw.circle(screen, (redBig,greenBig,blueBig), [largeCircleXPos, largeCircleYPos], bigRadius)
 
#smaller circles, for loop to draw them in a box
    smallColor=0
    for xpos in range(0,450,20):
            for ypos in range(0,150,20):
                if smallColor== 200:
                    change=-1
                elif smallColor==0:
                
                    change=1
                
                smallColor+=change
                pygame.draw.circle(screen, (smallColor), [xpos, ypos], 10)


   
    pygame.display.flip()

pygame.quit()
