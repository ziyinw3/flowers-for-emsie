from FFE_game import FFEGame
from settings import Settings

import pygame

from spritesheet import mm, buttonu, buttond, cursor, cursor_rect

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

    def run(self):
        run = True
        while run:
            self.clock.tick(2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            cursor_rect.center = pygame.mouse.get_pos()  # update position 
            self.screen.blit(cursor, cursor_rect)

