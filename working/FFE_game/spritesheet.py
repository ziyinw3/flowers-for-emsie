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

mc_i3 = []
ss.load_strip(coords_i3, mc_i3)

mc_w3 = []
ss.load_strip(coords_w3, mc_w3)