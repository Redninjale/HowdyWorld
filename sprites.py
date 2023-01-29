import pygame
from settings import*

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf # image is the surface
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(self.rect.width * 0.2, - self.rect.height * 0.75)


#lass Interaction(Generic):
 #   def __init__(self, pos, size, groups, name):
   #     surf = pygame.Surface(size)
     #   super().__init__(pos, surf, groups)
       # self.name = name

#class Example(Generic):
 #   def __init__(self, pos, surf, groups):
  #      super().__init__(pos, surf, groups)
   #     self.hitbox = self.rect.copy().inflate(-20, -self.height * 0.9)