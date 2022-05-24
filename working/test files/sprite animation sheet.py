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
for i in range(1, 13):
    d_names.append("mc_d" + str(i))
    i = i + 1

d_sprites_dic = {}
for name in d_names:
    filename = 'working\sprites\emsie\\' + name + '.png'
    d_sprites_dic[name] = pygame.image.load(filename)

d_vals = d_sprites_dic.values()
d_sprites = list(d_vals)

dw_names = []
for i in range(1, 17):
    dw_names.append("mc_dw" + str(i))
    i = i + 1

dw_sprites_dic = {}
for name in dw_names:
    filename = 'working\sprites\emsie\\' + name + '.png'
    dw_sprites_dic[name] = pygame.image.load(filename)

dw_vals = dw_sprites_dic.values()
dw_sprites = list(dw_vals)

u_names = []
for i in range(1, 13):
    u_names.append("mc_u" + str(i))
    i = i + 1

u_sprites_dic = {}
for name in u_names:
    filename = 'working\sprites\emsie\\' + name + '.png'
    u_sprites_dic[name] = pygame.image.load(filename)

u_vals = u_sprites_dic.values()
u_sprites = list(u_vals)    


mc_cur = d_sprites_dic.get('mc_d1')
(pos_x, pos_y) = (100, 100)
(pos_x2, pos_y2) = (150, 100)
(pos_x3, pos_y3) = (200, 100)
(pos_x4, pos_y4) = (250, 100)
mc_speed = 10

gameQuit = False

standcount = 1
walkcount = 1

while not gameQuit:
    # "FPS, lower faster"
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True
            pygame.quit()
            sys.exit()

    standcount += 1
    if standcount >= 48:
        standcount = 1
    screen.fill(white)
    screen.blit(d_sprites[standcount // 4], (pos_x, pos_y))
    screen.blit(u_sprites[standcount // 4], (pos_x2, pos_y2))

    walkcount += 1
    if walkcount >= 64:
        walkcount = 1
    screen.blit(dw_sprites[walkcount // 4], (pos_x3, pos_y3))
    
    pygame.display.flip()
