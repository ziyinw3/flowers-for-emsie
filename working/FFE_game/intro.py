#cutscene player, click to seek next section

import pygame, sys
pygame.init()

from settings import settings
from pyvidplayer import Video

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
main_cutscene = Video("FFE_game\\videos\\timer_vid.mp4")
main_cutscene.set_size((640, 480))

class Intro:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.click_count = 0
        self.elapsed = 0
        self.seek_time = 0
    
    def run(self):
        run = True

        # listen to settings here

        while run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #release video resources when done
                    main_cutscene.close()
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.click_count < 12:
                        self.elapsed = pygame.time.get_ticks() / 1000
                        if self.elapsed > 5:
                            self.seek_time = 5 % self.elapsed
                        else:
                            self.seek_time = (5 - self.elapsed)
                        print(self.elapsed, self.seek_time, self.elapsed + self.seek_time)
                        main_cutscene.seek(self.seek_time)
                    
            
            main_cutscene.draw(screen, (0, 0), force_draw=False)
            
            pygame.display.update()

vid = Intro(screen)

vid.run()
