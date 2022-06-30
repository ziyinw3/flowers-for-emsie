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

        self.state = 'main_menu'
#-----------------------------------------------------
    def play_music(self, typem, name):
        self.type = typem
        self.name = name
        if self.type == 'OST':
            pygame.mixer.music.load('FFE_game\OST\\' + self.name + '.wav')
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
    
    def resume_music(self):
        pygame.mixer.music.unpause()
    
    def stop_music(self):
        pygame.mixer.music.pause()

    def interact_sound(self, sname):
        self.sname = sname
        self.sound = pygame.mixer.Sound('FFE_game\sounds\\' + self.sname + '.wav')
        self.sound.set_volume(0.7)
        pygame.mixer.Sound.play(self.sound)

    def stop_sound(self):
        pygame.mixer.pause()

    def resume_sound(self):
        pygame.mixer.unpause()
        

# global settings
settings = Settings()