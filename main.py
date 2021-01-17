import pygame
import sys
import menu
from component import *

pygame.init()

screen_init()

clock = pygame.time.Clock()

FPS = 60

running = True
i = 0

#StudyZone
menu.main()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill((0 , 0 ,0))
    p = Paragraph("I WILL SURVIVAL",(255 , 255 ,255) ,CENTER_X,CENTER_Y)
    p.write()
       
    pygame.display.update()
    clock.tick(FPS)
    
