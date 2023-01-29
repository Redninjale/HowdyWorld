# the function of this is to display items on top of the game itself
import pygame
from settings import *

class Overlay:
    def __init__(self, player):
        #general setup
        overlay_path = './graphics/overlay/'
        self.display_surface = pygame.display.get_surface()
        self.player = player

        happy_path = './graphics/animations/happiness'
        hunger_path = './graphics/animations/hunger'
        self.happiness_surf = {num : pygame.image.load(f'{happy_path}/{num}.png').convert_alpha() for num in player.happiness}
        self.hunger_surf = {num : pygame.image.load(f'{hunger_path}/{num}.png').convert_alpha() for num in player.hunger}


        # happiness_img = pygame.image.load('./graphics/animations/happiness' + self.player.happiness + '.png').convert_alpha()


    def display(self):
        print('test')
        happiness_now = 
        # happiness_rect = happiness_surf.get_rect(topleft = OVERLAY_POSITIONS['happiness'])
        # self.display_surface.blit()