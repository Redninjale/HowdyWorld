import pygame
from settings import *
from support import import_folder # not here before
from pause import Pause


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, group, collision_sprites):

        super().__init__(group)

        self.import_assets()
        self.status = 'up'#self.status = 'down_idle'
        self.frame_index = 0

        # temp character
        # self.image = pygame.Surface((32,64))
        self.image = self.animations[self.status][self.frame_index]
        
        self.rect = self.image.get_rect(center = pos)
        #Collisions
        

        # direction and position stuff
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

        # change speed below if needed
        self.speed = 200
        self.hitbox = self.rect.copy().inflate((-126,-70))
        self.collision_sprites = collision_sprites

        # happiness bar
        self.happiness = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.happiness_index = 10
        self.current_happiness = self.happiness[self.happiness_index]

        # hunger bar
        self.hunger = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.hunger_index = 10
        self.current_hunger = self.hunger[self.hunger_index]

    def happiness_change(self, amount):
        self.happiness_index += amount
        if (self.happiness_index <= 0):
            print('sad :( dead')
        elif (self.happiness_index > 10):
            self.happiness = 10      
        else:
            self.current_happiness = self.happiness[self.happiness_index]      

    def hunger_change(self, amount):
        self.hunger_index += amount
        if (self.hunger_index <= 0):
            print('hungry :( dead')
        if (self.hunger_index > 10):
            self.current_hunger = self.hunger[self.hunger_index]

    def import_assets(self):

        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}

        for animation in self.animations.keys():
            full_path = './graphics/animations/' + animation
            self.animations[animation] = import_folder(full_path)
        # print(self.animations)

    def animate(self, dt):
        self.frame_index += 6 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):

        keys = pygame.key.get_pressed()

        # changes self.direction based on button press, 0 as default
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
        

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0
        
        if keys[pygame.K_ESCAPE]:
            self.pause = Pause()
            self.pause.displayMenu()
    
    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0: #moving right
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0: #moving left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                    if direction == 'vertical':
                        if self.direction.y > 0: #moving down
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0: #moving up
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery 


    def move(self,dt):

        # normalizes diagonal movement
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # changes pos and center based on x and y instead of completely centered
        self.pos.x += self.direction.x * self.speed * dt
        
        self.hitbox.centerx = round(self.pos.x)
        # self.rect.centerx = self.pos.x
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = self.pos.y
        # self.rect.centery = self.pos.y
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)