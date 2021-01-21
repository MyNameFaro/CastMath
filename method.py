import pygame

pygame.init()

#CHANGE_PAGE

page = None

def link_to(page_next) :
    global page
    page = page_next
    
def get_page() :
    return page