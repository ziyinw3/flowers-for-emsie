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
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Continuous Movement Test")

# sprites and dictionaries -------------------------------------------------------------------------------------------------------------------------

# down idle set (d1 - d6)
d_names = []
for i in range(1, 7):
    d_names.append("mc_d" + str(i))
    i = i + 1

d_sprites = {}
for name in d_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    d_sprites[name] = pygame.image.load(filename)

# down walking set ()

u_names = []
for i in range(1, 7):
    u_names.append("mc_u" + str(i))
    i = i + 1

u_sprites = {}
for name in u_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    u_sprites[name] = pygame.image.load(filename)


mc_l = pygame.image.load("hexagonal flower maze\sprites\emsie\mc sprite left.png")


mc_r = pygame.image.load("hexagonal flower maze\sprites\emsie\mc sprite right.png")


sprite_dim = (41, 41)
mc_cur = d_sprites.get('mc_d1')
(pos_x, pos_y) = (100, 100)
mc_speed = 10

gameQuit = False

while not gameQuit:
    # "FPS, lower faster"
    clock.tick(15)
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
        screen.blit(u_sprites.get('mc_u1'), (pos_x, pos_y))
        pos_y = pos_y - mc_speed
        mc_cur = u_sprites.get('mc_u1')
        pygame.display.update()

    if key_state[pygame.K_DOWN]:
        screen.fill(white)
        screen.blit(d_sprites.get('mc_d1'), (pos_x, pos_y))
        pos_y = pos_y + mc_speed
        mc_cur = d_sprites.get('mc_d1')
        pygame.display.update()


    pygame.display.flip()                
