import pygame

from .constants import *

class Player:
    def __init__(self, pos_on_map: tuple, pos_on_screen: tuple) -> None:
        self.pos_on_map = pos_on_map
        self.pos_on_screen = pos_on_screen

        # Same coordinates as Minecraft: east is positive x and south is positive y
        self.velocity = (0, 0)

    def tick(self) -> None:
        self.move()
    
    def move(self) -> None:
        velocity = MAX_VELOCITY
        self.pos_on_map = self.pos_on_map + velocity

    def input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # Positive x is east
            if self.velocity[0] < MAX_VELOCITY:
                self.velocity[0] +=1
            if self.velocity[0] == MAX_VELOCITY:
                self.velocity[0] = MAX_VELOCITY

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # Negative x is west
            if self.velocity[0] > -MAX_VELOCITY:
                self.velocity[0] -=1
            if self.velocity[0] == -MAX_VELOCITY:
                self.velocity[0] = -MAX_VELOCITY

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            # Negative y is north
            if self.velocity[1] > -MAX_VELOCITY:
                self.velocity[1] -=1
            if self.velocity[1] == -MAX_VELOCITY:
                self.velocity[1] = -MAX_VELOCITY

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # Negative y is west
            if self.velocity[1] > MAX_VELOCITY:
                self.velocity[1] +=1
            if self.velocity[1] == MAX_VELOCITY:
                self.velocity[1] = MAX_VELOCITY
