# permanent bits to reference or copy

# game window and prereqs

import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("test with updateWindow class")

clock = pygame.time.Clock()

white = (225, 225, 225)

(x, y) = (100, 100)
vel = 2

left = False
right = False
up = False
down = False

last_pressed = pygame.K_DOWN


# mass upload sprites and put into list

d_names = []
for i in range(1, 13):
    d_names.append("mc_d" + str(i))
    i = i + 1

d_sprites_dic = {}
for name in d_names:
    filename = 'working\sprites\emsie\\' + name + '.png'
    d_sprites_dic[name] = pygame.image.load(filename)

d_vals = d_sprites_dic.values()
d_sprites = list(d_vals)