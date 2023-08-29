import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from script.Const import COLOR_YELLOW, MENU_OPTION, EVENT_ENEMY
from script.Entity import Entity
from script.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, menu_option):
        self.screen: Surface = screen
        self.name = name
        self.menu_option = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level01BG'))
        self.entity_list.append(EntityFactory.get_entity('Player01'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player02'))
        pygame.time.set_timer(EVENT_ENEMY, 6000)

    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f'./asset/Music/{self.name}.wav')
        pygame.mixer_music.play(-1)

        while True:
            clock.tick(30)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    # choice = randon.choice(('Enemy01, Enemy02))
                    self.entity_list.append(EntityFactory.get_entity('Enemy01'))

            pygame.display.flip()
        pass
