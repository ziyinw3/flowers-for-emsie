import pygame

class Button:
    def __init__(self, imgu, imgd, x, y, navi):
        self.imgu = imgu
        self.imgd = imgd
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, 128, 52)
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


    def pressed_navi(self, pg_instance):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pg_instance = self.navi()
            pg_instance.run()
            del pg_instance