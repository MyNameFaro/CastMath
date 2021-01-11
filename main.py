import pygame
import sys
import component
import method

pygame.init()
screen = pygame.display.set_mode((500 , 500))
pygame.display.set_caption('ถ้้าไม่มีอะไรจะทำอย่ามัวแต่นอนตีพุง')
clock = pygame.time.Clock()

position_x = 100
position_y = 100

#info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
#screen_width,screen_height = info.current_w,info.current_h

#print(screen_width)
#print(screen_height)

box_surface = pygame.image.load('img.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if pygame.key.get_pressed()[pygame.K_w]:
        print("UP")
        position_y -= 1
    elif pygame.key.get_pressed()[pygame.K_s]:
        position_y += 1
    elif pygame.key.get_pressed()[pygame.K_d]:
        position_x += 1
    elif pygame.key.get_pressed()[pygame.K_a]:
        position_x -= 1

    box_surface = pygame.transform.flip(box_surface,False,True)
    screen.blit(box_surface,(position_x , position_y))
    pygame.display.update()
    clock.tick(60)
    
