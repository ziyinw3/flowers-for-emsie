# two functions for getting images with rectangular coords

import pygame

class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        self.filename = filename
        self.spritesheet = pygame.image.load(filename)
    def load_strip(self, rects, lis):
        for rect in rects:
            sprite = pygame.Surface((41, 41), pygame.SRCALPHA).convert_alpha()
            sprite.blit(self.spritesheet,(0, 0), rect)
            lis.append(sprite)
