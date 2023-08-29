import pygame

# SCREEN SIZE:
SCREEN_HEIGHT = 324
SCREEN_WIDTH = 576

# ENTITY CONST:

ENTITY_SPEED = {'Level01BG0': 0,
                'Level01BG1': 1,
                'Level01BG2': 1,
                'Player01': 3,
                'Player02': 3,
                'Enemy01': 2
                }
# EVENT:

EVENT_ENEMY = pygame.USEREVENT

# PLAYER CONTROL:

PLAYER_KEY_UP = {'Player01': pygame.K_UP,
                 'Player02': pygame.K_w}

PLAYER_KEY_DOWN = {'Player01': pygame.K_DOWN,
                   'Player02': pygame.K_s}

PLAYER_KEY_LEFT = {'Player01': pygame.K_LEFT,
                   'Player02': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player01': pygame.K_RIGHT,
                    'Player02': pygame.K_d}

# MENU COLOR TEXT:
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (255, 255, 128)

# MENU TEXT :
MENU_OPTION = ('START GAME', 'COOPERATIVE', 'VS MODE', 'QUIT GAME')
