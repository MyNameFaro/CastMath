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

def main(data) :
    #MATH OPERATION
    FPS = 60
    running = True

    padding = 200

    time = 0.00

    TIME_LIMIT = 2
    

    progress = Progress(TIME_LIMIT , (0 , 200 , 200) , CENTER_X , CENTER_Y)
    background = Object(pygame.image.load('./src/GAME/seeker/MC/2x/x2.jpeg') , CENTER_X , CENTER_Y)
    button_menu = Button(pygame.image.load('./src/pic/study_zone/menu.png'), SCREEN_WIDTH - 80 - padding ,80 + padding)

    user_input = ""
    voice_ans = False

    ex = random.choice([dynamic_course.get_exercise_real , dynamic_course.get_exercise_pro])

    eqt , ans = ex()
    
    time_start = 0

    while running:
        
        data = dynamic_course.Data(level = -1)
        level = data.get_level() * (-1)
        
        background.draw()
        
        time += 1 / FPS
       
        if voice_ans :
            user_input = str(voice_control.ANS)

        equation = Text(eqt , (40 ,40 ,40) , CENTER_X , CENTER_Y , size=150)
        input_box = Text(user_input , (255 ,0 ,0) , CENTER_X , CENTER_Y + 300 , size=200)
        

        #TIME_LIMIT = len(ans)
        #progress = Progress(TIME_LIMIT , (0 , 200 , 200) , CENTER_X , CENTER_Y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if button_menu.onclick() :
                    link_to('menu')
                    running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    if str(ans) == user_input :
                        print(time - time_start)
                        data.append([time - time_start])
                        data.train()
                        data.update()
                        print(data.get_m())
                        time_start = time
                        voice_ans = False
                        ex = random.choice([dynamic_course.get_exercise_real , dynamic_course.get_exercise_pro , dynamic_course.get_exercise_real])
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
        
        progress.update(time)
        equation.draw()
        input_box.draw()
        button_menu.draw()

        data.update()

        pygame.display.update()
        clock.tick(FPS)

