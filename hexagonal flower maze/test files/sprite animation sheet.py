import pygame
import sys

pygame.init()

size = (640, 480)
white = (225, 225, 225)
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sprite Sheet Tests")

d_names = []
for i in range(1, 7):
    d_names.append("mc_d" + str(i))
    i = i + 1

d_sprites = {}
for name in d_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    d_sprites[name] = pygame.image.load(filename)

dw_names = []
for i in range(1, 9):
    dw_names.append("mc_dw" + str(i))
    i = i + 1

dw_sprites = {}
for name in dw_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    dw_sprites[name] = pygame.image.load(filename)

u_names = []
for i in range(1, 7):
    u_names.append("mc_u" + str(i))
    i = i + 1

u_sprites = {}
for name in u_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    u_sprites[name] = pygame.image.load(filename)    

t_names = []
for i in range(1, 5):
    t_names.append("tail" + str(i))
    i = i + 1

t_sprites = {}
for name in t_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    t_sprites[name] = pygame.image.load(filename)  

print(t_names)


mc_cur = d_sprites.get('mc_d1')
(pos_x, pos_y) = (100, 100)
(pos_x2, pos_y2) = (150, 100)
(pos_x3, pos_y3) = (200, 100)
(pos_x4, pos_y4) = (250, 100)
mc_speed = 10

gameQuit = False

standcount = 1
walkcount = 1
tailcount = 1

while not gameQuit:
    # "FPS, lower faster"
    clock.tick(8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True
            pygame.quit()
            sys.exit()

    standcount += 1
    if standcount == 7:
        standcount = 1
    screen.fill(white)
    screen.blit(d_sprites['mc_d' + str(standcount % 7)], (pos_x, pos_y))
    screen.blit(u_sprites['mc_u' + str(standcount % 7)], (pos_x2, pos_y2))

    walkcount += 1
    if walkcount == 9:
        walkcount = 1
    screen.blit(dw_sprites['mc_dw'+ str(walkcount % 9)], (pos_x3, pos_y3))

    tailcount += 1
    if tailcount == 5:
        tailcount = 1
    screen.blit(t_sprites['tail'+ str(tailcount % 5)], (pos_x4, pos_y4))
    
    pygame.display.flip()
