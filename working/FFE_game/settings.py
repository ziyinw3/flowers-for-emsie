import pygame

class Settings:

    def __init__(self):
        self.screen_width, self.screen_height = 640, 480
        self.bg_color = (225, 225, 225)
        self.game_caption = "flowers for emsie"

        self.icon = pygame.image.load('FFE_game\images\icon.png')
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)

        # can change from options menu

        self.music_on = True
        self.sound_on = True
        self.twox_res = False