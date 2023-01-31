import pygame
from settings import *
from player import Player
from overlay import Overlay
from sprites import *
from pytmx.util_pygame import load_pygame
import pytmx
from support import *

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        tmx_data = load_pygame('./graphics/mapping/tmx/maptesting.tmx')

        # house
        print(type(tmx_data.get_layer_by_name('bottom')))
        for layer in ['bottom', 'roads_grass']:
           for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
               Generic((x * TILE_SIZE,y * TILE_SIZE), surf, self.all_sprites, LAYERS['bottom'])
        
        for layer in ['background_buildings', 'buildings']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
               Generic((x * TILE_SIZE,y * TILE_SIZE), surf, [self.all_sprites] , LAYERS['building'])

        # Collision tiles
        for x, y, surf in tmx_data.get_layer_by_name('Collision').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), self.collision_sprites)

        # #Player
        for obj in tmx_data.get_layer_by_name('Player'):
            if obj.name == 'Apartment':
                self.player = Player(pos=(obj.x, obj.y), group=self.all_sprites, collision_sprites=self.collision_sprites, interaction=self.interaction_sprites)
                if obj.name == 'Apartment':
                    Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)
        # self.player = Player((640,360), self.all_sprites, self.collision_sprites, self.interaction_sprites)
        
        Generic(
            pos = (0,0),
            surf = pygame.image.load('../HowdyWorld/graphics/Modern_Exteriors_RPG_Maker_MV/Tileset_37_MV.png').convert_alpha(), #I dont know how the fuck this went wrong, but there's 2 images that are moving  needs to be fixed
            groups = self.all_sprites, 
            z = LAYERS['ground'])
        
        # Example((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])


    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.customize_draw(self.player)####
        # self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

        self.overlay.display()
        # self.overlay.text('testing 1234567890', 1)
        # self.overlay.text('2nd line test', 2)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def customize_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)