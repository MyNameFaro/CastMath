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

    user_input = ""
    voice_ans = False

    eqt , ans = dynamic_course.get_exercise_real()

    while running:
        
        screen.fill((0 , 0 ,0))
        
        time += 1 / FPS
       
        if voice_ans :
            user_input = str(voice_control.ANS)

        equation = Text(eqt , (255 ,255 ,255) , CENTER_X , CENTER_Y , size=50)
        input_box = Text(user_input , (255 ,255 ,255) , CENTER_X , CENTER_Y + 300)

        #TIME_LIMIT = len(ans)
        #progress = Progress(TIME_LIMIT , (0 , 200 , 200) , CENTER_X , CENTER_Y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    if str(ans) == user_input :
                        voice_ans = False
                        eqt , ans = dynamic_course.get_exercise_real()
                        user_input = ""
                elif event.key == pygame.K_t:
                    progress.run(time)
                    voice_ans = True
                    voice = Thread(target = voice_control.main, args = [TIME_LIMIT])
                    voice.start()
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input = user_input + event.unicode
        

        progress.update(time)
        equation.draw()
        input_box.draw()

        pygame.display.update()
        clock.tick(FPS)

