import pygame
import random
import database

pygame.init()

def id():
    return str(random.randint(1000000,9999999))
#CHANGE_PAGE

PAGE = None
ARGUMENT = None

def link_to(page_next , arg = True) :
    global PAGE
    global ARGUMENT
    PAGE = page_next
    ARGUMENT = arg
    
def get_page() :
    return PAGE , ARGUMENT

#LOGIN and Register



#def get_login(data) :
    #database.search(u'users',data[])

#def login(data) :
    