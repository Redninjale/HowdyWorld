import pygame
from settings import *
from support import*

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, group):

        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        # temp character
        self.image = self.animations[self.status][self.frame_index]
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)

        # direction and position stuff
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

        # change speed below if needed
        self.speed = 200

    def import_assets(self):

        self.animations = {'up': [], 'down': [], 'left': [], 'right': [], 'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': []}

        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)

    def input(self):

        keys = pygame.key.get_pressed()

        # changes self.direction based on button press, 0 as default
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self,dt):

        # normalizes diagonal movement
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # changes pos and center based on x and y instead of completely centered
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)