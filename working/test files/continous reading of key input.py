import pygame
import sys

pygame.init()

size = (640, 480)
white = (225, 225, 225)
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Continous Reading test")

gameQuit = False

standcount = 0
walkcount = 0

while not gameQuit:
    # "FPS, lower faster"
    clock.tick(8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True
            pygame.quit()
            sys.exit()

    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_SPACE] == False:
        standcount += 1
        if standcount > 6:
            standcount = 1
    else:
        walkcount += 1
        if walkcount > 2:
            walkcount = 1
    print(standcount, walkcount)
    # standcount increments per tick, aka. response feedback time
    # if key is not pressed, idle will loop. if key is pressed, walking animation will loop.
    