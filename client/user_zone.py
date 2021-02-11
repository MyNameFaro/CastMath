import pygame
import sys
from method import *
from component import *
import voice_control
from threading import Thread
import database
import dynamic_course

pygame.init()

#this_page IS 'study_zone'

clock = pygame.time.Clock()
running = True

class Column():
    def __init__(self , n):
        self.n = n
        self.background = Object(pygame.image.load('./src/pic/study_zone/white_bg_1.png').convert(),CENTER_X ,CENTER_Y)
    def draw(self):
        self.background.draw()

class Evalution():
    def __init__(self,data , x):
        self.level1 = Text_button("Course 1 : Level "+str(data["level1"]), CENTER_X - 150 + + x, CENTER_Y - 250 , left = True , color=(255 , 0 , 0))
        self.progress1 = Progress(1 , (255 , 0 , 0) , CENTER_X + x , CENTER_Y - 190,percent = (int(data['progress1']) / dynamic_course.COUSE1) * 100,infinite=True , text="Success " + str((int(data['progress1']) / dynamic_course.COUSE1) * 100) +"%")
        self.level2 = Text_button("Course 2 : Level "+str(data["level2"]), CENTER_X - 150 + x, CENTER_Y - 130, left = True , color=(0 , 128 , 0))
        self.progress2 = Progress(1 , (0 , 128 , 0) , CENTER_X + x, CENTER_Y - 70,percent = (int(data['progress2']) / dynamic_course.COUSE2) * 100,infinite=True , text="Success " + str((int(data['progress2']) / dynamic_course.COUSE2) * 100) +"%")
        self.level3 = Text_button("Course 3 : Level "+str(data["level3"]), CENTER_X - 150+ x, CENTER_Y - 10 , left = True , color=(0 , 102 , 204))
        self.progress3 = Progress(1 , (0 , 102 , 204) , CENTER_X + x, CENTER_Y + 50,percent = (int(data['progress3']) / dynamic_course.COUSE3) * 100,infinite=True, text="Success " + str((int(data['progress3']) / dynamic_course.COUSE3) * 100) +"%")
        self.level4 = Text_button("Course 4 : Level "+str(data["level4"]), CENTER_X - 150+ x, CENTER_Y + 110 , left = True , color=(128 , 0 , 128))
        self.progress4 = Progress(1 , (128 , 0 , 128) , CENTER_X + x, CENTER_Y + 170,percent = (int(data['progress4']) / dynamic_course.COUSE4) * 100,infinite=True, text="Success " + str((int(data['progress4']) / dynamic_course.COUSE4) * 100) +"%")
    def run(self):
        self.progress1.run(0)
        self.progress2.run(0)
        self.progress3.run(0)
        self.progress4.run(0)
    def draw(self , time):
        self.level1.draw()
        self.level2.draw()
        self.level3.draw()
        self.level4.draw()

        self.progress1.update(time)
        self.progress2.update(time)
        self.progress3.update(time)
        self.progress4.update(time)

        
    

##MENU OF USER_ZONE
def main(session) : 

    FPS = 60
    running = True

    try :
        data = database.get_doc(u'learning' , session["user_id"])
    except :
        link_to('menu')
        running = False
    
    n = 0

    profile = Object(pygame.image.load('./src/pic/menu/profile_1.png').convert_alpha(),CENTER_X - 200 ,CENTER_Y - 180)
    background = Object(pygame.image.load('./src/pic/study_zone/CLASSROOM.png').convert(),CENTER_X ,CENTER_Y)
    shade = Object(pygame.image.load('./src/pic/menu/dark_mask.png').convert_alpha(),CENTER_X ,CENTER_Y)
    title = Text("ผู้เรียน" , (255 , 255 , 0) , CENTER_X , CENTER_Y - 340,size=100)
    button_menu = Button(pygame.image.load('./src/pic/study_zone/menu.png').convert_alpha(), CENTER_X , SCREEN_HEIGHT - 200)
    edit = Button(pygame.image.load('./src/pic/menu/edit.png').convert_alpha(), CENTER_X - 200, CENTER_Y + 30)
    logout = Button(pygame.image.load('./src/pic/menu/logout.png').convert_alpha(), CENTER_X - 200, CENTER_Y + 100)

    name = Text(session['username'], (36 , 36 , 36) , CENTER_X - 200 , CENTER_Y - 70)
    evalution = Evalution(data,100)
    evalution.run()    

    time = 0.0

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
                if edit.onclick():
                    link_to('regis')
                    running = False
                if logout.onclick():
                    link_to('login')
                    running = False
        
        col_1 = Column(n + 1)


        background.draw()
        shade.draw()

        col_1.draw()
        title.draw()
        button_menu.draw()

        name.draw()
        profile.draw()

        edit.draw()
        logout.draw()

        evalution.draw(time)
        #link_to('unit_1')
        #running = False
        pygame.display.update()
        clock.tick(FPS)


