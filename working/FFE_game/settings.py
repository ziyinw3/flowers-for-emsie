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
#-----------------------------------------------------
    def play_music(self, typem, namem):
        self.type = typem
        self.name = namem
        if self.type == 'OST':
            pygame.mixer.music.load('FFE_game\OST\\' + self.name + '.wav')
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
    
    def stop_music(self):
        pygame.mixer.music.pause()

global settings
settings = Settings()