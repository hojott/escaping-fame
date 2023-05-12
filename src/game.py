import pygame
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

game = Game()