import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from script.Const import SCREEN_WIDTH, MENU_OPTION, COLOR_BLACK, COLOR_YELLOW


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surf = pygame.image.load('./asset/Sample_urban.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Music/MA_Gvidon_Roadkill_Menu_.wav')
        pygame.mixer_music.play(-1)

        menu_option = 0

        while True:
            # Draw surface:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, 'SPACE COLLISION', COLOR_BLACK, ((SCREEN_WIDTH / 2), 80))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((SCREEN_WIDTH / 2), 180 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_BLACK, ((SCREEN_WIDTH / 2), 180 + 25 * i))

            pygame.display.flip()

            # Check events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        # font menu: https://www.dafont.com/pt/germinabunt.font
        text_font: Font = pygame.font.SysFont('Germinabunt Regular', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_position)
        self.screen.blit(source=text_surf, dest=text_rect)
