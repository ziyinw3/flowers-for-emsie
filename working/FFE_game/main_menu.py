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
        # communicate with settings
        if settings.music_on == True and settings.state == 'main_menu':
            settings.play_music('OST', 'main_theme')
        elif settings.music_on == True and settings.state == 'main_menu2':
            settings.resume_music()
        else:
            settings.music_on = False
            settings.stop_music()
        if settings.sound_on == True:
            settings.stop_sound()
        else:
            settings.resume_sound()
        while run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # simple on click sound
                    if settings.sound_on == True:
                        settings.interact_sound('on_click')
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

