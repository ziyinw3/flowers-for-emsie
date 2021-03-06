"""Smooth Movement in pygame"""

#Imports
import pygame, sys

#Constants
WIDTH, HEIGHT = 400, 400
TITLE = "Smooth Movement"

#pygame initialization
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

#Player Class
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.left_indic = (250, 120, 60)
        self.right_indic = (120, 60, 250)
        self.down_indic = (60, 250, 120)
        self.up_indic = (250, 250, 60)
        self.idle_indic = (60, 120, 250)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
    
    def draw(self, win):
        if self.left_pressed == True:
            pygame.draw.rect(win, self.left_indic, self.rect)
        elif self.right_pressed == True:
            pygame.draw.rect(win, self.right_indic, self.rect)
        elif self.down_pressed == True:
            pygame.draw.rect(win, self.down_indic, self.rect)
        elif self.up_pressed == True:
            pygame.draw.rect(win, self.up_indic, self.rect)
        else:
            pygame.draw.rect(win, self.idle_indic, self.rect)
    
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        
        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

#Player Initialization
player = Player(WIDTH/2, HEIGHT/2)

#Main Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left_pressed = True
            if event.key == pygame.K_d:
                player.right_pressed = True
            if event.key == pygame.K_w:
                player.up_pressed = True
            if event.key == pygame.K_s:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left_pressed = False
            if event.key == pygame.K_d:
                player.right_pressed = False
            if event.key == pygame.K_w:
                player.up_pressed = False
            if event.key == pygame.K_s:
                player.down_pressed = False
        
    #Draw
    win.fill((12, 24, 36))  
    player.draw(win)

    #update
    player.update()
    pygame.display.flip()

    clock.tick(30)