import pygame

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    from main_menu import MainMenu
    mainMenu = MainMenu(screen)
    mainMenu.run()