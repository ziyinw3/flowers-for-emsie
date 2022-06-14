""" main game file"""

import sys

import pygame

from settings import Settings

# from mc_sprite_set import McSpriteSet

from msc_functions import *


class FFEGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_caption)
        pygame.display.set_icon(self.settings.icon)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            # self._attributes_update()
            self._update_screen()
            print(states, (walkcount, standcount), loc)
            clock.tick(10)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        ks_listener()
        loc_listener()
        walk_counter()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        blit_mc(self.screen)
        pygame.display.flip()
    
    # def _attributes_update(self):
    #     ks_listener()
    #     loc_listener()
    #     walk_counter()


if __name__ == '__main__':
    FFE_game = FFEGame()
    FFE_game.run_game()