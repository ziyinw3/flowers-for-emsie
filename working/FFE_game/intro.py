#cutscene player, click to seek next section

import pygame, sys
pygame.init()

from settings import settings
from pyvidplayer import Video

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
main_cutscene = Video("FFE_game\\videos\\sample_vid.mp4")
main_cutscene.set_size((640, 480))

class Intro:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.click_count = 0
        self.seek_time = 5
        self.pos = 60
    
    def run(self):
        run = True

        # listen to settings here

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
                    print(self.pos, self.seek_time)
                    
            
            main_cutscene.draw(screen, (0, 0), force_draw=False)
            self.pos -= 1/60
            
            pygame.display.update()

vid = Intro(screen)

vid.run()
