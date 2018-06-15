#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel

import pygame
from math import pi
import random

pygame.init()
import random





size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")
WHITE=(255,255,255)
done = False
clock = pygame.time.Clock()



while not done:
    screen.fill(WHITE)
  
    clock.tick(10)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            done = True  

    x, y = pygame.mouse.get_pos()

    for xpos in range(0, x, 10):
        for ypos in range(0, y, 10):
            col1 = (xpos + ypos )%255
            col2 = (xpos * ypos )%255
            col3 = (xpos + 2* ypos) %255
            pygame.draw.circle(screen, (col1, col2, col3), [xpos, ypos], 5)
    pygame.display.update()

pygame.quit()



