from FFE_game import FFEGame
from options import OptPage
from load import LoadPage
from Button import Button
from settings import settings

# from run import settings

import pygame, sys

from spritesheet import mm, buttonu, buttond, cursor, cursor_rect

# initialize some buttons

start_b = Button(buttonu[0], buttond[0], 256, 265, FFEGame, 128, 52)
load_b = Button(buttonu[1], buttond[1], 256, 265 + 60, LoadPage, 128, 52)
opt_b = Button(buttonu[2], buttond[2], 256, 265 + 120, OptPage, 128, 52)

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.mm_count = 0 
        # track menu animation

    def run(self):
        run = True
        # self.settings = Settings()
        if settings.music_on == True:
            self.play_music('OST', 'main_theme')
        else:
            self.stop_music()
        while run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if settings.sound_on == True:
                        pygame.mixer.Sound('FFE_game\sounds\on_click.wav').set_volume(0.2)
                        pygame.mixer.Sound('FFE_game\sounds\on_click.wav').play()
                    # instances are dummy names
                    start_b.pressed_navi('a')
                    load_b.pressed_navi('b')
                    opt_b.pressed_navi('c')
            if settings.sound_on == True:
                start_b.hover_sound()
                load_b.hover_sound()
                opt_b.hover_sound()

            if self.mm_count < 179:
                self.mm_count += 1
            else:
                self.mm_count = 0

            self.draw_mm()
            self.draw_buttons()
            self.draw_curs()
        pygame.quit()

    def draw_mm(self):        
        self.screen.blit(mm[self.mm_count // 30], (0, 0))

    def draw_curs(self):
        # blit cursor
        cursor_rect.center = pygame.mouse.get_pos()  # update position 
        self.screen.blit(cursor, cursor_rect)
        pygame.display.update()

    def draw_buttons(self):
        # blit buttons
        self.screen.blit(start_b.hover(), start_b.pos)
        self.screen.blit(load_b.hover(), load_b.pos)
        self.screen.blit(opt_b.hover(), opt_b.pos)

    #------------------------------------------------------------- 

    def play_music(self, typem, namem):
        self.type = typem
        self.name = namem
        if self.type == 'OST':
            pygame.mixer.music.load('FFE_game\OST\\' + self.name + '.wav')
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
    
    def stop_music(self):
        pygame.mixer.music.stop()

