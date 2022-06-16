from FFE_game import FFEGame
from settings import Settings

import pygame

start_btn = pygame.image.load(os.path.join("game_assets", "button_play.png")).convert_alpha()
logo = pygame.image.load(os.path.join("game_assets", "logo.png")).convert_alpha()

class MainMenu:
    def __init__(self, screen):
    # self.bg = a set of images for animated menu
    self.screen = screen
    self.btn = (self.width/2 - start_btn.get_width()/2, 350, start_btn.get_width(), start_btn.get_height())
