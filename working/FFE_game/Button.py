import pygame
from settings import settings

screen = pygame.display.set_mode((640, 480))

class Button:
    def __init__(self, imgu, imgd, x, y, navi, dimx, dimy):
        self.imgu = imgu
        self.imgd = imgd
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, dimx, dimy)
        self.navi = navi
        self.played = False
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
    def __init__(self, x, y, dimx, dimy, toggler, state):
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, dimx, dimy)
        self.hover = False
        self.clicked = False
        self.state = state
        self.toggler = toggler
        self.last_blit = state
        self.played = False
    # actual toggler
    def button_listener(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.state == 1:
                settings.interact_sound('interact')
            self.clicked = True
        else: self.clicked = False

        # state toggler
        if self.clicked == True and self.state == 1:
            print(self.toggler + ' turned off!')
            self.state = 0
        elif self.clicked == True and self.state == 0:
            print(self.toggler + ' turned on!')
            self.state = 1

    # new combined method for hover detection and sound playing    
    def hover_sound(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False    
        if self.hover == True:
            if not self.played and settings.sound_on == True:
                settings.interact_sound('interact')  
                self.played = True
        else:
            self.played = False

    def blitter(self, lis):
        self.lis = lis
        if self.state == 0 and self.hover == True:
            self.last_blit = 1
        if self.state == 0 and self.hover == False:
            self.last_blit = 2
        if self.state == 1 and self.hover == True:
            self.last_blit = 3
        if self.state == 1 and self.hover == False:
            self.last_blit = 0
        return self.lis[self.last_blit]

    # exclusive for music_b
    def music_toggle(self):
        if self.state == 0:
            settings.stop_music()
        else:
            settings.resume_music()
    
    def sound_toggle(self):
        if self.state == 0:
            settings.stop_sound()
        else:
            settings.resume_sound()

    # dummy funct for toggling 2x resolution
    