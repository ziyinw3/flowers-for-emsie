# function for loading images from given list of coords

import pygame
import sys

from ss_storages import *

class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        self.filename = filename
        self.spritesheet = pygame.image.load(filename)
    def load_strip(self, rects, lis, dimx, dimy):
        for rect in rects:
            sprite = pygame.Surface((dimx, dimy), pygame.SRCALPHA)
            sprite.blit(self.spritesheet,(0, 0), rect)
            lis.append(sprite)

ss = SpriteSheet('FFE_game\images\mc_ss.png')
menu_ss = SpriteSheet('FFE_game\images\menu_ss.png')
button_ss = SpriteSheet('FFE_game\images\\buttons_ss.png')
options_ss = SpriteSheet('FFE_game\images\\options_ss.png')
flower_b_ss = SpriteSheet('FFE_game\images\\flower_b_ss.png')

# lists of sprites in order based on idle and direction

mc_i3 = []
ss.load_strip(coords_i3, mc_i3, 41, 41)

mc_w3 = []
ss.load_strip(coords_w3, mc_w3, 41, 41)

mc_i2 = []
ss.load_strip(coords_i2, mc_i2, 41, 41)

mc_w2 = []
ss.load_strip(coords_w2, mc_w2, 41, 41)

mc_i1 = []
ss.load_strip(coords_i1, mc_i1, 41, 41)

mc_w1 = []
ss.load_strip(coords_w1, mc_w1, 41, 41)

mc_i0 = []
ss.load_strip(coords_i0, mc_i0, 41, 41)

mc_w0 = []
ss.load_strip(coords_w0, mc_w0, 41, 41)

#-------------------------

mm = []

menu_ss.load_strip(coords_mm, mm, 640, 480)

buttonu = []

button_ss.load_strip(coords_buttonu, buttonu, 128, 52)

buttond = []

button_ss.load_strip(coords_buttond, buttond, 128, 52)



#-------------------------

cursor = pygame.image.load('FFE_game\images\cursor.png')

cursor_rect = cursor.get_rect()
#-------------------------

op = []

options_ss.load_strip(coords_op, op, 640, 480)

flower_bu = []

flower_b_ss.load_strip(coords_flower_bu, flower_bu, 64, 56)

flower_bd = []

flower_b_ss.load_strip(coords_flower_bd, flower_bd, 64, 56)

# pygame.init()

# size = (640, 480)
# white = (225, 225, 225)
# clock = pygame.time.Clock()
# FPS = 60
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Sprite Sheet Tests")

# i = 0

# while True:
#     for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_q:
#                     sys.exit()
#     if i > 11:
#         i = 0
#     screen.fill(white)
#     clock.tick(10)
#     screen.blit(mc_i0[i], (0, 0))
#     i += 1
#     print(i)
#     pygame.display.flip()