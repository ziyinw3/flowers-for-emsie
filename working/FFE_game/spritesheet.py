# two functions for getting images with rectangular coords

import pygame


class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""

    def image_at(self, rectangle):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        return image

    def images_at(self, rects):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect) for rect in rects]