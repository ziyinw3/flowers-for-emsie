# function for loading images from given list of coords

import pygame
import sys

from ss_storages import *

class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        self.filename = filename
        self.spritesheet = pygame.image.load(filename)
    def load_strip(self, rects, lis):
        for rect in rects:
            sprite = pygame.Surface((41, 41), pygame.SRCALPHA)
            sprite.blit(self.spritesheet,(0, 0), rect)
            lis.append(sprite)

ss = SpriteSheet('FFE_game\images\mc_ss.png')

# lists of sprites in order based on idle and direction

mc_i3 = []
ss.load_strip(coords_i3, mc_i3)

mc_w3 = []
ss.load_strip(coords_w3, mc_w3)

mc_i2 = []
ss.load_strip(coords_i2, mc_i2)

mc_w2 = []
ss.load_strip(coords_w2, mc_w2)

mc_i1 = []
ss.load_strip(coords_i1, mc_i1)

mc_w1 = []
ss.load_strip(coords_w1, mc_w1)

mc_i0 = []
ss.load_strip(coords_i0, mc_i0)

mc_w0 = []
ss.load_strip(coords_w0, mc_w0)

#-------------------------

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
#     i += 1
#     if i > 15:
#         i = 0
#     screen.fill(white)
#     clock.tick(10)
#     screen.blit(mc_i3[i], (100, 150))
#     pygame.display.flip()