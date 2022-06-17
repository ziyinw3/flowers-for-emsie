from FFE_game import FFEGame
from settings import Settings

import pygame

start_btn = pygame.image.load()
logo = pygame.image.load()

class MainMenu:
    def __init__(self, screen):
    # self.bg = a set of images for animated menu
    # self.screen = screen
    self.btn = (self.width/2 - start_btn.get_width()/2, 350, start_btn.get_width(), start_btn.get_height())

    def run(self):
        run = True
        while run:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

