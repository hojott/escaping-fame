import pygame
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen: tuple = pygame.display.set_mode(SCREEN_SIZE)

        self.start_game()
    
    def start_game(self):
        self.running: bool = True'
        
        while self.running:
            continue

game = Game()
