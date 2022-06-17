import pygame
pygame.init()

from spritesheet import *


# attributes update

class MC:
    def __init__(self):
        self.loc = [100, 150]
        self.states = [False, False, False, False]
        self.vel = 5
        self.face_dir = 3
        self.idle = True
        self.img = mc_i3[0]
        self.walkcount = 0
        self.standcount = 0

    def ks_listener(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.states[0] = True
                if event.key == pygame.K_d:
                    self.states[1] = True
                if event.key == pygame.K_w:
                    self.states[2] = True
                if event.key == pygame.K_s:
                    self.states[3] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.states[0] = False
                if event.key == pygame.K_d:
                    self.states[1] = False
                if event.key == pygame.K_w:
                    self.states[2] = False
                if event.key == pygame.K_s:
                    self.states[3] = False

    def loc_listener(self):
        if self.states[0] == True and self.loc[0] - self.vel > 0:
            self.loc[0] -= self.vel
        if self.states[1] == True and self.loc[0] + self.vel < 599:
            self.loc[0] += self.vel
        if self.states[2] == True and self.loc[1] - self.vel > 0:
            self.loc[1] -= self.vel
        if self.states[3] == True and self.loc[1] + self.vel < 439:
            self.loc[1] += self.vel

    def walk_counter(self):
        # find first item in self.states that is true
        # set idle state
        if self.states == [False, False, False, False]:
            self.idle == True
        elif True in self.states:
            self.idle == False
            self.face_dir = self.states.index(True)

        if self.idle == False:    
            self.walkcount += 1
            self.standcount = 0
        if self.idle == True:
            self.standcount += 1
            self.walkcount = 0
        if self.standcount > 47:
            self.standcount = 0
        if self.walkcount > 63:
            self.walkcount = 0

    # update screen

    def blit_mc(self, scr):
        if self.idle == True:
            if self.face_dir == 3:
                scr.blit(mc_i3[self.standcount // 4], self.loc)
            if self.face_dir == 2:
                scr.blit(mc_i2[self.standcount // 4], self.loc)
            if self.face_dir == 1:
                scr.blit(mc_i1[self.standcount // 4], self.loc)
            if self.face_dir == 0:
                scr.blit(mc_i0[self.standcount // 4], self.loc)    
        if self.idle == False:
            if self.face_dir == 3:
                scr.blit(mc_w3[self.walkcount // 4], self.loc)
            if self.face_dir == 2:
                scr.blit(mc_w2[self.walkcount // 4], self.loc)
            if self.face_dir == 1:
                scr.blit(mc_w1[self.walkcount // 4], self.loc)
            if self.face_dir == 0:
                scr.blit(mc_w0[self.walkcount // 4], self.loc)
            

# instantiate character class
emsie = MC()





