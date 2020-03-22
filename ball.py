import pygame
import math
from Structure import Struct
import config
ballgroup = pygame.sprite.Group()
class ball(Struct,pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.x=Struct.x+Struct.radius*math.cos(Struct.direction)
        self.y=Struct.y+Struct.radius*math.sin(Struct.direction)
        self.speedx = Struct.speedx*2*math.cos(Struct.direction)
        self.speedy = Struct.speedy*2*math.sin(Struct.direction)
        self.radius = 2
    def draw(self):
        pygame.draw.circle(screen,(255,255,255),(int(self.x),int(self.y)),int(self.radius))
    def update(self,time_passed,shipgroup):
        self.x += self.speedx
        self.y += self.speedy
        rect1 = pygame.rect(self.x,self.y,self.radius*2,self.radius*2)
        for elem in shipgroup:
            rect2 = elem.image.get_rect()
            if (rect1.colliderect(rect2)):
                pygame.sprite.Sprite.kill(self)
                pygame.sprite.Sprite.kill(elem)
    def run(self,time_passed,shipgroup):
        self.update(time_passed,shipgroup)
        self.draw()
        