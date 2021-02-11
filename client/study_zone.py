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
        self.img = Object(pygame.image.load('./src/pic/study_zone/logo_' + str(self.n) + '.png').convert() , CENTER_X , CENTER_Y - 50)
        self.title = Button(pygame.image.load('./src/pic/study_zone/title_' + str(self.n) + '_little.png').convert(), CENTER_X - 5 , CENTER_Y + 225)
        self.pos = None
        self.click = None
    def draw(self):
        self.img.draw()
        self.title.draw()
    def onclick(self):
        self.pos = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if self.img.rect.collidepoint(self.pos) or self.title.rect.collidepoint(self.pos):
            for c in self.click :
                if c > 0 :
                    return True
        else :
            return False

##MENU OF STUDY_ZONE
def main(session) : 

    FPS = 60
    running = True

    n = 0

    background = Object(pygame.image.load('./src/pic/study_zone/CLASSROOM.png').convert(),CENTER_X ,CENTER_Y)
    shade = Object(pygame.image.load('./src/pic/menu/dark_mask.png').convert_alpha(),CENTER_X ,CENTER_Y)
    title = Text("เรียนรู้" , (255 , 255 , 0) , CENTER_X , CENTER_Y - 340,size=100)
    button_menu = Button(pygame.image.load('./src/pic/study_zone/menu.png').convert_alpha(), CENTER_X , SCREEN_HEIGHT - 200)
    button_left = Button(pygame.image.load('./src/pic/study_zone/left.png').convert_alpha(), CENTER_X - 350, CENTER_Y)
    button_right = Button(pygame.image.load('./src/pic/study_zone/right.png').convert_alpha(), CENTER_X + 350, CENTER_Y)
    

    while running:
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
        
        col_1 = Column(n + 1)


        background.draw()
        shade.draw()

        if col_1.onclick() :
            link_to('course',[{
                "course" : str(n + 1),
                "page" : database.get_doc(u'learning',session['user_id'])['progress' + str(n + 1)]
            },session])
            running = False

        col_1.draw()
        title.draw()
        button_menu.draw()
        button_left.draw()
        button_right.draw()

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
    time_start = 0.0

    TIME_LIMIT = 1

    button_menu = Button(pygame.image.load('./src/pic/study_zone/menu.png').convert_alpha(), CENTER_X , SCREEN_HEIGHT - 80 - padding)
    button_left = Button(pygame.image.load('./src/pic/study_zone/left.png').convert_alpha(), 150 + padding, SCREEN_HEIGHT - 80- padding)
    button_right = Button(pygame.image.load('./src/pic/study_zone/right.png').convert_alpha(), SCREEN_WIDTH - 150 - padding, SCREEN_HEIGHT - 80- padding)

    learning = dynamic_course.Data( database.get_doc(u'dataset' , u'learning')['value'] , level = 0)

    progress = Progress(TIME_LIMIT , (0 , 200 , 200) , CENTER_X , 700 ,text = "ลองพูด",txt_color=(255 , 255 ,255))

    while running:

        try :
            background = Object(pygame.image.load('./src/pic/study_zone/COURSE/' + str(data[0]['course']) + str(data[0]['page']) + '.png').convert() , CENTER_X , CENTER_Y)
        except :
            link_to('study_zone')
            running = False   

        time += 1 / FPS

        if learning.get_level() < 0:
            database.update(u"dataset",u"learning",{
                u"value" : learning.get_data()
            })       
            link_to('test_faro' , data[1])
            running = False
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if button_menu.onclick() : 
                    link_to('menu')
                    running = False
                if button_right.onclick() : ###NEXT
                    data[0]['page'] = str(int(data[0]['page']) + 1)
                    
                    #print(time - time_start)

                    learning.train()
                    learning.test(time - time_start)
                    learning.update()
                    learning.append([time - time_start])

                    time_start = 0.0

                    database.update(u"learning",data[1]['user_id'],{
                        u"progress"+str(data[0]['course']) : str(int(data[0]['page']) + 1)
                    })
                    #running = False
                if button_left.onclick() :  ##LEFT
                    data[0]['page'] = str(int(data[0]['page']) - 1)
                    #running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_e:
                    progress.run(time)
                    voice = Thread(target = voice_control.main, args = [TIME_LIMIT])
                    voice.start()
                if event.key == pygame.K_a:  ##PREVIOUS
                    data[0]['page'] = str(int(data[0]['page']) - 1)
                    #running = False
                if event.key == pygame.K_d: ##NEXT
                    data[0]['page'] = str(int(data[0]['page']) + 1)
                    
                    #print(time - time_start)

                    learning.train()
                    learning.test(time - time_start)
                    learning.update()
                    learning.append([time - time_start])

                    time_start = 0.0

                    database.update(u"learning",data[1]['user_id'],{
                        u"progress"+str(data[0]['course']) : str(int(data[0]['page']) + 1)
                    }) 
                    #running = False
        if voice_control.ANS == "NEXT" :
            data[0]['page'] = str(int(data[0]['page']) + 1)
                    
                    #print(time - time_start)

            learning.train()
            learning.test(time - time_start)
            learning.update()
            learning.append([time - time_start])

            time_start = 0.0

            database.update(u"learning",data[1]['user_id'],{
                u"progress"+str(data[0]['course']) : str(int(data[0]['page']) + 1)
            })
            #running = False

        if voice_control.ANS == "PREVIOUS" :
            voice_control.ANS = 0
            data[0]['page'] = str(int(data[0]['page']) - 1)
            #running = False

        background.draw()
        if int(data[0]['page']) < dynamic_course.COUSE1:
            button_right.draw()
        if int(data[0]['page']) > 0:
            button_left.draw()
        progress.update(time)
        button_menu.draw()

        pygame.display.update()
        clock.tick(FPS)

