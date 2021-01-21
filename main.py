import pygame
import sys
import menu
import study_zone
from component import *
from method import *

pygame.init()

screen_init()

clock = pygame.time.Clock()

#YRC PAGE

brand_time = 0.3 #LOGO TIME LONG
screen.fill((255 , 255 ,255))
yrc_logo = Object(pygame.image.load('src/pic/YRC.png') ,CENTER_X , CENTER_Y)
yrc_logo.draw()
pygame.display.update()
clock.tick(brand_time)

link_to('menu')

#PAGE REPRESENT

running = True

def exit() :
    running = False #Close This Page
    pygame.quit()
    sys.exit()

pages = {
    'menu' : menu.main,
    'study_zone' : study_zone.main,
    'unit_1' : study_zone.unit_1,
    'exit' : exit
}

while running :
    page = get_page()
    pages[page]() 

 
    
