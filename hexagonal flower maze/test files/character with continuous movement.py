# MVP: make sprite that has continuous movement across the screen when arrow keys are held down.

from operator import truediv
import pygame
import sys
import math
from pygame.locals import *

pygame.init()


size = (640, 480)
white = (225, 225, 225)
clock = pygame.time.Clock()
FPS = 60

# sprites and dictionaries -------------------------------------------------------------------------------------------------------------------------
d_names = []
for i in range(0, 7):
    d_names.append("mc_d" + str(i))
    i = i + 1
d_sprites = {}



mc_d = pygame.image.load("sprites\emsie\mc_d1.png")


mc_u = pygame.image.load("sprites\emsie\mc sprite up.png")


mc_l = pygame.image.load("sprites\emsie\mc sprite left.png")


mc_r = pygame.image.load("sprites\emsie\mc sprite right.png")


sprite_dim = (41, 41)
mc_cur = mc_d
(pos_x, pos_y) = (100, 100)
mc_speed = 10

gameQuit = False

while not gameQuit:
    # "FPS, lower faster"
    clock.tick(15)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Continuous Movement Test")
    screen.fill(white)
    screen.blit(mc_cur, (pos_x, pos_y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

    # continous walk ----------------------------------------------------------------------------------------------------------------------
    key_state = pygame.key.get_pressed()
        
    if key_state[pygame.K_LEFT]:
        screen.fill(white)
        screen.blit(mc_l, (pos_x, pos_y))
        pos_x = pos_x - mc_speed
        mc_cur = mc_l
        pygame.display.update()

    if key_state[pygame.K_RIGHT]:
        screen.fill(white)
        screen.blit(mc_r, (pos_x, pos_y))
        pos_x = pos_x + mc_speed
        mc_cur = mc_r
        pygame.display.update()

    if key_state[pygame.K_UP]:
        screen.fill(white)
        screen.blit(mc_u, (pos_x, pos_y))
        pos_y = pos_y - mc_speed
        mc_cur = mc_u
        pygame.display.update()

    if key_state[pygame.K_DOWN]:
        screen.fill(white)
        screen.blit(mc_d, (pos_x, pos_y))
        pos_y = pos_y + mc_speed
        mc_cur = mc_d
        pygame.display.update()    


    pygame.display.flip()                
