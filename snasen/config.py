import pygame

SIZE = (WIDTH, HEIGHT) = (640, 500)
GAMENAME = 'Mayhem'
MIN_SPEED = 50
MAX_SPEED = 250


pngfile = pygame.image.load("ship.png")
pngfile2 = pygame.image.load("fireship.png")
pngfile = pygame.transform.scale(pngfile,(30,30))
pngfile2 = pygame.transform.scale(pngfile2,(30,35))
