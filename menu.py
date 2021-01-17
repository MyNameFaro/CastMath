import pygame
import sys
import method
from component import *
import time

pygame.init()

words = ["""การดำเนินการทางคณิตศาสตร์ หมายถึง การกระทำตามลำดับ <br>หรือลำดับขั้นตอนเพื่อให้ได้ผลลัพธ์ โดยอาศัยตัวดำเนินการ
<br>ในทางคณิตศาสตร์ตัวดำเนินการแบ่งออกเป็น 4 ตัวหลักๆ คือ"""]

clock = pygame.time.Clock()
running = True

def close() :
    print("Click")

def main() : 

    FPS = 60
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        background = Object(pygame.image.load('src/pic/menu/BG.jpeg'),CENTER_X ,CENTER_Y)
        background.draw()
        title = Object(pygame.image.load('src/pic/menu/title.png'), CENTER_X ,500)
        title.draw()

        button_1 = Button(pygame.image.load('src/pic/menu/button-1.png'), 610 , 800)
        button_2 = Button(pygame.image.load('src/pic/menu/button-2.png'), SCREEN_WIDTH - 610 , 800)
        button_3 = Button(pygame.image.load('src/pic/menu/button-3.png'), 610 , 910)
        button_4 = Button(pygame.image.load('src/pic/menu/button-4.png'), SCREEN_WIDTH - 610 , 910)

        button_1.draw()
        button_2.draw()
        button_3.draw()
        button_4.draw()

        if button_4.onclick() :
            running = False
            pygame.quit()
            sys.exit()


        pygame.display.update()
        clock.tick(FPS)
        
        
    
