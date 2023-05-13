import pygame

from ..graphics import drawWorld
from ..constants import *
from ..map import maps

from .entity import *

class World:
    def __init__(self, game, map_num: int):
        self.sprites = []
        self.game = game
        self.map_num = map_num
        self.position = [0, 0] # Map position on the screen, top-left point

        drawWorld(self.game.screen, self.map_num, world_pos = self.position)
        self.WORLD_SIZE = maps[self.map_num][0]
        self.spawn_humans()
    
    def spawn_humans(self):
        self.humans = []
        # Spawns in humans on sidewalks, randomising their positions slightly
        for y_pos, horizontal_stripe in enumerate(maps[self.map_num], -1):
            if y_pos == -1:
                # First line of list is map size (yes its weird)
                pass

            else:    
                for x_pos, vertical_point in enumerate(horizontal_stripe):
                    if vertical_point[0:2] == "sw":
                        if random.random() < 0.5:
                            self.humans.append(Human(self.game.screen, "texture", [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], -1))

    def tick(self):
        drawWorld(self.game.screen, self.map_num, world_pos = self.position)
        self.WORLD_SIZE = maps[self.map_num][0]
        for human in self.humans:
            human.tick()
