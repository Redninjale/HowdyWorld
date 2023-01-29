# the function of this is to display items on top of the game itself
import pygame
from settings import *

class Overlay:
    def __init__(self, player):
        # general setup
        # overlay_path = './graphics/overlay/'
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # bar stuff
        bar_path = './graphics/animations/'
        self.happiness_surf = {num : pygame.image.load(f'{bar_path}/happiness/{num}.png').convert_alpha() for num in player.happiness}
        self.hunger_surf = {num : pygame.image.load(f'{bar_path}/hunger/{num}.png').convert_alpha() for num in player.hunger}

        # font stuff
        self.myfont = pygame.font.Font('./graphics/font/pixel font-7.ttf', 48)


    def display(self):
        # happiness bar
        happiness_visual = self.happiness_surf[self.player.current_happiness]
        happiness_visual = pygame.transform.scale(happiness_visual, (350, 21))
        happiness_rect = happiness_visual.get_rect(topleft = OVERLAY_POSITIONS['happiness'])
        self.display_surface.blit(happiness_visual, happiness_rect)

        # hunger bar
        hunger_visual = self.hunger_surf[self.player.current_hunger]
        hunger_visual = pygame.transform.scale(hunger_visual, (350, 21))
        hunger_rect = hunger_visual.get_rect(topleft = OVERLAY_POSITIONS['hunger'])
        self.display_surface.blit(hunger_visual, hunger_rect)

        # buttons
        # need to know where to pull # of buttons from lol
        buttonspresent = 0
        pressed = False
        if (buttonspresent >= 1):
            shadow_surf = pygame.image.load('./graphics/animations/messages/button shadow only.png').convert_alpha()
            shadow_surf = pygame.transform.scale(shadow_surf, (1080, 60))
            while (not pressed):
                if (pygame.mouse.get_pos[0] >= 100 and pygame.mouse.get_pos[0] <= 1180):
                    ypos1 = 680 - 1 * 70
                    ypos2 = ypos1 - 70
                    if (pygame.mouse.get_pos[1] <= 680 and pygame.mouse.get_pos[1] >= 620):
                        shadow_rect = shadow_surf.get_rect(topleft = (99, 680))
                        if (pygame.mouse.get_pressed):
                            self.display_surface.blit(shadow_surf, shadow_rect)
                            pressed = True
                    if (pygame.mouse.get_pos[1] <= 610 and pygame.mouse.get_pos[1] >= 550):
                        shadow_rect = shadow_surf.get_rect(topleft = (99, 610))
                        if (pygame.mouse.get_pressed):
                            self.display_surface.blit(shadow_surf, shadow_rect)
                            pressed = True
                    if (pygame.mouse.get_pos[1] <= 540 and pygame.mouse.get_pos[1] >= 480):
                        shadow_rect = shadow_surf.get_rect(topleft = (99, 610))
                        if (pygame.mouse.get_pressed):
                            self.display_surface.blit(shadow_surf, shadow_rect)
                            pressed = True
                    





    def text(self, str, line):
        if (line == 1):
            bg_surf = pygame.image.load('./graphics/animations/messages/big bg.png').convert_alpha()
            bg_surf = pygame.transform.scale(bg_surf, (1140, 300))
            bg_rect = bg_surf.get_rect(topleft = OVERLAY_POSITIONS['msgboard'])
            self.display_surface.blit(bg_surf, bg_rect)
        mytext = self.myfont.render(str, True, 'white')
        self.display_surface.blit(mytext, (120, 370 + 56 * line)) # 56 is font size + 8 for line breaks

    def text_button(self, str, num):
        button_surf = pygame.image.load('./graphics/animations/messages/bit button.png').convert_alpha()
        button_surf = pygame.transform.scale(button_surf, (1080, 60))
        button_rect = button_surf.get_rect(topleft = (100, 680 - (num * 70)))
        self.display_surface.blit(button_surf, button_rect)
        buttontext = self.myfont.render(str, True, 'white')
        self.display_surface.blit(buttontext, (120, 700 - (num * 70)))
        
       