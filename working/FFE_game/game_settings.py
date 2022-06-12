import pygame

pygame.init()

clock = pygame.time.Clock()
loc = (0, 0)
vel = 10

face_dir = 0
# left

walkcount = 0
standcount = 0

states = [False, False, False, False]