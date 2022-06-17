from FFE_game import FFEGame
from settings import Settings

import pygame

from spritesheet import mm, buttonu, buttond, cursor, cursor_rect

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.mm_count = 0 

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
        cursor_rect.center = pygame.mouse.get_pos()  # update position 
        self.screen.blit(cursor, cursor_rect)
        pygame.display.flip()

class Button:
    def __init__(self, imgu, imgd, pos):
        self.imgu = imgu
        self.imgd = imgd
        self.rect = pygame.img.get_rect()
        self.pos = pos
    def hover(self):
        return True if self.rect.collidepoint(pygame.mouse.get_pos()) else False