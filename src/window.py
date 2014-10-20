import sys
import pygame


def init(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    while True:
        screen.fill((0, 0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                sys.exit()



