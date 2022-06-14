import pygame, sys
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((200,200))
pygame.display.set_caption("test with keydown combo")

class mc:
    def __init__(self):
        self.moving = False
        self.m_dir = []
        self.f_dir = []
        self.self.loc = (0, 0)
        self.speed = 4
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        self.mc_sprite = pygame.Rect(self.x, self.y, 32, 32)
    
    def draw_mc(self, screen):
        # implement sprite iteration later
        # mc_sprite = # load sprite img
    
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