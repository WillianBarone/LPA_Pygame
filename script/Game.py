import pygame

from script.Const import SCREEN_HEIGHT, SCREEN_WIDTH
from script.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.screen)
            menu.run()
            pass
