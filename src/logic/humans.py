import pygame
import random

from ..constants import *
from ..graphics import drawHuman

class Human:
    def __init__(self, game, texture, pos_on_map: list[int, int], direction: int):
        self.game = game
        self.texture = texture
        self.pos_on_map = pos_on_map
        self.pos_on_screen = pos_on_map # pos_on_screen is only used to draw the characters
        self.direction = direction

        self.velocity = self.direction * (HUMAN_VELOCITY + (random.random() - 0.5))
        self.bounding_box = pygame.draw.rect(self.game.screen, 0, (self.pos_on_screen, HUMAN_SIZE))

        drawHuman(self.game, self.pos_on_map, self.texture)

    def tick(self):
        self.move()
        drawHuman(self.game, self.pos_on_map, self.texture)
        self.check_collide()

    def move(self):
        self.pos_on_map[0] += self.velocity
        self.bounding_box.update((self.pos_on_screen[0]+self.velocity, self.pos_on_screen[1]), HUMAN_SIZE)
    
    def check_collide(self):
        pass
    
    def rect(self):
        return self.bounding_box

class Car(Human):
    def __init__(self, game, texture, pos_on_map: list[int, int]):
        super().__init__(game, texture, pos_on_map, -1)
        self.velocity = self.direction * (CAR_VELOCITY + (random.random() - 0.5))
        self.bounding_box = pygame.draw.rect(self.game.screen, 0, (self.pos_on_screen, CAR_SIZE))
    
    def check_collide(self):
        if self.bounding_box.colliderect(self.game.player.bounding_box):
            self.game.start_battle()

class Fan(Human):
    def __init__(self, game, texture, pos_on_map: list[int, int]):
        super().__init__(game, texture, pos_on_map, -1)
        #TODO: self.view_box = pygame.draw.rect(self.game.screen, 0, (self.pos_on_screen, FAN_SIGHT_SIZE))
    
    def check_collide(self):
        if self.bounding_box.colliderect(self.game.player.bounding_box):
            self.game.start_battle()
