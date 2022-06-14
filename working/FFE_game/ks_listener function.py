import pygame
pygame.init()

def ks_listener():
    self.states = [False, False, False, False]
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