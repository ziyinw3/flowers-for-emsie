# function for loading images from given list of coords

import pygame

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