import pygame

# Use relative imports because running app from main.py
from .constants import *
from .graphics import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen: tuple = pygame.display.set_mode(SCREEN_SIZE)
        self.state: str = "menu"

        self.start_game()


    def start_game(self):
        self.running: bool = True

        clock = pygame.time.Clock()

        while self.running:
            if self.state == "menu":
                drawMenu(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if self.state == "menu":
                        if event.key == pygame.K_q:
                            self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "menu":
                        pos = pygame.mouse.get_pos()

                        if pos[0] > 215 and pos[0] < 785:
                            if pos[1] > 550 and pos[1] < 660:
                                self.load_game()

                            elif pos[1] > 700 and pos[1] < 810:
                                self.running = False

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

    def load_game(self):
        self.state = "game"
        print("load_game")
