import pygame
pygame.init()

def ks_listener():
    states = [False, False, False, False]
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                states[0] = True
            if event.key == pygame.K_RIGHT:
                states[1] = True
            if event.key == pygame.K_UP:
                states[2] = True
            if event.key == pygame.K_DOWN:
                states[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                states[0] = False
            if event.key == pygame.K_RIGHT:
                states[1] = False
            if event.key == pygame.K_UP:
                states[2] = False
            if event.key == pygame.K_DOWN:
                states[3] = False