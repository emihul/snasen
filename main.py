import pygame
from Structure import shipgroup
from ball import ballgroup
from config import screen
pygame.init()
"""
Obstgroup = pygame.sprite.Group()
for element in range(0,5):
    obstel = Obst()
    Obstgroup.add(obstel)
"""

"""
class main():
    def __init__(self):

    def loop(self):
"""    
while True:
    clock = pygame.time.Clock()
    screen.fill((255,255,255))
    time_passed = clock.tick(30) / 1000.0
    """
    for wall in Walls:
        wall.run((0,0,255))
    """
    i=1
    for element in shipgroup:
        element.run(time_passed,i)
        i+=1
    for balls in ballgroup:
        balls.run(time_passed,shipgroup)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
    pygame.display.update()