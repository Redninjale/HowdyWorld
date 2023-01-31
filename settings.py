from pygame.math import Vector2

SCREEN_WIDTH = 1280 #1280 720
SCREEN_HEIGHT = 720
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 75
TILE_SIZE = 32

# OVERLAY POSITIONS
OVERLAY_POSITIONS = {
    'happiness' : (15, 15),
    'hunger' : (15, 50),
    'msgboard' : (70, 400),
    'money' : (1000, 15),
    'money_text' : (1240, 30)
    }

LAYERS = {'ground': 0, 'bottom': 1, 'building': 2, 'main': 3, 'building top': 4}