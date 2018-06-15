#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel

import pygame
from math import pi
import random
#gets random function, initiate pygame
pygame.init()
import random



#gets screensize

size = [400, 300]
screen = pygame.display.set_mode(size)
#shows caption
pygame.display.set_caption("code")
WHITE=(255,255,255)
done = False
clock = pygame.time.Clock()


#fills screen
while not done:
    screen.fill(WHITE)
  
    clock.tick(10)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            done = True  
#unpacks the event array as useable xy position
    x, y = pygame.mouse.get_pos()
#mod makes fill more random
#uses double for loop to create 2d effect
    for xpos in range(0, x, 10):
        for ypos in range(0, y, 10):
            col1 = (xpos + ypos )%255
            col2 = (xpos * ypos )%255
            col3 = (xpos + 2* ypos) %255
            pygame.draw.circle(screen, (col1, col2, col3), [xpos, ypos], 5)
    pygame.display.update()

pygame.quit()



