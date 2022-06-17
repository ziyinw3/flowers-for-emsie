from FFE_game import FFEGame
from settings import Settings

import pygame

from spritesheet import mm, buttonu, buttond, cursor, cursor_rect

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.mm_count = 0 
        # track menu animation

    def run(self):
        run = True
        while run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if self.mm_count < 179:
                self.mm_count += 1
            else:
                self.mm_count = 0
            self.draw()

    def draw(self):        
        self.screen.blit(mm[self.mm_count // 30], (0, 0))
        # blit buttons
        start_b = Button(buttonu[0], buttond[0], 256, 265)
        load_b = Button(buttonu[1], buttond[1], 256, 265 + 60)
        opt_b = Button(buttonu[2], buttond[2], 256, 265 + 120)
        self.screen.blit(start_b.hover(), start_b.pos)
        self.screen.blit(load_b.hover(), load_b.pos)
        self.screen.blit(opt_b.hover(), opt_b.pos)
        # blit cursor
        cursor_rect.center = pygame.mouse.get_pos()  # update position 
        self.screen.blit(cursor, cursor_rect)
        pygame.display.flip()

class Button:
    def __init__(self, imgu, imgd, posx, posy):
        self.imgu = imgu
        self.imgd = imgd
        self.pos = (posx, posy)
        self.rect = pygame.Rect(posx, posy, 128, 52)
    def hover(self):
        return self.imgd if self.rect.collidepoint(pygame.mouse.get_pos()) else self.imgu