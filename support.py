from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load('./graphics/animations/right/2.png')
            surface_list.append(image_surf)

    # print(surface_list)
    return surface_list

animations = {'up': [], 'down': [], 'left': [], 'right': []}

for animation in animations.keys():
    full_path = './graphics/animations/' + animation
    animations[animation] = import_folder(full_path)