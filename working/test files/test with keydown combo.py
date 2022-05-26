# testing a combo of continuous reading and KEY_DOWN event

import pygame
pygame.init()

screen = pygame.display.set_mode((200,200))
pygame.display.set_caption("test with keydown combo")

clock = pygame.time.Clock()

last_pressed = pygame.K_DOWN
key_list = []
keys_pressed = []

events = pygame.event.get()

def direction():
    global last_pressed
    global key_list

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("down is pressed")
            if event.key == pygame.K_UP:
                key_list.append("^")
                print("up is pressed")


direction = []
direction.append('V')

def direction_state():
    global direction
    for event in events:
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            direction = []
            if keys[pygame.K_DOWN]:
                direction.append('V')
            if keys[pygame.K_UP]:
                direction.append('^')
            if keys[pygame.K_LEFT]:
                direction.append('<')
            if keys[pygame.K_RIGHT]:
                direction.append('>')
    print(direction)      

run = True

while run:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # if event.type == pygame.KEYDOWN:
        #     keys = pygame.key.get_pressed()
        #     direction = []
        #     if keys[pygame.K_DOWN]:
        #         direction.append('V')
        #     if keys[pygame.K_UP]:
        #         direction.append('^')
        #     if keys[pygame.K_LEFT]:
        #         direction.append('<')
        #     if keys[pygame.K_RIGHT]:
        #         direction.append('>')
    direction_state()
    