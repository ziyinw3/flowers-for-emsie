import pygame
pygame.init()

from game_settings import *

# from mc_sprite_set import *

from spritesheet import *


# attributes update

class MC:
    def __init__(self):
        self.loc = (100, 150)
        self.states = [False, False, False, False]
        self.vel = 10
        self.face_dir = 3
        self.idle = True
        self.img = mc_i3[0]
        self.walkcount = 0
        self.standcount = 0

    def ks_listener(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.states[0] = True
                if event.key == pygame.K_RIGHT:
                    self.states[1] = True
                if event.key == pygame.K_UP:
                    self.states[2] = True
                if event.key == pygame.K_DOWN:
                    self.states[3] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.states[0] = False
                if event.key == pygame.K_RIGHT:
                    self.states[1] = False
                if event.key == pygame.K_UP:
                    self.states[2] = False
                if event.key == pygame.K_DOWN:
                    self.states[3] = False

    def loc_listener(self):
        if self.states[0] == True:
            self.loc[0] -= self.vel
        if self.states[1] == True:
            self.loc[0] += self.vel
        if self.states[2] == True:
            self.loc[1] += self.vel
        if self.states[3] == True:
            self.loc[1] -= self.vel

    def walk_counter(self):
        # find first item in self.states that is true
        for item in self.states:
            if item == True:
                self.face_dir = self.states.index(item)
                self.idle = False
        if self.idle == False:    
            self.walkcount += 1
            self.standcount = 0
        if self.idle == True:
            self.standcount += 1
            self.walkcount = 0
        if self.standcount > 11:
            self.standcount = 0
        if self.walkcount > 15:
            self.standcount = 0
        self.face_dir = 3

    # update screen

    def blit_mc(self, scr):
        if idle == True:
            scr.blit(mc_i3[self.standcount], self.loc)
        if idle == False:
            scr.blit(mc_w3[self.walkcount], self.loc)


emsie = MC()





