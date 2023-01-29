import pygame, sys
from settings import *
from level import Level
from support import import_folder # this too

class Game:
    def __init__(self):
        pygame.init() #initializes
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #sets screen size
        pygame.display.set_caption('Howdy World!') #the top part of the bar that says whats the name
        self.clock = pygame.time.Clock() #framerate stuff
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get(): #if we ever want to quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() #deinitialize

            dt = self.clock.tick ()/1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
