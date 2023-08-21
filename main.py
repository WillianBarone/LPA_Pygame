import pygame
from pygame import Surface

pygame.init()

SCREEN_WIDTH = 918
SCREEN_HEIGHT = 515

screen: Surface = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
bg_surface = pygame.image.load('./asset/Sample_platformer.png').convert_alpha()
screen.blit(source=bg_surface, dest=(0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
