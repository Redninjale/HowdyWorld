
import pygame
import financetab 


class Pause():
    def __init__(self):
        owo =1
    def displayMenu(self,balance,rent,medicalExpenses,salary,randomEvent,debt):
        keys = pygame.key.get_pressed()
        self.paused = True
        while self.paused():
            for event in pygame.event.get():
                if keys[pygame.K_ESCAPE]:
                    self.paused = False
            else:
                    self.display_surface = pygame.display.get_surface()
                    pygame.display.update
                    clock.tick(15)
                    
                

