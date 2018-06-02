import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))



pygame.draw.rect(screen,(0,0,255),(0,0,640,400))
pygame.draw.circle(screen,(255,255,0),(50,400),200)

pygame.draw.rect(screen,(0,255,0),(0,400,640,80))


pygame.draw.rect(screen,(255,0,0),(255,400-180,200,180))
 
pygame.draw.rect(screen,(255,255,255),(255+80,400-60,40,60))
 
pygame.draw.circle(screen,(0,0,0),(255+112,400-30),4)

pygame.draw.polygon(screen, (0,0,0), ( (255,400-180),(255+100,400-250),(255+200,400-180) ) )


pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
