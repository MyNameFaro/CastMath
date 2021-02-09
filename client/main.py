import pygame
import sys
import menu
import study_zone
import play_zone
import database
import login
import regis
import seeker
import test_faro
from component import *
from method import *

pygame.init()

screen_init()

clock = pygame.time.Clock()

#YRC PAGE

brand_time = 0.3 #LOGO TIME LONG
screen.fill((255 , 255 ,255))
yrc_logo = Object(pygame.image.load('./src/pic/YRC.png') ,CENTER_X , CENTER_Y)
yrc_logo.draw()
pygame.display.update()
#clock.tick(brand_time)

#link_to('login')
link_to('test_faro')

#PAGE REPRESENT

running = True

def exit(argument) :
    running = False #Close This Page
    pygame.quit()
    sys.exit()

session = {
    "user_id" : None,
    "username" : "TEST"
}

def get_regis(data) :
    database.add(u'users',data[u'id'],data) #add to user , data.id , data
    link_to('login')
    return 0

def get_login(data) :
    accout = database.search(u'users' , u'username' , data[u'username'])
    if len(accout) == 0:
        link_to('login' , False)
    else:
        for a in accout :
            if a[u'password'] == data[u'password'] :
                session['user_id'] = a[u'id']
                session['username'] = a[u'username']
                print(session['user_id'])
                link_to('menu' , session)
                return 0
        link_to('login' , False)
    
pages = {
    'menu' : menu.main,
    'study_zone' : study_zone.main,
    'play_zone' : play_zone.main,
    'course' : study_zone.course,
    'exit' : exit,
    'play' : play_zone.main,
    'login' : login.main,
    'regis' : regis.main,
    'get_regis' : get_regis,
    'get_login' : get_login,
    'seeker' : seeker.main,
    'test_faro' : test_faro.main
} 

while running :
    page , argument = get_page()
    if argument == True:
        pages[page](session)
    else:
        pages[page](argument) 

 
    
