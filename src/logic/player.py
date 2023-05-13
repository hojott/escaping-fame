import pygame
import math

from ..constants import *
from ..graphics import drawPlayer

class Player:
    def __init__(self, game, pos_on_map: list, pos_on_screen: list) -> None:
        self.game = game
        
        self.pos_on_map = pos_on_map
        self.pos_on_screen = pos_on_screen

        # Same coordinates as Minecraft: east is positive x and south is positive y
        self.velocity = [0, 0]
        drawPlayer(self.game.screen, self.pos_on_screen)

    def tick(self) -> None:
        self.input()
        self.inputnt()
        self.move_player()
        drawPlayer(self.game.screen, self.pos_on_screen)
    
    def calculate_movement(self) -> list[float, float]:
        movement = [float, float]

        if self.velocity[0] == 0 or self.velocity[1] == 0:
            movement[0] = self.velocity[0]
            movement[1] = self.velocity[1]
        
        else:
            # Fix diagonal movement being op
            velocity_pyth = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)

            movement[0] = self.velocity[0]*abs(self.velocity[0])/velocity_pyth
            movement[1] = self.velocity[1]*abs(self.velocity[1])/velocity_pyth

        return movement
    
    def move_player(self):
        movement = self.calculate_movement()

        # Horizontal movement
        if movement[0] >= 0:
            if self.game.world.position[0] + 1000 >= WORLD_SIZE[0] or self.pos_on_screen[0] < 475:
                self.pos_on_screen[0] += movement[0]
            else:
                self.pos_on_map[0] += movement[0]
                self.game.world.position[0] += movement[0]
            
        if movement[0] <= 0:
            if self.game.world.position[0] <= 0 or self.pos_on_screen[0] > 475:
                self.pos_on_screen[0] += movement[0]
            else:
                self.pos_on_map[0] += movement[0]
                self.game.world.position[0] += movement[0]

        # Vertical movement
        if movement[1] >= 0:
            if self.game.world.position[1] + 1000 >= WORLD_SIZE[1] or self.pos_on_screen[1] < 475:
                self.pos_on_screen[1] += movement[1]
            else:
                self.pos_on_map[1] += movement[1]
                self.game.world.position[1] += movement[1]
        
        if movement[1] <= 0:
            if self.game.world.position[1] <= 0 or self.pos_on_screen[1] > 475:
                self.pos_on_screen[1] += movement[1]
            else:
                self.pos_on_map[1] += movement[1]
                self.game.world.position[1] += movement[1]

    def input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # Positive x is east
            if self.velocity[0] < MAX_VELOCITY:
                self.velocity[0] += 1
            if self.velocity[0] == MAX_VELOCITY:
                self.velocity[0] = MAX_VELOCITY

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # Negative x is west
            if self.velocity[0] > -MAX_VELOCITY:
                self.velocity[0] -= 1
            if self.velocity[0] == -MAX_VELOCITY:
                self.velocity[0] = -MAX_VELOCITY

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            # Negative y is north
            if self.velocity[1] > -MAX_VELOCITY:
                self.velocity[1] -= 1
            if self.velocity[1] == -MAX_VELOCITY:
                self.velocity[1] = -MAX_VELOCITY

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # Positive y is west
            if self.velocity[1] < MAX_VELOCITY:
                self.velocity[1] += 1
            if self.velocity[1] == MAX_VELOCITY:
                self.velocity[1] = MAX_VELOCITY

    def inputnt(self):
        keys = pygame.key.get_pressed()

        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            if self.velocity[0] > 0:
                if self.velocity[0] > 1:
                    self.velocity[0] -= 1
                else:
                    self.velocity[0] = 0

            elif self.velocity[0] < 0:
                if self.velocity[0] < 1:
                    self.velocity[0] += 1
                else:
                    self.velocity[0] = 0

        if not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            if self.velocity[1] > 0:
                if self.velocity[1] > 1:
                    self.velocity[1] -= 1
                else:
                    self.velocity[1] = 0

            elif self.velocity[1] < 0:
                if self.velocity[1] < 1:
                    self.velocity[1] += 1
                else:
                    self.velocity[1] = 0
