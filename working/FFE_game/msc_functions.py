import pygame
pygame.init()

from game_settings import *

def ks_listener():
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

def loc_listener():
    if states[0] == True:
        loc[0] -= vel
    if states[1] == True:
        loc[0] += vel
    if states[2] == True:
        loc[1] += vel
    if states[3] == True:
        loc[1] -= vel
