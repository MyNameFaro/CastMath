import pygame
import sys
from method import *
from component import *
import voice_control
from threading import Thread

pygame.init()

#this_page IS 'study_zone'

clock = pygame.time.Clock()
running = True

class Column():
    def __init__(self , n):
        self.n = n
        self.background = Object(pygame.image.load('./src/pic/study_zone/white_bg_1.png'),CENTER_X ,CENTER_Y)
    def draw(self):
        self.background.draw()
    

##MENU OF STUDY_ZONE
def main(session) : 

    FPS = 60
    running = True

    n = 0

    background = Object(pygame.image.load('./src/pic/menu/BG.jpeg').convert(),CENTER_X ,CENTER_Y)
    shade = Object(pygame.image.load('./src/pic/menu/dark_mask.png').convert_alpha(),CENTER_X ,CENTER_Y)
    title = Text("สนุกสนาน" , (255 , 255 , 0) , CENTER_X , CENTER_Y - 340, size=100)
    search = Textbox(pygame.image.load('src/pic/login/textbox.png').convert_alpha() , u"ค้นหาห้อง" , CENTER_X - 70, CENTER_Y - 250)
    search_button = Text_button("ค้นหา" , CENTER_X + 200, CENTER_Y - 250  , color = (40 , 40 , 40))
    create = Button(pygame.image.load('./src/pic/play_zone/create.png').convert_alpha(), CENTER_X , CENTER_Y + 250)
    button_menu = Button(pygame.image.load('./src/pic/study_zone/menu.png').convert_alpha(), CENTER_X , SCREEN_HEIGHT - 200)
    button_left = Button(pygame.image.load('./src/pic/study_zone/left.png').convert_alpha(), CENTER_X - 350, CENTER_Y)
    button_right = Button(pygame.image.load('./src/pic/study_zone/right.png').convert_alpha(), CENTER_X + 350, CENTER_Y)

    while running:

        button_lists = []
        game_list = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if button_left.onclick() :
                    n = (n + 1) % 4
                if button_right.onclick() :
                    n = (n - 1) % 4
                if button_menu.onclick() :
                    link_to('menu')
                    running = False
                if search.onclick():
                    search.get_active()
                if create.onclick():
                    link_to('create_room',session)
                    running = False
                for b in button_lists:
                    if b.onclick():
                        link_to('menu')
            if event.type == pygame.KEYDOWN:
                if search != None:
                    if event.key == pygame.K_BACKSPACE:
                        search.input("BACK")
                    else :
                        char = event.unicode
                        search.input(char)
        
        col_1 = Column(n + 1)


        background.draw()
        shade.draw()

        col_1.draw()
        title.draw()
        button_menu.draw()
        button_left.draw()
        button_right.draw()
        search.draw()
        create.draw()
        search_button.draw()

        i = 0
        for g in game_list:
            button_list = Text_button(g["id"] + " " + g["name"] , CENTER_X - 280, CENTER_Y - 180 + (50 * i)  , color = (225 , 0 , 40) ,left=True)
            button_lists.append(button_list)
            i += 1

        for b in button_lists:
            b.draw()

        #link_to('unit_1')
        #running = False
        pygame.display.update()
        clock.tick(FPS)

def create_room(session) : 

    FPS = 60
    running = True

    n = 0

    room_id = id()

    background = Object(pygame.image.load('./src/pic/menu/BG.jpeg').convert(),CENTER_X ,CENTER_Y)
    shade = Object(pygame.image.load('./src/pic/menu/dark_mask.png').convert_alpha(),CENTER_X ,CENTER_Y)
    title = Text(str(room_id) , (255 , 255 , 0) , CENTER_X , CENTER_Y - 340, size=100)
    #search = Textbox(pygame.image.load('src/pic/login/textbox.png') , u"ค้นหาห้อง" , CENTER_X, CENTER_Y - 300)
    #search_button = Text_button("ค้นหา" , CENTER_X + 200, CENTER_Y - 250  , color = (40 , 40 , 40))
    start = Button(pygame.image.load('./src/pic/play_zone/start.png').convert_alpha(), CENTER_X , CENTER_Y + 250)
    button_menu = Button(pygame.image.load('./src/pic/study_zone/menu.png').convert_alpha(), CENTER_X , SCREEN_HEIGHT - 200)
    button_left = Button(pygame.image.load('./src/pic/study_zone/left.png').convert_alpha(), CENTER_X - 350, CENTER_Y)
    button_right = Button(pygame.image.load('./src/pic/study_zone/right.png').convert_alpha(), CENTER_X + 350, CENTER_Y)

    while running:

        button_lists = []
        game_list = [{"id":session['user_id'] , "name" : session['username']}]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if button_left.onclick() :
                    n = (n + 1) % 4
                if button_right.onclick() :
                    n = (n - 1) % 4
                if button_menu.onclick() :
                    link_to('menu')
                    running = False
                if start.onclick() :
                    link_to('seeker', session)
                    running = False
            if event.type == pygame.KEYDOWN:
                if search != None:
                    if event.key == pygame.K_BACKSPACE:
                        search.input("BACK")
                    else :
                        char = event.unicode
                        search.input(char)
        
        col_1 = Column(n + 1)


        background.draw()
        shade.draw()

        col_1.draw()
        title.draw()
        button_menu.draw()
        button_left.draw()
        button_right.draw()
        #search.draw()
        start.draw()
        #search_button.draw()

        i = 0
        for g in game_list:
            button_list = Text_button(g["id"] + " " + g["name"] , CENTER_X - 280, CENTER_Y - 180 + (50 * i)  , color = (225 , 0 , 40) ,left=True)
            button_lists.append(button_list)
            i += 1

        for b in button_lists:
            b.draw()

        #link_to('unit_1')
        #running = False
        pygame.display.update()
        clock.tick(FPS)



