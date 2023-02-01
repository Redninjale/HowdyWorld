# the function of this is to display items on top of the game itself
import pygame
from settings import *

class Overlay:
    def __init__(self, player):
        # general setup
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

        # money
        money_surf = pygame.image.load('./graphics/animations/messages/blank money.png').convert_alpha()
        money_surf = pygame.transform.scale(money_surf, (280, 80))
        money_rect = money_surf.get_rect(topleft = OVERLAY_POSITIONS['money'])
        self.display_surface.blit(money_surf, money_rect)

        money_text = self.myfont.render(str(self.player.money), True, 'white')
        money_rect = money_text.get_rect(topright = OVERLAY_POSITIONS['money_text'])
        self.display_surface.blit(money_text, money_rect)

        icon_surf = pygame.image.load('./graphics/animations/messages/coin icon.png').convert_alpha()
        icon_surf = pygame.transform.scale(icon_surf, (50, 50))
        self.display_surface.blit(icon_surf, (1040, 27))


        # self.text("test", 1)
        self.text_button("button1", 1)
        # self.text_button("button2", 2)
        # buttons
        # need to know where to pull # of buttons from lol
        buttonspresent = 1 # need to change
        if (buttonspresent >= 1):
            shadow_surf = pygame.image.load('./graphics/animations/messages/button shadow only.png').convert_alpha()
            shadow_surf = pygame.transform.scale(shadow_surf, (1060, 60))
            if (pygame.mouse.get_pos()[0] >= 100 and pygame.mouse.get_pos()[0] <= 1180):
                if (pygame.mouse.get_pos()[1] <= 650 and pygame.mouse.get_pos()[1] >= 580):
                    shadow_rect = shadow_surf.get_rect(topleft = (85, 615))
                    self.display_surface.blit(shadow_surf, shadow_rect)
                    # if (pygame.event.get() and pygame.mouse.get_pressed()):
                    #     print('pressed 1')
                if (buttonspresent == 2):
                    if (pygame.mouse.get_pos()[1] <= 560 and pygame.mouse.get_pos()[1] >= 500):
                        shadow_rect = shadow_surf.get_rect(topleft = (85, 525))
                        self.display_surface.blit(shadow_surf, shadow_rect)
                    # if (pygame.event.get() == pygame.MOUSEBUTTONDOWN):
                    #     print('pressed 2')
                
                    

    def text(self, str, line):
        if (line == 1):
            bg_surf = pygame.image.load('./graphics/animations/messages/big bg.png').convert_alpha()
            bg_surf = pygame.transform.scale(bg_surf, (1140, 300))
            bg_rect = bg_surf.get_rect(topleft = OVERLAY_POSITIONS['msgboard'])
            self.display_surface.blit(bg_surf, bg_rect)
        mytext = self.myfont.render(str, True, 'white')
        self.display_surface.blit(mytext, (120, 370 + 56 * line)) # 56 is (font size + 8)

    def text_button(self, str, num):
        button_surf = pygame.image.load('./graphics/animations/messages/big button.png').convert_alpha()
        button_surf = pygame.transform.scale(button_surf, (1080, 80))
        button_rect = button_surf.get_rect(topleft = (100, 680 - (num * 90)))
        self.display_surface.blit(button_surf, button_rect)
        buttontext = self.myfont.render(str, True, 'white')
        self.display_surface.blit(buttontext, (135, 690 - (num * 90)))
        
       