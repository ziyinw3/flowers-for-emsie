import pygame
from pygame.locals import *


# prelims
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((200,200))
pygame.display.set_caption("test with keydown combo")

key_dict = {K_DOWN:'V', K_UP:'^', K_LEFT:'<', K_RIGHT:'>'}

# character class

class mc:
    def __init__(self, moving, m_dir, f_dir, loc):
        self.moving = False
        self.m_dir = []
        self.f_dir = ['V']
        self.loc = (0, 0) 

    def set_m(self):
        for event in pygame.event.get():
            if event.type == pygame.key.KEYDOWN:
                self.moving = True

    def get_m(self, screen):
        pygame.blit
    

chara = mc(False, [], [], (0, 0))

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    chara.set_m()
    print(chara.moving)

    clock.tick(5)


