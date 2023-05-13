import pygame
import random

from ..constants import *
from ..graphics import drawHuman

class Human:
    def __init__(self, screen, texture, pos_on_map: list[int, int], direction: int):
        self.texture = texture
        self.pos_on_map = pos_on_map
        self.pos_on_screen = pos_on_map # pos_on_screen is only used to draw the characters
        self.direction = direction
        self.screen = screen

        self.velocity = self.direction * (HUMAN_VELOCITY * (random.random() - 0.5))

        drawHuman(self.screen, self.pos_on_map)

    def tick(self):
        self.move()
        drawHuman(self.screen, self.pos_on_map)

    def move(self):
        self.pos_on_map[0] += self.velocity

#class Fan(Human):
#
#class Car(Human):
#
