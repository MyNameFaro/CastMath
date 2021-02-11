import pygame
import os
import random
import math
from pygame.math import Vector2
from component import *
from method import *
import dynamic_course
import voice_control
import string
from threading import Thread
import pickle
import socket

pygame.init()
#H+W Screen
Width = SCREEN_WIDTH
Height = SCREEN_HEIGHT

#Color
Pink = (255,153,204)
RED = (255,0,0)
White = (255,255,255)
Black = (0,0,0)
Darkslateblue = (72,61,139)
Indigo = (75,0,130)
Rebeccapurple = (102,51,153)
#screen = pygame.display.set_mode((Width,Height))
#pygame.display.set_caption('Test')
game_folder = os.path.dirname(__file__)
img_folder = "./src/GAME/seeker"
direction = 0
FPS = 60
clock = pygame.time.Clock()
background_pic = os.path.join(img_folder,'MC','2x','x2.jpeg')
background = pygame.image.load(background_pic)

global_session = {
    "user_id" : "123",
    "username" : "Website"
}

######################################Seeker_class
 
class Seeker(pygame.sprite.Sprite):

    def __init__(self , name , seeker_id):
        pygame.sprite.Sprite.__init__(self)
        Seeker_idle = os.path.join(img_folder,'MC','x3','ไฟล์_002.png')
        self.type = "Seeker"
        self.name = name
        self.id = seeker_id
        self.image = pygame.image.load(Seeker_idle)
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        ##################################Seeker_position
        self.rect.centerx = Width / 2
        self.rect.bottom = Height / 2

    def update(self):
        if global_session['user_id'] == self.id:
            Seeker_left = os.path.join(img_folder,'MC','x3','ไฟล์_001.png')
            Seeker_right = os.path.join(img_folder,'MC','x3','ไฟล์_000.png')
            Seeker_up = os.path.join(img_folder,'MC','x3','ไฟล์_003.png')
            Seeker_down = os.path.join(img_folder,'MC','x3','ไฟล์_002.png')
            #Seeker_look_direction = 
            self.speedx = 0
            self.speedy = 0

            ############################################seeker move funtion
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_a]:
                self.image = pygame.image.load(Seeker_left).convert()
                self.image.set_colorkey(Black)
                self.speedx = -5
            
            if keystate[pygame.K_d]:
                self.image = pygame.image.load(Seeker_right).convert()
                self.image.set_colorkey(Black)
                self.speedx = 5
                
            if keystate[pygame.K_s]:
                self.image = pygame.image.load(Seeker_down).convert()
                self.image.set_colorkey(Black)
                self.speedy = 5
                
            if keystate[pygame.K_w]:
                self.image = pygame.image.load(Seeker_up).convert()
                self.image.set_colorkey(Black)
                self.speedy = -5
            
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            ###################for avoid seeker run out of map
            if self.rect.right > Width + 10:
                self.rect.right = Width + 10
            
            if self.rect.left < -10:
                self.rect.left = -10
            
            if self.rect.top < 4:
                self.rect.top = 4
            
            if self.rect.bottom > Height:
                self.rect.bottom = Height

    ####################################Seeker attack
    def attack(self,a_e , angle_degree):
        Seeker_left = os.path.join(img_folder,'MC','x3','ไฟล์_001.png')
        Seeker_right = os.path.join(img_folder,'MC','x3','ไฟล์_000.png')
        Seeker_up = os.path.join(img_folder,'MC','x3','ไฟล์_003.png')
        Seeker_down = os.path.join(img_folder,'MC','x3','ไฟล์_002.png')
        #attack_effects.add(a_e)
        attack_angle = angle_degree
        

        if attack_angle <= 45 and attack_angle >= -45:
            self.image = pygame.image.load(Seeker_right).convert()
            self.image.set_colorkey(Black)

        if attack_angle < -45 and attack_angle >= -135:
            self.image = pygame.image.load(Seeker_up).convert()
            self.image.set_colorkey(Black)
        
        if (attack_angle > 135 and attack_angle <= 180) or (attack_angle < -135 and attack_angle >= -180):
            if (attack_angle < -135 and attack_angle >= -180) or (attack_angle > 135 and attack_angle <= 180):
                self.image = pygame.image.load(Seeker_left).convert()
                self.image.set_colorkey(Black)
        
        if attack_angle >= 45 and attack_angle <=135:
                self.image = pygame.image.load(Seeker_down).convert()
                self.image.set_colorkey(Black)

SERVER_IP = "192.168.43.175"
PORT = 3000
BUFFER = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((SERVER_IP , PORT))

def main():

    
    seeker = pickle.loads(server.recv(BUFFER))
    #seeker = server_data[0]
    #seeker_label = server_data[1]
    #enemy = server_data[2]
    #enemy_label = server_data[3]
    #hps = server_data[4]
    #attack_effects = server_data[5]


    sk = Seeker(global_session['username'] , global_session['user_id'])

    seeker.add(sk)
    server.send(pickle.dumps(seeker))

    Game_running = True
    char_hit_status = False
    char_hit_count = 0
    score_p1 = 0

    time = 0.00

    TIME_LIMIT = 2


    while Game_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

        seeker = pickle.loads(server.recv(BUFFER))
        if not seeker:
            break        
        seeker.update()

            ###################################hit enemy function
            
        screen.blit(background,background.get_rect(center = (Width/2, Height/2)))
            #screen.blit(Score_p1,250,250)
        seeker.draw(screen)
            #hps.draw(screen)

        server.send(pickle.dumps(seeker))

        clock.tick(FPS)
        pygame.display.update()
            

main()