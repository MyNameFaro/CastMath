import pygame
import sys
from method import *
from component import *

pygame.init()

this_page = 'menu'

words = ["""การดำเนินการทางคณิตศาสตร์ หมายถึง การกระทำตามลำดับ <br>หรือลำดับขั้นตอนเพื่อให้ได้ผลลัพธ์ โดยอาศัยตัวดำเนินการ
<br>ในทางคณิตศาสตร์ตัวดำเนินการแบ่งออกเป็น 4 ตัวหลักๆ คือ"""]

clock = pygame.time.Clock()
running = True

def close() :
    print("Click")

def main() : 

    FPS = 60
    running = True

    background = Object(pygame.image.load('src/pic/menu/BG.jpeg'),CENTER_X ,CENTER_Y)
    title = Object(pygame.image.load('src/pic/menu/title.png'), CENTER_X ,400)
    
    button_1 = Button(pygame.image.load('src/pic/menu/button-1.png'), 750 , 700)
    button_2 = Button(pygame.image.load('src/pic/menu/button-2.png'), SCREEN_WIDTH - 750 , 700)
    button_3 = Button(pygame.image.load('src/pic/menu/button-3.png'), 750 , 820)
    button_4 = Button(pygame.image.load('src/pic/menu/button-4.png'), SCREEN_WIDTH - 750 , 820)

    while running:

        
        background.draw()
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

                if button_2.onclick() :
                    pass

                if button_3.onclick() :
                    pass

                if button_4.onclick() :
                    link_to('exit')
                    running = False #Close This Page

        button_1.draw()
        button_2.draw()
        button_3.draw()
        button_4.draw()


        pygame.display.update()
        clock.tick(FPS)
        
        
    
