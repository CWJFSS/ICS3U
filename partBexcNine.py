#explanation: draw lines
#set x position to a variable that can either be 0 or 600
#set y position equal to preset indexed values in an array 

#create a for loop that increases x position by 600/50=12
#
#generate a random array of 50 numbers representing the y position
#using built in function
#
#loop through that array using for loop

#use an if statement that checks if the y potition of the point is
#greater than midscreen(600/2=300 pixels) or less than midscreen  

#if greater, draw to starting x position 600
#if less, set starting x position to 0
#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel
import numpy
import random

#generates a point somewhere on screen and makes a line to the closest wall

import pygame
from math import pi


pygame.init()



WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


size = [600,  600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")
 
done = False
clock = pygame.time.Clock()
screen.fill((WHITE))


topWall=250
bottomWall=0
xpos=0
while not done:
 

    clock.tick(10)
    

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True 

        for i in range(0,50,1):
            
            ypos=[10,30,50,20,31,35,600,400,300,500,100,333,444,555,11,22,33,44,55,66,77,88,99,11,2,333,600,556,222,110,234,345,456,567,122,334,558,365,476,452,321,126,347,543,432,321,231,523,533,381]
            xpos+=12
            if ypos[i]>300:
                strt_x_pos=600
            if ypos[i]==300:
                strt_x_pos=0
            if ypos[i]<300:
                strt_x_pos=0
            pygame.draw.lines(screen, RED, True, [(xpos,strt_x_pos), (xpos,ypos[i])], 5)

    pygame.display.flip()


pygame.quit()


