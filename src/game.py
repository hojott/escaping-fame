import pygame

# Use relative imports because running app from main.py
from .constants import *
from .graphics import *
from .logic.player import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen: tuple = pygame.display.set_mode(SCREEN_SIZE)

        self.start_game()


    def start_game(self):
        self.running: bool = True
        self.load_menu()

        clock = pygame.time.Clock()

        while self.running:
            keys = pygame.key.get_pressed()
            mouse_buttons = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            if self.state == "menu":
                drawMenu(self.screen)

                if keys[pygame.K_q]:
                    self.running = False

                if mouse_buttons[0]:
                    if mouse_pos[0] > 215 and mouse_pos[0] < 785:
                        if mouse_pos[1] > 550 and mouse_pos[1] < 660:
                            self.load_game()

                        elif mouse_pos[1] > 700 and mouse_pos[1] < 810:
                            self.running = False

            if self.state == "game":
                drawWorld(self.screen)

                if keys[pygame.K_ESCAPE]:
                    self.load_menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

    def load_menu(self):
        self.state = "menu"
        print("load_menu")

    def load_game(self):
        self.state = "game"
        print("load_game")
