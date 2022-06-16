""" main game file"""

import sys, pygame

from settings import Settings

from msc_functions import emsie

pygame.init()
settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption(settings.game_caption)
pygame.display.set_icon(settings.icon)

class FFEGame:
    """Overall class to manage game assets and behavior."""
    # initializer
    def __init__(self):
        """Initialize the game, and create resources."""

    # main game loop
    def run_game(self):
        """Start the main loop for the game."""
        
        while True:
            self._check_events()
            self._update_screen()
            print(emsie.loc)
            settings.clock.tick(30)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    emsie.states[0] = True
                if event.key == pygame.K_RIGHT:
                    emsie.states[1] = True
                if event.key == pygame.K_UP:
                    emsie.states[2] = True
                if event.key == pygame.K_DOWN:
                    emsie.states[3] = True
                if event.key == pygame.K_z:
                    emsie.vel = 10
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    emsie.states[0] = False
                if event.key == pygame.K_RIGHT:
                    emsie.states[1] = False
                if event.key == pygame.K_UP:
                    emsie.states[2] = False
                if event.key == pygame.K_DOWN:
                    emsie.states[3] = False
                if event.key == pygame.K_z:
                    emsie.vel = 4
        
        if True in emsie.states:
            emsie.idle = False
        else:
            emsie.idle = True
        emsie.walk_counter()
        emsie.loc_listener()

    def _update_screen(self):
        screen.fill(settings.bg_color)
        emsie.blit_mc(screen)
        pygame.display.flip()

if __name__ == '__main__':
    FFE_game = FFEGame()
    FFE_game.run_game()