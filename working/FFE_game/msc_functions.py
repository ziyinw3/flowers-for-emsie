import pygame
pygame.init()

from game_settings import *


# attributes update

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

def walk_counter():
    # find first item in states that is true
    for item in states:
        if item == True:
            face_dir = states.index(item)
            idle = False
    if idle == False:    
        if walkcount < 16:
            walkcount += 1
        elif walkcount == 17:
            walkcount = 1
    if idle == True:
        if standcount < 12:
            standcount += 1
        elif standcount == 13:
            standcount = 1
        walkcount = 0
    face_dir = 3

# update screen

def blit_mc():
    if idle == True:
        self.screen.blit(mc_di[standcount], loc)
    if idle == False:
        self.screen.blit(mc_dw[walkcount], loc)





