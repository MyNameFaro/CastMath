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
def main(argument) : 

    FPS = 60
    running = True

    n = 0

    background = Object(pygame.image.load('./src/pic/menu/BG.jpeg'),CENTER_X ,CENTER_Y)
    shade = Object(pygame.image.load('./src/pic/menu/dark_mask.png'),CENTER_X ,CENTER_Y)
    title = Text("สนุกสนาน" , (255 , 255 , 0) , CENTER_X , CENTER_Y - 340, size=100)
    search = Textbox(pygame.image.load('src/pic/login/textbox.png') , u"ค้นหาห้อง" , CENTER_X - 70, CENTER_Y - 250)
    search_button = Text_button("ค้นหา" , CENTER_X + 200, CENTER_Y - 250  , color = (40 , 40 , 40))
    button_menu = Button(pygame.image.load('./src/pic/study_zone/menu.png'), CENTER_X , SCREEN_HEIGHT - 200)
    button_left = Button(pygame.image.load('./src/pic/study_zone/left.png'), CENTER_X - 350, CENTER_Y)
    button_right = Button(pygame.image.load('./src/pic/study_zone/right.png'), CENTER_X + 350, CENTER_Y)

    while running:

        button_lists = []
        game_list = [{"id":"00001" , "name" : "กุ๊กกิ๊ก"} , {"id":"00001" , "name" : "กุ๊กกิ๊ก"} , {"id":"00001" , "name" : "กุ๊กกิ๊ก"}]

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


def course(data) :
    #MATH OPERATION
    FPS = 60
    running = True

    padding = 200

    time = 0.00

    TIME_LIMIT = 1
    try :
        background = Object(pygame.image.load('./src/pic/study_zone/COURSE/' + str(data['course']) + str(data['session']) + str(data['page']) + '.png') , CENTER_X , CENTER_Y)
    except :
        link_to('study_zone')
        running = False   
    button_menu = Button(pygame.image.load('./src/pic/study_zone/menu.png'), CENTER_X , SCREEN_HEIGHT - 80 - padding)
    button_left = Button(pygame.image.load('./src/pic/study_zone/left.png'), 150 + padding, SCREEN_HEIGHT - 80- padding)
    button_right = Button(pygame.image.load('./src/pic/study_zone/right.png'), SCREEN_WIDTH - 150 - padding, SCREEN_HEIGHT - 80- padding)

    progress = Progress(TIME_LIMIT , (0 , 200 , 200) , CENTER_X , CENTER_Y)

    while running:

        time += 1 / FPS
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if button_menu.onclick() :
                    link_to('menu')
                    running = False
                if button_right.onclick() :
                    link_to('course',{
                        "course" : data['course'],
                        "session" : data['session'],
                        "page" : str(int(data['page']) + 1)
                    })
                    running = False
                if button_left.onclick() :
                    link_to('course',{
                        "course" : data['course'],
                        "session" : data['session'],
                        "page" : str(int(data['page']) - 1)
                    })
                    running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    progress.run(time)
                    voice = Thread(target = voice_control.main, args = [TIME_LIMIT])
                    voice.start()
        
        if voice_control.ANS == "NEXT" :
            voice_control.ANS = 0
            link_to('course',{
            "course" : data['course'],
            "session" : data['session'],
            "page" : str(int(data['page']) + 1)
            })
            running = False

        if voice_control.ANS == "PREVIOUS" :
            voice_control.ANS = 0
            link_to('course',{
            "course" : data['course'],
            "session" : data['session'],
            "page" : str(int(data['page']) - 1)
            })
            running = False

        background.draw()
        button_right.draw()
        button_left.draw()
        progress.update(time)
        button_menu.draw()

        pygame.display.update()
        clock.tick(FPS)

