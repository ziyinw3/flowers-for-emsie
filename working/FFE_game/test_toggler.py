# test toggler

import pygame, sys
pygame.init()

from Button import Button

from main_menu import MainMenu

from spritesheet import flower_bu, flower_bd

screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

button = Button(flower_bu[0], flower_bd[0], 50, 100, MainMenu, 50, 50)

rect = pygame.Rect(50, 100, 50, 50)

while True:
    # clock.tick(60)
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
    screen.blit(flower_bu[0], (100, 200))
    screen.blit(flower_bu[1], (100 + 100, 200))
    screen.blit(flower_bd[0], (100 + 100 + 100, 200))
    screen.blit(flower_bd[1], (100 + 100 + 100 + 100, 200))
    # if rect.collidepoint(pygame.mouse.get_pos()):
    #     screen.blit(flower_bu[0], (100, 200))
    
    pygame.display.update()
    






