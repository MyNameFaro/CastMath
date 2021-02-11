import pygame
import sys
from method import *
from component import *
import voice_control
import dynamic_course
from threading import Thread

pygame.init()

#this_page IS 'study_zone'

clock = pygame.time.Clock()
running = True

def main(session) :
    #MATH OPERATION
    FPS = 60
    running = True

    padding = 200

    time = 0.00

    score_p1 = 0

    TIME_LIMIT = 2
    
    progress = Progress(TIME_LIMIT , (0 , 200 , 200) , CENTER_X , 700,text="ลองพูด")
    background = Object(pygame.image.load('./src/GAME/seeker/MC/2x/x2.jpeg') , CENTER_X , CENTER_Y)
    button_menu = Button(pygame.image.load('./src/pic/study_zone/menu.png'), SCREEN_WIDTH - 80 - padding ,80 + padding)

    user_input = ""
    voice_ans = False

    ex = random.choice([dynamic_course.get_exercise_real , dynamic_course.get_exercise_pro])

    eqt , ans = ex()
    
    time_start = 0
    
    data = dynamic_course.Data( database.get_doc(u'dataset' , u'hunza_game')['value'] , level = database.get_doc(u'learning',session['user_id'])[u'level1'])
    data.CRITICAL = 7

    button_left = Button(pygame.image.load('./src/pic/study_zone/left.png').convert_alpha(), 150 + padding, SCREEN_HEIGHT - 80- padding)

    while running:
        score = Text_button(str(score_p1), SCREEN_WIDTH - 300, 200 , right = True , color=(255 , 120 , 0) ,size=75)
        
        time += 1 / FPS

        level = data.get_level()
        #print(level)

        if (level <= 0) or (int(score_p1) < -30) or (int(score_p1) > 700):
            database.update(u"dataset",u"hunza_game",{
                u"value" : data.get_data()
            })
            database.update(u"learning",session["user_id"],{
                u"level1" : level
            })
            link_to('course',[{
                "course" : '1',
                "page" : database.get_doc(u'learning',session['user_id'])['progress1']
            },session])
            running = False
       
        if voice_ans :
            user_input = str(voice_control.ANS)

        equation = Text(eqt , (40 ,40 ,40) , CENTER_X , CENTER_Y , size=90)
        input_box = Text(user_input , (255 ,0 ,0) , CENTER_X , CENTER_Y + 300 , size=200)
        

        #TIME_LIMIT = len(ans)
        #progress = Progress(TIME_LIMIT , (0 , 200 , 200) , CENTER_X , CENTER_Y)

        red_bg = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if button_menu.onclick() :
                    link_to('menu')
                    running = False
                if button_left.onclick() :
                    database.update(u"dataset",u"hunza_game",{
                        u"value" : data.get_data()
                    })
                    database.update(u"learning",session["user_id"],{
                        u"level1" : level
                    })
                    link_to('course',[{
                        "course" : '1',
                        "page" : database.get_doc(u'learning',session['user_id'])['progress1']
                    },session])
                    running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    if str(ans) == user_input :
                        point = int(50 - time + time_start)
                        #print(time - time_start)
                        data.train()
                        data.test(point)
                        data.update()
                        data.append([point])
                        #print(data.get_m())
                        score_p1 += point  ##SCORE
                    else :
                        score_p1 -= 10
                        #data.append([(time - time_start) * (-1)])
                        #data.train()
                        red_bg = True
                    time_start = time
                    voice_ans = False
                    ex = random.choice([dynamic_course.get_exercise_real])
                    eqt , ans = ex(level)
                    user_input = ""
                        
                        
                elif event.key == pygame.K_e:
                    progress.run(time)
                    voice_ans = True
                    voice = Thread(target = voice_control.main, args = [TIME_LIMIT])
                    voice.start()
                elif event.key == pygame.K_BACKSPACE:
                    if voice_ans:
                        voice_ans = False
                    user_input = user_input[:-1]
                else:
                    if voice_ans:
                        voice_ans = False
                    user_input = user_input + event.unicode
        
        if red_bg:
            screen.fill((255 , 0 , 0))
        else:
            background.draw()
        progress.update(time)
        equation.draw()
        input_box.draw()
        button_menu.draw()
        score.draw()
        button_left.draw()

        data.update()

        pygame.display.update()
        clock.tick(FPS)

