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

uw_names = []
for i in range(1, 17):
    uw_names.append("mc_uw" + str(i))
    i = i + 1

uw_sprites_dic = {}
for name in uw_names:
    filename = 'working\sprites\emsie\\' + name + '.png'
    uw_sprites_dic[name] = pygame.image.load(filename)

uw_vals = uw_sprites_dic.values()
uw_sprites = list(uw_vals)

r_names = []
for i in range(1, 13):
    r_names.append("mc_r" + str(i))
    i = i + 1

r_sprites_dic = {}
for name in r_names:
    filename = 'working\sprites\emsie\\' + name + '.png'
    r_sprites_dic[name] = pygame.image.load(filename)

r_vals = r_sprites_dic.values()
r_sprites = list(r_vals)   

rw_names = []
for i in range(1, 17):
    rw_names.append("mc_rw" + str(i))
    i = i + 1

rw_sprites_dic = {}
for name in rw_names:
    filename = 'working\sprites\emsie\\' + name + '.png'
    rw_sprites_dic[name] = pygame.image.load(filename)

rw_vals = rw_sprites_dic.values()
rw_sprites = list(rw_vals)

l_names = []
for i in range(1, 13):
    l_names.append("mc_l" + str(i))
    i = i + 1

l_sprites_dic = {}
for name in l_names:
    filename = 'working\sprites\emsie\\' + name + '.png'
    l_sprites_dic[name] = pygame.image.load(filename)

l_vals = l_sprites_dic.values()
l_sprites = list(l_vals)  

lw_names = []
for i in range(1, 17):
    lw_names.append("mc_lw" + str(i))
    i = i + 1

lw_sprites_dic = {}
for name in lw_names:
    filename = 'working\sprites\emsie\\' + name + '.png'
    lw_sprites_dic[name] = pygame.image.load(filename)

lw_vals = lw_sprites_dic.values()
lw_sprites = list(lw_vals)

mc_cur = d_sprites_dic.get('mc_d1')
(pos_x, pos_y) = (100, 100)
(pos_x2, pos_y2) = (150, 100)
(pos_x3, pos_y3) = (200, 100)
(pos_x4, pos_y4) = (100, 150)
(pos_x5, pos_y5) = (150, 150)
(pos_x6, pos_y6) = (250, 100)
(pos_x7, pos_y7) = (200, 150)
(pos_x8, pos_y8) = (250, 150)
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
    screen.blit(r_sprites[standcount // 4], (pos_x3, pos_y3))
    screen.blit(l_sprites[standcount // 4], (pos_x6, pos_y6))

    walkcount += 1
    if walkcount >= 64:
        walkcount = 1
    screen.blit(dw_sprites[walkcount // 4], (pos_x4, pos_y4))
    screen.blit(uw_sprites[walkcount // 4], (pos_x5, pos_y5))
    screen.blit(rw_sprites[walkcount // 4], (pos_x7, pos_y7))
    screen.blit(lw_sprites[walkcount // 4], (pos_x8, pos_y8))
    
    pygame.display.flip()
