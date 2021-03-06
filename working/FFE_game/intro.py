#cutscene player, click to seek next section

import pygame, sys
pygame.init()

from FFE_game import FFEGame
from settings import settings
from pyvidplayer import Video
from spritesheet import cursor, cursor_rect, load_screen

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption(settings.game_caption)
pygame.display.set_icon(settings.icon)

main_cutscene = Video("FFE_game\\videos\\sample_vid.mp4")
main_cutscene.set_size((640, 480))

class Intro:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.click_count = 0
        self.seek_time = 5
        self.pos = 29
    
    def run(self):
        run = True

        while run:
            #fps for detecting input
            self.clock.tick(60)
                # increment timer by 1 sec
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #release video resources when done
                    main_cutscene.close()
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pos - self.seek_time > 0:
                        self.seek_time = (5 - self.pos % 5)
                        self.pos -= self.seek_time                        
                        main_cutscene.seek(self.seek_time)
                    
            # self.draw_curs()
            main_cutscene.draw(screen, (0, 0), force_draw=False)
            self.pos -= 1/60

            if self.pos - 1/60 > 0:
                # self.draw_curs()
                pygame.display.update()
            else:
                self.screen.blit(load_screen, (0, 0))
                pygame.display.update()
                pg_instance = FFEGame(screen)
                pg_instance.run()
                del pg_instance      

    def draw_curs(self):
        # blit cursor
        cursor_rect.center = pygame.mouse.get_pos()  # update position 
        self.screen.blit(cursor, cursor_rect)
        pygame.display.update()    

# vid = Intro(screen)
# vid.run()