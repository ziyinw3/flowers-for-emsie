import pygame

screen = pygame.display.set_mode((640, 480))

class Button:
    def __init__(self, imgu, imgd, x, y, navi, dimx, dimy):
        self.imgu = imgu
        self.imgd = imgd
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, dimx, dimy)
        self.navi = navi
    def hover(self):
        return self.imgd if self.rect.collidepoint(pygame.mouse.get_pos()) else self.imgu
        
    def hover_sound(self):
        if self.hover() == self.imgd:
            if not self.played:
                pygame.mixer.Sound('FFE_game\sounds\interact.wav').play()
                self.played = True
        else:
            self.played = False

    # function for buttons that take you to a new screen
    def pressed_navi(self, pg_instance):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pg_instance = self.navi(screen)
            pg_instance.run()
            del pg_instance

    # function for buttons that change settings only
    # def pressed_setting(self):


class ToggleButton():
    def __init__(self, x, y, dimx, dimy, toggler):
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, dimx, dimy)
        self.hover = False
        # self.toggler = toggler

    def button_listener(self):
        print ('pressed!')
    
    # def hover(self):
    #     if self.rect.collidepoint(pygame.mouse.get_pos()):
    #         self.hover = True
    #         print('hi!')
    
    def hover_sound(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False        
        if self.hover == True:
            if not self.played:
                pygame.mixer.Sound('FFE_game\sounds\interact.wav').play()
                self.played = True
        else:
            self.played = False        

    def toggler(self, lis):
        self.lis = lis
        self.last_blit = 0
        self.to_blit = 0
        if self.last_blit == 0 and self.hover == True:
            self.to_blit = 1
        return self.lis[self.to_blit]


    
    