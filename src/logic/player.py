import pygame

from ..constants import *
from ..graphics import drawPlayer

class Player:
    def __init__(self, screen: tuple, pos_on_map: list, pos_on_screen: list) -> None:
        self.pos_on_map = pos_on_map
        self.pos_on_screen = pos_on_screen

        self.stress: int = 5
        self.time: float = 0.0

        self.screen = screen

        # Same coordinates as Minecraft: east is positive x and south is positive y
        self.velocity = [0, 0]
        drawPlayer(self.screen, self.pos_on_screen)

    def endTurn(self, stress: int):
        self.time += 0.5 + stress * 0.3
        self.stress += stress

    def tick(self) -> None:
        self.input()
        self.inputnt()
        self.move()
        drawPlayer(self.screen, self.pos_on_screen)
    
    def move(self) -> None:
        self.pos_on_screen[0] += self.velocity[0]
        self.pos_on_screen[1] += self.velocity[1]

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

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # Positive y is west
            if self.velocity[1] < MAX_VELOCITY:
                self.velocity[1] +=1
            if self.velocity[1] == MAX_VELOCITY:
                self.velocity[1] = MAX_VELOCITY

    def inputnt(self):
        keys = pygame.key.get_pressed()

        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and self.velocity[0] != 0:
            if self.velocity[0] < 0.4 and self.velocity[0] > -0.4:
                self.velocity[0] = 0
            elif self.velocity[0] > 0:
                self.velocity[0] -= 0.4
            elif self.velocity[0] < 0:
                self.velocity[0] += 0.4

        if not keys[pygame.K_DOWN] and not keys[pygame.K_UP] and self.velocity[1] != 0:
            if self.velocity[1] < 0.4 and self.velocity[1] > -0.4:
                self.velocity[1] = 0
            elif self.velocity[1] > 0:
                self.velocity[1] -= 0.4
            elif self.velocity[1] < 0:
                self.velocity[1] += 0.4
