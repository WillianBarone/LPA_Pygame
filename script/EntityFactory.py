import random

from script.Background import Background
from script.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from script.Enemy import Enemy
from script.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level01BG':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level01BG{i}', position))
                    list_bg.append(Background(f'Level01BG{i}', (SCREEN_WIDTH, 0)))
                return list_bg

            case 'Player01':
                return Player('Player01', (10, SCREEN_HEIGHT/2 - 30))

            case 'Player02':
                return Player('Player02', (10, SCREEN_HEIGHT/2 + 30))

            case 'Enemy01':
                return Enemy('Enemy01', (SCREEN_WIDTH + 15, random.randint(0 + 40, SCREEN_HEIGHT - 40)))

