import pygame
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen: tuple = pygame.display.set_mode(SCREEN_SIZE)

        self.running: bool = True
        self.tick()
    
    def tick(self):
        while self.running:
            continue

game = Game()
