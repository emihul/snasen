import pygame
import math
from Ship import Ship
import config as cng

# ballgroup = pygame.sprite.Group()

screen = pygame.display.set_mode(cng.SIZE, 0, 32)

class ball(Ship, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.x = Ship.x + Ship.radius * math.cos(Ship.direction)
        self.y = Ship.y + Ship.radius * math.sin(Ship.direction)
        self.speedx = Ship.speedx * 2 * math.cos(Ship.direction)
        self.speedy = Ship.speedy * 2 * math.sin(Ship.direction)
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
        