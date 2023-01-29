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


    def display(self):
        happiness_visual = self.happiness_surf[self.player.current_happiness]
        happiness_visual = pygame.transform.scale(happiness_visual, (156, 21))
        happiness_rect = happiness_visual.get_rect(topleft = OVERLAY_POSITIONS['happiness'])
        self.display_surface.blit(happiness_visual, happiness_rect)

        hunger_visual = self.hunger_surf[self.player.current_hunger]
        hunger_visual = pygame.transform.scale(hunger_visual, (156, 21))
        hunger_rect = hunger_visual.get_rect(topleft = OVERLAY_POSITIONS['hunger'])
        self.display_surface.blit(hunger_visual, hunger_rect)
       