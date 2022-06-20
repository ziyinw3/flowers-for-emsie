from FFE_game import FFEGame
from settings import Settings
from Button import Button

import pygame

from spritesheet import cursor, cursor_rect, op, flower_bu, flower_bd

# initialize buttons

music_b = Button(flower_bu[0], flower_bd[0], 372, 160, FFEGame)
sound_b = Button()
twox_b = Button()


class OptPage:
    def __init__(self, screen):
        print('init options')
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.op_count = 0

    def run(self):
        print('running options page')
        run = True
        self.settings = Settings()
        
        # start while loop, check for q

        while run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # if event.type == pygame.MOUSEBUTTONDOWN:
                    # three buttons should access settings

        # blit option screen loop based on step count

        # mouse visible false, blit custom cursor
        # write button hovers, sounds, and store button clicked state and blit clicked image
            if self.settings_sound_on == True:
                music_b.hover_sound()
                sound_b.hover_sound()
                twox_b.hover_sound()
            
            if self.op_count == 1:
                self.op_count = 0
            else:
                self.op_count = 1
            
            self.draw_op()
            self.draw_buttons()
            self.draw_curs()
        pygame.quit()
    
    def draw_op(self):
        self.screen.blit(op[self.op_count // 30], (0, 0))

    def draw_curs(self):
        # blit cursor
        cursor_rect.center = pygame.mouse.get_pos()  # update position 
        self.screen.blit(cursor, cursor_rect)
        pygame.display.update()

    def draw_buttons(self):
        self.screen.blit(music_b.hover(), music_b.pos)
        self.screen.blit(sound_b.hover(), sound_b.pos)
        self.screen.blit(twox_b.hover(), twox_b.pos)

        # write back button that can thread back to previous screen??
        