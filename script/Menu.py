import pygame
from pygame import Surface, Rect
from pygame.font import Font

from script.Const import SCREEN_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surf = pygame.image.load('./asset/Sample_urban.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Music/menu_music.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, "TEXTOTEXTO", (0, 0, 0), ((SCREEN_WIDTH/2), 100))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        # font menu: https://www.dafont.com/pt/gameplay.font
        text_font: Font = pygame.font.SysFont("Gameplay Regular", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_position)
        self.screen.blit(source=text_surf, dest=text_rect)
