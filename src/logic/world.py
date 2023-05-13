import pygame

from ..graphics import drawWorld
from ..constants import *
from ..map import maps

class World:
    def __init__(self, game):
        self.sprites = []
        self.game = game
        self.position = [0, 0] # Map position on the screen, top-left point

        drawWorld(self.game, map_num = 0, world_pos = self.position)
        self.WORLD_SIZE = maps[0][0]

    def tick(self):
        drawWorld(self.game, map_num = 0, world_pos = self.position)
        self.WORLD_SIZE = maps[0][0]
