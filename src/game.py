import pygame
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen: tuple = pygame.display.set_mode(SCREEN_SIZE)
        self.state = "menu"

        self.start_game()
    
    def start_game(self):
        self.running: bool = True

        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if self.state == "menu":
                        if event.key == pygame.K_q:
                            self.running = False

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()


game = Game()
