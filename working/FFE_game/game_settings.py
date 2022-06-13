import pygame

pygame.init()

clock = pygame.time.Clock()
loc = (0, 0)
vel = 10
idle = True

face_dir = 3
# down

walkcount = 0
standcount = 0

# walking states, left right up down
states = [False, False, False, False]