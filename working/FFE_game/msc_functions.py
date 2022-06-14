import pygame
pygame.init()

from game_settings import *

# from mc_sprite_set import *

from spritesheet import *


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
    global idle
    global standcount
    global walkcount
    for item in states:
        if item == True:
            face_dir = states.index(item)
            idle = False
    if idle == False:    
        walkcount += 1
        standcount = 0
    if idle == True:
        standcount += 1
        walkcount = 0
    face_dir = 3

# update screen

def blit_mc(scr):
    if idle == True:
        scr.blit(mc_i3[standcount % 12], loc)
    if idle == False:
        scr.blit(mc_w3[walkcount % 16], loc)





