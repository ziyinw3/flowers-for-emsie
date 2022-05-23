import pygame
pygame.init()

win = pygame.display.set_mode((640,480))
pygame.display.set_caption("test with updateWindow class")

# sprites bank -----------------------------------------------------------------------------------------------------------

#facing down sprites

d_names = []
for i in range(1, 7):
    d_names.append("mc_d" + str(i))
    i = i + 1

d_sprites = {}
for name in d_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    d_sprites[name] = pygame.image.load(filename)

dw_names = []
for i in range(1, 3):
    dw_names.append("mc_dw" + str(i))
    i = i + 1

dw_sprites = {}
for name in dw_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    dw_sprites[name] = pygame.image.load(filename)

#facing up sprites

u_names = []
for i in range(1, 7):
    u_names.append("mc_u" + str(i))
    i = i + 1

u_sprites = {}
for name in u_names:
    filename = 'hexagonal flower maze\sprites\emsie\\' + name + '.png'
    u_sprites[name] = pygame.image.load(filename)

clock = pygame.time.Clock()

white = (225, 225, 225)

(x, y) = (100, 100)
vel = 10

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

    win.fill(white)

    # loop animation back to 1 when loop is finished      
    # detect if down key is pressed: if so, iterate through walkcount sprites, else, iterate through standcount sprites
    if down:
        walkcount += 1
        if walkcount > 2:
            walkcount = 1
        win.blit(dw_sprites['mc_dw' + str(walkcount % 3)], (x, y))
    else:
        standcount += 1
        if standcount > 6:
            standcount = 1
        win.blit(d_sprites['mc_d' + str(standcount % 7)], (x, y))

    print(walkcount, standcount)

    pygame.display.update()

run = True

while run:
    clock.tick(10)

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