import pygame
import random
import math
import config as cng
from pygame.locals import *

# from ball import ball

screen = pygame.display.set_mode(cng.SIZE, 0, 32)

class Ship(pygame.sprite.Sprite):
    
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.x =int(random.randrange(cng.MIN_SPEED,cng.MAX_SPEED))
        self.y =int(random.randrange(cng.MIN_SPEED,cng.MAX_SPEED))
        self.speedx = 0
        self.speedy = 0
        self.direction = math.pi/2
        self.angle = 0
        self.radius = 4
        self.original = cng.pngfile
        self.nonfireship = cng.pngfile
        self.fireship = cng.pngfile2
        self.image = cng.pngfile
   
    def hitedge(self):
        
        if((self.x +self.width) >= cng.WIDTH):
            return 1
        elif((self.x-self.width)<=0):
            return 1
        elif((self.y+self.heigth)>=cng.HEIGHT):
            return 1
        elif((self.y-self.heigth)<=0):
            return 1

    def update(self,time_passed):

        self.x +=self.speedx*time_passed
        self.y +=self.speedy*time_passed+50*time_passed
        if (self.hitedge==1):
            pygame.sprite.Sprite.kill(self)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.image = pygame.transform.rotate(self.original,self.angle)

    def decrease(self,time_passed):
        if (self.speedy<0):
            self.speedy +=75*time_passed
        self.speedx -= 0.2*self.speedx*time_passed
        self.original = self.nonfireship

    def increase(self,time_passed):
        self.speedx -= 0.2*self.speedx*time_passed
        if(abs(self.speedx) < 150 and abs(self.speedy< 150)):
            self.speedx +=140*time_passed*math.cos(self.direction)
            self.speedy +=140*time_passed*-math.sin(self.direction)
            self.original = self.fireship
        
    def changedirection(self,time_passed,key):
        if(key == "left"):
            self.direction+=2*time_passed
        if(key == "right"):
            self.direction-=2*time_passed
        self.angle = self.direction/(2*math.pi)*360-90
        self.angle = self.angle%360

    def collision(self,ships,obstacles):
        rect1 = self.rect
        rect2 =0
        for elem in ships:
            if self != elem:
                rect2 = elem.rect
        if(rect1.colliderect(rect2)):
            for elem in ships:
                pygame.sprite.Sprite.kill(elem)
                
    def draw(self):
        screen.blit(self.image,self.rect)
    
    # def shoot(self):
    #     ballel = ball()
    #     ballgroup.add(ballel)

    def run(self,time_passed,index):
        pygame.key.get_pressed()
        keys = pygame.key.get_pressed()
        
        if (index==1):
            if keys[pygame.K_LEFT]:
                self.changedirection(time_passed,"left")
            elif keys[pygame.K_RIGHT]:
                self.changedirection(time_passed,"right")
            if keys[pygame.K_UP]:
                self.increase(time_passed)
            else:
                self.decrease(time_passed)
        else:
            if keys[pygame.K_a]:
                self.changedirection(time_passed,"left")
            elif keys[pygame.K_d]:
                self.changedirection(time_passed,"right")
            if keys[pygame.K_w]:
                self.increase(time_passed)
            else:
                self.decrease(time_passed)
        self.update(time_passed)
        self.draw()
        # self.shoot()
    
# ballgroup = pygame.sprite.Group()
Ship1 = Ship()
Ship2 = Ship()
shipgroup = pygame.sprite.Group()
shipgroup.add(Ship1)
shipgroup.add(Ship2)