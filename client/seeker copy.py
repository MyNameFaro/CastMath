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
background = pygame.image.load(background_pic).convert()
global_session = []

######################################Seeker_class
 
class Seeker(pygame.sprite.Sprite):

    def __init__(self , name , seeker_id):
        pygame.sprite.Sprite.__init__(self)
        Seeker_idle = os.path.join(img_folder,'MC','x3','ไฟล์_002.png')
        self.type = "Seeker"
        self.name = name
        self.id = seeker_id
        self.image = pygame.image.load(Seeker_idle).convert_alpha()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        ##################################Seeker_position
        self.rect.centerx = Width / 2
        self.rect.bottom = Height / 2

    def update(self):
    #def update(self,Attack_effect):
        #if session
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
            self.image = pygame.image.load(Seeker_left).convert_alpha()
            self.image.set_colorkey(Black)
            self.speedx = -5
        
        if keystate[pygame.K_d]:
            self.image = pygame.image.load(Seeker_right).convert_alpha()
            self.image.set_colorkey(Black)
            self.speedx = 5
            
        if keystate[pygame.K_s]:
            self.image = pygame.image.load(Seeker_down).convert_alpha()
            self.image.set_colorkey(Black)
            self.speedy = 5
            
        if keystate[pygame.K_w]:
            self.image = pygame.image.load(Seeker_up).convert_alpha()
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
            self.image = pygame.image.load(Seeker_right).convert_alpha()
            self.image.set_colorkey(Black)

        if attack_angle < -45 and attack_angle >= -135:
            self.image = pygame.image.load(Seeker_up).convert_alpha()
            self.image.set_colorkey(Black)
        
        if (attack_angle > 135 and attack_angle <= 180) or (attack_angle < -135 and attack_angle >= -180):
            if (attack_angle < -135 and attack_angle >= -180) or (attack_angle > 135 and attack_angle <= 180):
                self.image = pygame.image.load(Seeker_left).convert_alpha()
                self.image.set_colorkey(Black)
        
        if attack_angle >= 45 and attack_angle <=135:
                self.image = pygame.image.load(Seeker_down).convert_alpha()
                self.image.set_colorkey(Black)

class Seeker_label(pygame.sprite.Sprite):

    def __init__(self , name , id):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.id = id
        self.type = "Seeker_label"
        self.image = font.render(name, True,(40 , 40 , 40))
        self.rect = self.image.get_rect()
        ##################################Seeker_position
        self.rect.centerx = Width / 2
        self.rect.bottom = Height / 2
        self.rect.bottom -= 70
        self.speedx = 0
        self.speedy = 0

    def update(self):
    #def update(self,Attack_effect):
        if global_session['user_id'] == self.id:
            self.speedx = 0
            self.speedy = 0
            ############################################seeker move funtion
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_a]:
                self.speedx = -5
            
            if keystate[pygame.K_d]:
                self.speedx = 5
                
            if keystate[pygame.K_s]:
                self.speedy = 5
                
            if keystate[pygame.K_w]:
                self.speedy = -5
            
            self.rect.x += self.speedx
            self.rect.y += self.speedy


class HP1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = "HP1"
        self.image = pygame.Surface((40,40))
        self.image.fill(Pink)
        self.rect = self.image.get_rect()
        self.rect.left = 60 + padding
        self.rect.bottom = 70 + padding

class HP2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = "HP2"
        self.image = pygame.Surface((40,40))
        self.image.fill(Pink)
        self.rect =self.image.get_rect()
        self.rect.left = 120 + padding
        self.rect.bottom = 70 + padding

class HP3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = "HP3"
        self.image = pygame.Surface((40,40))
        self.image.fill(Pink)
        self.rect =self.image.get_rect()
        self.rect.left = 180 + padding
        self.rect.bottom = 70 + padding

def lose_hp(char_hit_count ,hp1 ,hp2 ,hp3):
    if char_hit_count == 1:
        hp1.image.fill(Black)
    elif char_hit_count == 2:
        hp2.image.fill(Black)
    elif char_hit_count == 3:
        hp3.image.fill(Black)

#########################################Enemy_class
class Enemy(pygame.sprite.Sprite):

    def __init__(self , ans ,x ,y ,id):
        pygame.sprite.Sprite.__init__(self)
        self.type = "Enemy"
        self.ans = ans
        self.id = id
        Enemy_idle = os.path.join(img_folder,'SLIME_IDLE.png')
        self.image = pygame.image.load(Enemy_idle).convert_alpha()
        self.rect = self.image.get_rect(center = (x , y))

class Enemy_label(pygame.sprite.Sprite):

    def __init__(self , eqt , x , y , id):
        pygame.sprite.Sprite.__init__(self)
        self.type = "Enemy_equation"
        ###############################################Enemy position
        self.id = id
        self.image = font.render(eqt, True,(40 , 40 , 40))
        self.rect = self.image.get_rect(center = (x , y - 30))

    
#########################################Attack_effect
class Attack_effect(Seeker):

    def __init__(self , x, y,width, height,speed,targetx,targety):
        super().__init__("0" , "0")
        angle = math.atan2(targety-y, targetx-x) #get angle to target in radians
        self.type = "Attack_effect"
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x = x
        self.y = y

        Enemy_idle = os.path.join(img_folder,'MON/cystle.png')
        self.image = pygame.image.load(Enemy_idle).convert_alpha()
        self.rect = self.image.get_rect(center = (x , y))

    def update(self):

        self.x = self.x + self.dx
        self.y = self.y + self.dy
        ###############################attack_effect position
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

def create_enemy(enemy , enemy_label , count): 
    for i in range(count):
        ex = random.choice([dynamic_course.get_exercise_pro , dynamic_course.get_exercise_real])
        eqt , ans = ex()
        y = random.randrange(169,900)
        x = random.randrange(267,1500) 
        em = Enemy(ans , x , y ,i)
        em_label = Enemy_label(eqt , x , y ,i)
        enemy.add(em)
        enemy_label.add(em_label)

#SERVER_IP = "192.168.43.210"
#PORT = 3000
#BUFFER = 4096

#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.connect((SERVER_IP , PORT))

def main(session):

    
    #server_data = pickle.loads(server.recv(BUFFER).decode('utf-8'))
    
    #seeker = server_data[0]
    #seeker_label = server_data[1]
    #enemy = server_data[2]
    #enemy_label = server_data[3]
    #hps = server_data[4]
    #attack_effects = server_data[5]

    seeker = pygame.sprite.Group()
    seeker_label = pygame.sprite.Group()

    global global_session 
    global_session = session

    sk = Seeker(session['username'] , session['user_id'])
    sk_label = Seeker_label(session['username'] , session['user_id']) #session['user_id'])

    seeker.add(sk)
    seeker_label.add(sk_label)
    ############INIT
    enemy = pygame.sprite.Group()
    enemy_label = pygame.sprite.Group()
    hps = pygame.sprite.Group
    attack_effects = pygame.sprite.Group()

    #Create HP
    hp1 = HP1()
    hps.add(hp1)
    hp2 = HP2()
    hps.add(hp2)
    hp3 = HP3()
    hps.add(hp3)

    em_count = 0
    wave = 1

    Game_running = True
    char_hit_status = False
    char_hit_count = 0
    score_p1 = 0

    time = 0.00

    TIME_LIMIT = 2

    
        
    create_enemy(enemy , enemy_label , 1)
    em_count += 1

    progress = Progress(TIME_LIMIT , (0 , 200 , 200) , CENTER_X ,700,text="ลองพูด")
    user_input = ""
    voice_ans = False
    time_start = 0.0


    while Game_running:

        score = Text_button(str(score_p1), SCREEN_WIDTH - 300, 200 , right = True , color=(255 , 120 , 0) ,size=75)

        time = time + (1 / FPS)
        
        if voice_ans :
            user_input = str(voice_control.ANS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
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
                    k = event.unicode
                    print(k)
                    if voice_ans:
                        voice_ans = False
                    if (k == 'f' or k == 't') or (k >= '0' and k <= '9') :
                        user_input = user_input + k.upper()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                angle_cal = math.atan2(y - sk.rect.centery, x - sk.rect.centerx)
                angle_degree = int(angle_cal*180/math.pi)
                a_e = Attack_effect(sk.rect.centerx,sk.rect.centery,20,20,20,x,y)
                attack_effects.add(a_e)
                #a_e = Attack_effect(seeker.rect.centerx,seeker.rect.centery,x,y)
                #a_e = Attack_effect(seeker.rect.centerx, seeker.rect.centery, 20, x,y)
                sk.attack(a_e, angle_degree)            



            seeker.update()
            seeker_label.update()
            attack_effects.update()
        

            ###################################hit enemy function
            hit_done = False
            #if str(em.ans) == user_input :
                #print(time - time_start)
                #data.append([time - time_start])
                #data.train()
                #data.update()
                #print(data.get_m())
                #time_start = time
                #voice_ans = False
                #user_input = ""                                           
            hits_em = pygame.sprite.groupcollide(enemy,attack_effects,False,True)
            for e in hits_em:
                enemy_id = e.id
                answer = e.ans
                if answer == user_input:
                    for a in enemy:
                        if a.id == enemy_id:
                            enemy.remove(a)
                            break
                    for a in enemy_label:
                        if a.id == enemy_id:
                            enemy_label.remove(a)
                            break
                break
            if hits_em:  
                em_count -= 1
                score_p1 += 50                                     
                if em_count <= 0:
                    wave += 1
                    create_enemy(enemy , enemy_label , 5*wave)
                    em_count += 5*wave
            #################Check position seeker
            #print("top =" , seeker.rect.top)
            #print("bottom =" , seeker.rect.bottom)
            #print("left =" , seeker.rect.left)
            #print("right =" , seeker.rect.right)
            #check HP if HP run out,seeker will die
            
            red_bg = False
            if pygame.sprite.groupcollide(seeker,enemy,False,False):
                if not char_hit_status :
                    char_hit_status = True
                    char_hit_count += 1
                    lose_hp(char_hit_count ,hp1 ,hp2 ,hp3)
                    score_p1 -= 100
                    red_bg = True
            else :
                char_hit_status = False
            if char_hit_count >= 3:
                print("Thank for playing")
                Game_running=False
            
            if red_bg :
                screen.fill((255 , 0 , 0))
            else:
                screen.blit(background,background.get_rect(center = (Width/2, Height/2)))
            
            #screen.blit(Score_p1,250,250)
            input_box = Text(user_input , (255 ,0 ,0) , CENTER_X , CENTER_Y + 300 , size=200)
            screen.blit(input_box.surface,input_box.rect)
            seeker.draw(screen)
            seeker_label.draw(screen)
            #hps.draw(screen)
            enemy.draw(screen)
            enemy_label.draw(screen)
            attack_effects.draw(screen)
            score.draw()

            progress.update(time)
            #hps.draw(screen)
            clock.tick(FPS)
            pygame.display.update()
            

    pygame.quit()