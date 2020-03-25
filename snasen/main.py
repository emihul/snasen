import pygame
from Ship import shipgroup
# from ball import ballgroup
import config as cng
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode(cng.SIZE, 0, 32)
pygame.display.set_caption(cng.GAMENAME)
"""
Obstgroup = pygame.sprite.Group()
for element in range(0,5):
    obstel = Obst()
    Obstgroup.add(obstel)
"""


class Main:
    def __init__(self):
        self.screen = screen

    def loop(self):
        while True:
            clock = pygame.time.Clock()
            self.screen.fill((255,255,255))
            time_passed = clock.tick(30) / 1000.0
            """
            for wall in Walls:
                wall.run((0,0,255))
            """
            i=1
            for ships in shipgroup:
                ships.run(time_passed,i)
                i+=1
            # for balls in ballgroup:
            #     balls.run(time_passed,shipgroup)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
            
            pygame.display.update()

if __name__ == "__main__":
    run = Main()
    run.loop()