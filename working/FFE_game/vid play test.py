import pygame
from pyvidplayer import Video

pygame.init()
win = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

#provide video class with the path to your video
vid = Video("FFE_game\\videos\\sample_vid.mp4")
vid.set_size((1920/2, 1080/2))
pic = pygame.image.load('FFE_game\images\chaoz_cube.gif')

while True:
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #release video resources when done
            vid.close()
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
    
    #your program frame rate does not affect video playback
    #more info below
    clock.tick(60)
    
    if key == "r":
        vid.restart()           #rewind video to beginning
    elif key == "p":
        vid.toggle_pause()      #pause/plays video
    elif key == "right":
        vid.seek(15)            #skip 15 seconds in video
    elif key == "left":
        vid.seek(-15)           #rewind 15 seconds in video
    elif key == "up":
        vid.set_volume(1.0)     #max volume
    elif key == "down":
        vid.set_volume(0.0)     #min volume - mute
        
    #draws the video to the given surface, at the given position
    #info on force draw below
    vid.draw(win, (0, 0), force_draw=False)
    
    pygame.display.update()