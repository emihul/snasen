import pygame

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
pngfile = pygame.image.load("ship.png")
pngfile2 = pygame.image.load("fireship.png")
pngfile = pygame.transform.scale(pngfile,(30,30))
pngfile2 = pygame.transform.scale(pngfile2,(30,35))
SCREEN_X = 640
SCREEN_Y = 500