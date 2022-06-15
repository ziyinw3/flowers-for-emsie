""" main game file"""

import sys

import pygame

from settings import Settings

from msc_functions import MC, emsie

from game_settings import *


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
            self._update_screen()

            # testing
            print(emsie.walkcount, emsie.standcount, emsie.face_dir)
            clock.tick(5)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        emsie.ks_listener()
        emsie.walk_counter()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        emsie.blit_mc(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    FFE_game = FFEGame()
    FFE_game.run_game()