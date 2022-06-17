import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("test with updateWindow class")

# sprites bank -----------------------------------------------------------------------------------------------------------

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


clock = pygame.time.Clock()

white = (225, 225, 225)

(x, y) = (100, 100)
self.vel = 3

left = False
right = False
up = False
down = False

last_pressed = pygame.K_s

events = pygame.event.get()

walkcount = 0
standcount = 0

direction = []

def direction_state():
    global direction
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys_dir = pygame.key.get_pressed()
            direction = []
            if keys_dir[pygame.K_s]:
                direction.append('V')
            if keys_dir[pygame.K_w]:
                direction.append('^')
            if keys_dir[pygame.K_a]:
                direction.append('<')
            if keys_dir[pygame.K_d]:
                direction.append('>')
    print(direction)  

def updateFrame():
    global walkcount
    global standcount

    screen.fill(white)

    # loop animation back to frame 1 when loop is finished      
    # detect if down key is pressed: if so, iterate through walkcount sprites, else, iterate through standcount sprites
    if down:
        walkcount += 1
        if walkcount >= 64:
            walkcount = 1
        screen.blit(dw_sprites[walkcount // 4], (x, y))
    elif up:
        walkcount += 1
        if walkcount >= 64:
            walkcount = 1
        screen.blit(uw_sprites[walkcount // 4], (x, y))
    elif right:
        walkcount += 1
        if walkcount >= 64:
            walkcount = 1
        screen.blit(rw_sprites[walkcount // 4], (x, y))   
    elif left:
        walkcount += 1
        if walkcount >= 64:
            walkcount = 1
        screen.blit(lw_sprites[walkcount // 4], (x, y))   

    # loop to update idles based on last key pressed

    else:
        standcount += 1
        if standcount >= 48:
            standcount = 1
        screen.fill(white)
        if last_pressed == pygame.K_w:
            screen.blit(u_sprites[standcount // 4], (x, y))
        elif last_pressed == pygame.K_a:
            screen.blit(l_sprites[standcount // 4], (x, y))
        elif last_pressed == pygame.K_d:
            screen.blit(r_sprites[standcount // 4], (x, y))
        else:
            last_pressed == pygame.K_s
            screen.blit(d_sprites[standcount // 4], (x, y))

    # print(walkcount, standcount)

    pygame.display.update()

run = True

while run:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        last_pressed = pygame.K_s
        y += self.vel
        down = True
        standcount = 0

    if keys[pygame.K_w]:
        last_pressed = pygame.K_w
        y -= self.vel
        up = True
        standcount = 0

    if keys[pygame.K_a]:
        last_pressed = pygame.K_a
        x -= self.vel
        left = True
        standcount = 0

    if keys[pygame.K_d]:
        last_pressed = pygame.K_d
        x += self.vel
        right = True
        standcount = 0            

    else:
        down = False
        up = False
        left = False
        right = False
        walkcount = 0
    
    updateFrame()
    direction_state()

# pygame.quit()