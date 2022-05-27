import pygame
from pygame.locals import *


# prelims
pygame.init()
clock = pygame.time.Clock()

key_dict = {K_DOWN:'V', K_UP:'^', K_LEFT:'<', K_RIGHT:'>'}

# character class

class mc():
    def __init__(self):
        (x, y) = (0, 0)
        self.moving = False
        self.m_dir = []
        self.f_dir = ['V']

    def get_m(self):
        if keys[pygame.K_DOWN] or keys[pygame.K_UP] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            self.moving = True

    def get_m_dir(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.m_dir.append('V')
        if keys[pygame.K_UP]:
            self.m_dir.append('^')
        if keys[pygame.K_LEFT]:
            self.m_dir.append('<')
        if keys[pygame.K_RIGHT]:
            self.m_dir.append('>')
    
    def get_f_dir(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.event.KEY_DOWN:
                self.f_dir = []
                if event.key in key_dict:
                    self.f_dir.append(event.key)

run = True
chara = mc()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    chara.get_m()
    print(chara.moving)

    clock.tick(5)


