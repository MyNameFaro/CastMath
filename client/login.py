# -*- coding: utf-8 -*-

import pygame
import sys
from method import *
from component import *

pygame.init()


clock = pygame.time.Clock()
running = True

def close() :
    print("Click")

def main(argument) : 
    FPS = 60
    running = True

    username = Textbox(pygame.image.load('src/pic/login/textbox.png') , u"ชื่อผู้ใช้" , CENTER_X , CENTER_Y - 70)
    password = Textbox(pygame.image.load('src/pic/login/textbox.png') ,u"รหัสผ่าน" , CENTER_X , CENTER_Y ,password = True)
    submit = Button(pygame.image.load('./src/pic/login/login.png') , CENTER_X , CENTER_Y + 100)
    regis = Button(pygame.image.load('./src/pic/login/regis.png') , CENTER_X , CENTER_Y + 170)
    if not argument : #login fail
        title = Text(u"กรุณากรอกข้อมูลใหม่" , (255 , 0 , 0) ,CENTER_X , CENTER_Y - 160 ,50)
    else :
        title = Text(u"เข้าสู่ระบบ" , (40 , 40 , 40) ,CENTER_X , CENTER_Y - 160 ,50)
    
    active = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    link_to('get_login' , {
                        u'username' : username.get_value(),
                        u'password' : password.get_value()
                    })
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                if username.onclick() :
                    if active != None :
                        active.get_active()
                    active = username
                    active.get_active()
                if password.onclick() :
                    if active != None :
                        active.get_active()
                    active = password
                    active.get_active()
                if submit.onclick() :
                    link_to('get_login' , {
                        u'username' : username.get_value(),
                        u'password' : password.get_value()
                    })
                    running = False
                if regis.onclick() :
                    link_to('regis')
                    running = False
            if event.type == pygame.KEYDOWN:
                if active != None:
                    if event.key == pygame.K_BACKSPACE:
                        active.input("BACK")
                    else :
                        char = event.unicode
                        active.input(char)
                
        screen.fill((255 , 255 , 255)) # To Bright Tone Background

        username.draw()
        password.draw()
        submit.draw()
        regis.draw()
        title.draw()

        pygame.display.update()
        clock.tick(FPS)
        
        
    
