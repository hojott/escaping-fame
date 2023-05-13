import pygame

from ..graphics import drawWorld
from ..constants import *

class World:
    def __init__(self, game):
        self.sprites = []
        self.game = game
        self.position = [0, 0] # Map position on the screen, top-left point

        drawWorld(self.game.screen)

    def tick(self):
        drawWorld(self.game.screen)

