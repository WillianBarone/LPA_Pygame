import pygame.key

from script.Const import SCREEN_HEIGHT, ENTITY_SPEED, SCREEN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_LEFT
from script.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[f'{self.name}']

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[f'{self.name}']

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[f'{self.name}']

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < SCREEN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[f'{self.name}']
