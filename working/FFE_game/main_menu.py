from FFE_game import FFEGame
from options import OptPage
from load import LoadPage

from settings import Settings

import pygame

from spritesheet import mm, buttonu, buttond, cursor, cursor_rect

class Button:
    def __init__(self, imgu, imgd, x, y, navi):
        self.imgu = imgu
        self.imgd = imgd
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, 128, 52)
        self.navi = navi
    def hover(self):
        return self.imgd if self.rect.collidepoint(pygame.mouse.get_pos()) else self.imgu

    def pressed(self, pg_instance):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pg_instance = self.navi()
            pg_instance.run()
            del pg_instance

# initialize some buttons

start_b = Button(buttonu[0], buttond[0], 256, 265, FFEGame)
load_b = Button(buttonu[1], buttond[1], 256, 265 + 60, LoadPage)
opt_b = Button(buttonu[2], buttond[2], 256, 265 + 120, OptPage)

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.mm_count = 0 
        # track menu animation

    def run(self):
        run = True
        self.play_music('OST', 'main_theme')
        while run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                   start_b.pressed('a')
                   load_b.pressed('b')
                   opt_b.pressed('c')

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
        pygame.display.flip()

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

