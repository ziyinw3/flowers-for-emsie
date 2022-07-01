from FFE_game import FFEGame
from settings import settings
from Button import ToggleButton

import pygame, sys

from spritesheet import cursor, cursor_rect, op, flower_toggle

# initialize buttons, music and sound on, 2xres off

music_b = ToggleButton(372, 160, 64, 56, 'music_on', 1)
sound_b = ToggleButton(372, 224, 64, 56, 'sound_on', 1)
twox_b = ToggleButton(372, 288, 64, 56, 'twox_res', 0)


class OptPage:
    def __init__(self, screen):
        # print('init options')
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.op_count = 0

    def run(self):
        run = True
        while run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_ESCAPE:
                        # thread back to last screen visited
                        settings.state = 'main_menu2'
                        screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
                        from main_menu import MainMenu
                        mainMenu = MainMenu(screen)
                        mainMenu.run()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # simple on click sound
                    if sound_b.state == 1:
                        settings.interact_sound('on_click')
                    music_b.button_listener()
                    music_b.music_toggle()
                    sound_b.button_listener()
                    sound_b.sound_toggle()
                    twox_b.button_listener()
        # write button hovers, sounds, and store button clicked state and blit clicked image
                music_b.hover_sound()
                sound_b.hover_sound()
                twox_b.hover_sound()
             # blit option screen loop based on step count
            if self.op_count < 59:
                self.op_count += 1
            else:
                self.op_count = 0
            
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
        self.screen.blit(music_b.blitter(flower_toggle), music_b.pos)
        self.screen.blit(sound_b.blitter(flower_toggle), sound_b.pos)
        self.screen.blit(twox_b.blitter(flower_toggle), twox_b.pos)

        # write back button that can thread back to previous screen??
        