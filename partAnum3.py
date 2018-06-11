import pygame
from math import pi
import random
pygame.init()
import random




WHITE = (255, 255, 255)


size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")
screen.fill(WHITE)
done = False
clock = pygame.time.Clock()
 
while not done:

    clock.tick(30)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True 

        
    x, y = pygame.mouse.get_pos()    




    bgr = (random.randint(0,255), random.randint(0,255), random.randint(0,255))   
    circe=pygame.draw.circle(screen,(y), [x, y], 25)




    pygame.display.flip()

pygame.quit()
