#cutscene player

import pygame, sys
pygame.init()

from settings import settings
from pyvidplayer import Video

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
main_cutscene = Video("FFE_game\\videos\cutscene.mp4")
main_cutscene.set_size((640, 480))


global time_count

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #release video resources when done
            main_cutscene.close()
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
    
    main_cutscene.draw(screen, (0, 0), force_draw=False)
    settings.clock.tick(60)
    
    pygame.display.update()
