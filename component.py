import pygame

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

def screen_init() :
    return screen

font = pygame.font.Font('prompt.ttf', 32)

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
    def __init__(self ,text ,color ,x , y) :
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

##Note
##ex . button1 = Button(surface , x , y)
## IF you want to set an img to a button : button1 = pygame.image.load(...), x , y)
## x is position for the center_x of button and y is position for the center_y of button
##ex . button1 = Button(surface,x,y)
## button1.draw()
## if button1.onclick() :
##      do somethings .......

        


        
        
