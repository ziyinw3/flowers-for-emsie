import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("test with updateWindow class")

# sprites bank -----------------------------------------------------------------------------------------------------------

#facing down sprites

d_names = []
for i in range(1, 13):
    d_names.append("mc_d" + str(i))
    i = i + 1

d_sprites_dic = {}
for name in d_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    d_sprites_dic[name] = pygame.image.load(filename)

d_vals = d_sprites_dic.values()
d_sprites = list(d_vals)

dw_names = []
for i in range(1, 9):
    dw_names.append("mc_dw" + str(i))
    i = i + 1

dw_sprites_dic = {}
for name in dw_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    dw_sprites_dic[name] = pygame.image.load(filename)

dw_vals = dw_sprites_dic.values()
dw_sprites = list(dw_vals)

u_names = []
for i in range(1, 13):
    u_names.append("mc_u" + str(i))
    i = i + 1

u_sprites_dic = {}
for name in u_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    u_sprites_dic[name] = pygame.image.load(filename)

u_vals = u_sprites_dic.values()
u_sprites = list(u_vals)    

clock = pygame.time.Clock()

white = (225, 225, 225)

(x, y) = (100, 100)
vel = 3

left = False
right = False
up = False
down = False

last_pressed = pygame.K_DOWN

walkcount = 0
standcount = 0

def updateFrame():
    global walkcount
    global standcount

    screen.fill(white)

    # loop animation back to 1 when loop is finished      
    # detect if down key is pressed: if so, iterate through walkcount sprites, else, iterate through standcount sprites
    if down:
        walkcount += 1
        if walkcount + 1 == 33:
            walkcount = 1
        screen.blit(dw_sprites[walkcount // 4], (x, y))
    else:
        standcount += 1
        if standcount + 1 == 49:
            standcount = 1
        screen.fill(white)
        screen.blit(d_sprites[standcount // 4], (x, y))

    print(walkcount, standcount)

    pygame.display.update()

run = True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        y += vel
        down = True
        standcount = 0
    else:
        down = False
        walkcount = 0
    
    updateFrame()

# pygame.quit()