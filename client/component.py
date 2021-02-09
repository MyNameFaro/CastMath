import pygame

pygame.init()

SCREEN_WIDTH = 960*2
SCREEN_HEIGHT = 540*2

CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

padding = 200

def screen_init() :
    return screen

font = pygame.font.SysFont("kanit", 32)

class Object(): 
    def __init__(self ,surface ,x ,y) :
        self.surface = surface
        self.rect = self.surface.get_rect(center = (x , y))
    def draw(self) :
        screen.blit(self.surface , self.rect)
    def get_surface(self) :
        return self.surface

class Player(Object):
    def __init__(self ,img , x , y , text = None) :
        self.surface = pygame.image.load(img)
        super().__init__(self.surface , x , y)

class Text(Object):
    def __init__(self ,text ,color ,x , y ,size=32) :
        font = pygame.font.SysFont("kanit", size)
        self.text = font.render(text, True,color)
        super().__init__(self.text, x , y)

    def update(self ,text ,color ,x , y) :
        self.text = font.render(text, True,color)
        super().__init__(self.text, x , y)

class Paragraph(Object) :
    def __init__(self ,paragraph ,color ,x , y) :
        self.paragraph = paragraph.split('<br>')
        self.color = color
        self.x = x
        self.y = y
        self.surface = None
        self.rect = None
        self.numline = 0
        self.font_size = 50
    def write(self) :
        self.numline = len(self.paragraph)
        self.y -= (self.numline - 1) * self.font_size * 0.5
        for line in self.paragraph :
            self.surface = font.render(line, True, self.color)
            self.rect = self.surface.get_rect(center = (self.x , self.y))
            screen.blit(self.surface , self.rect)
            self.y += self.font_size

class Button() :
    def __init__(self , surface,x ,y):
        self.surface = surface
        self.rect = self.surface.get_rect(center = (x , y)) 
        self.pos = None
        self.click = None
        self.x = x
        self.y = y
    def draw(self) :
        screen.blit(self.surface , self.rect)
    def onclick(self):
        self.pos = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if self.rect.collidepoint(self.pos) :
            self.rect = self.surface.get_rect(center = (self.x , self.y + 10)) 
            for c in self.click :
                if c > 0 :
                    return True
        else :
            self.rect = self.surface.get_rect(center = (self.x , self.y)) 
            return False

class Text_button:
    def __init__(self , text, x , y,size = 32,color = (255 , 255 , 255) , right = False , left = False):
        font = pygame.font.SysFont("kanit", size)
        self.surface = font.render(text, True,color)
        if right:
            self.rect = self.surface.get_rect(midright = (x , y)) 
        elif left:
            self.rect = self.surface.get_rect(midleft = (x , y))
        else :
            self.rect = self.surface.get_rect(center = (x , y)) 
        self.pos = None
        self.click = None
        self.x = x
        self.y = y
    def draw(self) :
        screen.blit(self.surface , self.rect)
    def onclick(self):
        self.pos = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if self.rect.collidepoint(self.pos) :
            self.rect = self.surface.get_rect(center = (self.x , self.y + 10)) 
            for c in self.click :
                if c > 0 :
                    return True
        else :
            self.rect = self.surface.get_rect(center = (self.x , self.y)) 
            return False

class Textbox():
    def __init__(self , surface , name , x , y ,password=False):
        self.value = ""
        self.name = name
        self.active = False
        self.surface = surface
        self.rect = self.surface.get_rect(center = (x , y))
        self.text = font.render(name, True,(36 , 36 ,36))
        self.text_rect = self.text.get_rect(midleft = (x - 190, y))
        self.pos = None
        self.click = None
        self.password = password
    def draw(self):
        if self.value == "" :
            self.text = font.render(self.name, True,(36 , 36 ,36))
        screen.blit(self.surface , self.rect)
        screen.blit(self.text , self.text_rect)
    def get_value(self):
        return self.value
    def get_active(self):
        self.active = not self.active
        if self.active:
            self.surface = pygame.image.load('src/pic/login/textbox_active.png')
        else:
            self.surface = pygame.image.load('src/pic/login/textbox.png')
    def input(self , char):
        if self.value == "":
            self.value = str(char)
        elif char == "BACK":
            self.value = self.value[:-1] 
        else :
            if len(self.value) <= 40:
                self.value = self.value + str(char)
        if self.password:
            self.text = font.render('X' * len(self.value), True,(36 , 36 ,36))
        else:
            self.text = font.render(self.value, True,(36 , 36 ,36))
    def onclick(self):
        self.pos = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if self.rect.collidepoint(self.pos) :
            for c in self.click :
                if c > 0 :
                    return True
        else :
            return False    

class Progress():
    def __init__(self,time_limit , color, x , y):
        self.time_limit = time_limit
        self.time_start = 0.0
        self.color = color
        self.x = x
        self.y = y
        self.running = False
        self.time = 0.0
    def run(self , time_start) :
        self.time_start = float(time_start)
        self.running = True
    def update(self , time):
        if self.running :
            if (time - self.time_start) >= float(self.time_limit):
                self.running = False
            pygame.draw.rect(screen , self.color , pygame.Rect(self.x - 200 , self.y - 30 , 400 , 60),2) #FIGURE
            pygame.draw.rect(screen , self.color , pygame.Rect(self.x - 200 , self.y - 30 , 400 * ((time - self.time_start) / self.time_limit) , 60)) #SCALE
##Note
##ex . button1 = Button(surface , x , y)
## IF you want to set an img to a button : button1 = pygame.image.load(...), x , y)
## x is position for the center_x of button and y is position for the center_y of button
##ex . button1 = Button(surface,x,y)
## button1.draw()
## if button1.onclick() :
##      do somethings .......

        


        
        
