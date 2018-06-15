#Made by: Clark W
#date: 5/27/17
#teacher: Mr. Seidel

#imports everything needed
import pygame
from math import pi
import random
pygame.init()
import random




WHITE = (255, 255, 255)


size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("homework")
screen.fill(WHITE)
#allows the program to not close
done = False
clock = pygame.time.Clock()
 
while not done:
#30 fps clock means runs 30 times  per second
    clock.tick(30)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True 

        #gets mouse position
    x, y = pygame.mouse.get_pos()    


#draws a circle continously at the mouse position as the center

    bgr = (random.randint(0,255), random.randint(0,255), random.randint(0,255))   
    circe=pygame.draw.circle(screen,(y), [x, y], 25)



#shows the screen
    pygame.display.flip()

pygame.quit()
