import pygame
from settings import *
from player import Player
from overlay import Overlay
from sprites import Generic
# from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()
        # self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        #Collision tiles
        # for x, y, surf in tmx_data.get_layer_by_name('Collision').tiles():
        #     Generic((x * TILE_SIZE, y * TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), self.collision_sprites)
        
        #Player
        # for obj in tmx_data.get_layer_by_name('Player'):
        #     if obj.name == 'Start':
        #         self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
        self.player = Player((640,360), self.all_sprites, self.collision_sprites)
        
        # Generic(
        #     pos = (0,0),
        #     surf = pygame.image.load('../graphics/world/ground.png').convert_alpha(),
        #     groups = self.all_sprites)
        
        # Example((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])


    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

class CameraGroup(pygame.sprite.Group):
     def __init__(self):
         super().__init__()
         self.display_surface = pygame.display.get_surface()

     def customize_draw(self):
         for sprite in self.sprites():
             self.display_surface.blit(sprite.image, sprite.rect)