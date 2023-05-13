import pygame

from ..graphics import drawWorld
from ..constants import *

class World:
    def __init__(self, game):
        self.sprites = []
        self.game = game
        self.position = [0, 0] # Map position on the screen, top-left point

        # ((drawWorld returns world size))
        self.WORLD_SIZE = drawWorld(self.game.screen, map_num = 0, world_pos = self.position)

    def tick(self):
        self.WORLD_SIZE = drawWorld(self.game.screen, map_num = 0, world_pos = self.position)
