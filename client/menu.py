import pygame
import sys
from method import *
from component import *
#import voice_control
from threading import Thread

pygame.init()

this_page = 'menu'

clock = pygame.time.Clock()
running = True

def close() :
    print("Click")

def main(session) : 

    FPS = 60
    running = True

    background = Object(pygame.image.load('./src/pic/menu/BGVN.png'),CENTER_X ,CENTER_Y)
    shade = Object(pygame.image.load('./src/pic/menu/dark_mask.png'),CENTER_X ,CENTER_Y)
    title = Object(pygame.image.load('./src/pic/menu/title.png'), CENTER_X ,400)
    user_zone = Text_button("ยินดีต้อนรับ + - × ÷" + session["username"], SCREEN_WIDTH - 300, 200 , right = True)
    button_1 = Button(pygame.image.load('./src/pic/menu/button-1.png'), 750 , 700)
    button_2 = Button(pygame.image.load('./src/pic/menu/button-2.png'), SCREEN_WIDTH - 750 , 700)
    button_3 = Button(pygame.image.load('./src/pic/menu/button-3.png'), 750 , 820)
    button_4 = Button(pygame.image.load('./src/pic/menu/button-4.png'), SCREEN_WIDTH - 750 , 820)

    time = 0.00

    while running:

        time += 1 / FPS

        background.draw()
        shade.draw()
        #screen.fill(pygame.Color(255 , 255 , 255 , a = 200)) # To Bright Tone Background
       
        title.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if button_1.onclick() :
                    link_to('study_zone')
                    running = False #Close This Page

                elif button_2.onclick() :
                    link_to('play_zone')
                    running = False #Close This Page

                elif button_3.onclick() :
                    link_to('study_zone')
                    running = False #Close This Page

                elif button_4.onclick() :
                    link_to('exit')
                    running = False #Close This Page

        button_1.draw()
        button_2.draw()
        button_3.draw()
        button_4.draw()
        user_zone.draw()

        pygame.display.update()
        clock.tick(FPS)
        
        
    
