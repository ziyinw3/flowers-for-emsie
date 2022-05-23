import pygame
import sys

pygame.init()

size = (640, 480)
white = (225, 225, 225)
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Floored Divisor for frames")

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
