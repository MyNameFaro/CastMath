
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

    name = Textbox(pygame.image.load('src/pic/login/textbox.png') ,u'ชื่อ' , CENTER_X , CENTER_Y - 210)
    lastname = Textbox(pygame.image.load('src/pic/login/textbox.png') ,u'นามสกุล' , CENTER_X , CENTER_Y - 140)
    username = Textbox(pygame.image.load('src/pic/login/textbox.png') ,u'ชื่อผู้เรียน' , CENTER_X , CENTER_Y - 70)
    password = Textbox(pygame.image.load('src/pic/login/textbox.png') ,u'รหัสผ่าน' , CENTER_X , CENTER_Y , password = True)
    email = Textbox(pygame.image.load('src/pic/login/textbox.png') ,u'E-Mail' , CENTER_X , CENTER_Y + 70)
    submit = Button(pygame.image.load('./src/pic/login/submit.png') , CENTER_X , CENTER_Y + 170)
    have_accout = Button(pygame.image.load('./src/pic/login/have_accout.png') , CENTER_X , CENTER_Y + 240)
    title = Text(u'สมัครสมาชิก' , (40 , 40 , 40) ,CENTER_X , CENTER_Y - 300 , 50)
    
    active = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    link_to('get_regis' , {
                        u'username' : username.get_value(),
                        u'id' : id(),
                        u'e-mail' : email.get_value(),
                        u'password' : str(password.get_value()),
                        u'lastname' : lastname.get_value(),
                        u'name' : name.get_value()
                    })
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                if name.onclick() :
                    if active != None :
                        active.get_active()
                    active = name
                    active.get_active()
                if lastname.onclick() :
                    if active != None :
                        active.get_active()
                    active = lastname
                    active.get_active()
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
                if username.onclick() :
                    if active != None :
                        active.get_active()
                    active = username
                    active.get_active()
                if email.onclick() :
                    if active != None :
                        active.get_active()
                    active = email
                    active.get_active()
                if submit.onclick() :
                    link_to('get_regis' , {
                        u'username' : username.get_value(),
                        u'id' : id(),
                        u'e-mail' : email.get_value(),
                        u'password' : str(password.get_value()),
                        u'lastname' : lastname.get_value(),
                        u'name' : name.get_value()
                    })
                    running = False
                if have_accout.onclick() :
                    link_to('login')
                    running = False
            if event.type == pygame.KEYDOWN:
                if active != None:
                    if event.key == pygame.K_BACKSPACE:
                        active.input("BACK")
                    else :
                        char = event.unicode
                        active.input(char)
                
        screen.fill((255 , 255 , 255)) # To Bright Tone Background

        name.draw()
        lastname.draw()
        username.draw()
        password.draw()
        email.draw()
        submit.draw()
        have_accout.draw()
        title.draw()

        pygame.display.update()
        clock.tick(FPS)
        
        
    
