import sys

import pygame

from settings import Settings
from mc_ss import mc_sprite, mc_sprite_set


class FFE:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Flowers for Emsie")

        self.mc_ss = mc_sprite_set(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.mc_ss.mc_sprites[0].blitme()
        
        pygame.display.flip()


if __name__ == '__main__':
    chess_game = FFE()
    chess_game.run_game()