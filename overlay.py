# the function of this is to display items on top of the game itself
import pygame
from settings import *

class Overlay:
    def __init__(self, player):
        #general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # imports
        self.tools
        self.se