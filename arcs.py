import pygame
import sys
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
PI = 3.141592653
pygame.init()
size = width, height = 400, 600
screen = pygame.display.set_mode(size)
screen.fill(WHITE)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



 
        pygame.draw.arc(screen, (RED), [10,300,200,200], PI/2, 3*PI/2, 10)


        pygame.draw.arc(screen, (GREEN), [10,30,200,200], PI/2, 3*PI/2, 20)
    
        pygame.draw.arc(screen, (BLUE), [10,200,200,200], PI/2, 3*PI/2, 30)
        pygame.draw.arc(screen, (BLACK), [10,100,200,200], PI/2, 3*PI/2, 40)
        pygame.draw.arc(screen, (100,20,39), [80,20,200,200], PI/2, 3*PI/2, 50)

        #other (left side)
        pygame.draw.arc(screen, (10), [80,100,250,200], 3*PI/2, PI/2, 30)
        pygame.draw.arc(screen, (RED), [80,30,250,200], 3*PI/2, PI/2, 50)
        pygame.draw.arc(screen, (GREEN), [80,400,250,200], 3*PI/2, PI/2, 70)
        pygame.draw.arc(screen, (RED), [80,450,200,200], 3*PI/2, PI/2, 20)
        pygame.draw.arc(screen, (BLUE), [80,10,250,200], 3*PI/2, PI/2, 10)


        
    pygame.display.flip()
pygame.quit()
