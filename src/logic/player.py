import pygame
import math

from ..constants import *
from ..graphics import drawPlayer

class Player:
    def __init__(self, game, pos_on_map: list, pos_on_screen: list) -> None:
        self.game = game
        
        self.pos_on_map = pos_on_map
        self.pos_on_screen = pos_on_screen

        self.stress: int = 5
        self.time: float = 0.0

        self.game = game

        # Same coordinates as Minecraft: east is positive x and south is positive y
        self.velocity = [0, 0]
        self.MAX_VELOCITY = 5
        self.bounding_box = pygame.draw.rect(self.game.screen, 0, (self.pos_on_screen, PLAYER_SIZE))
        drawPlayer(self.game, self.pos_on_screen)

    def endTurn(self, stress: int):
        self.time += 0.5 + stress * 0.3
        self.stress -= stress
        if self.stress < 1: self.stress = 1
        elif self.stress > 10: self.stress = 10

    def tick(self) -> None:
        self.input()
        self.inputnt()
        self.move_player()
        drawPlayer(self.game, self.pos_on_screen)

        if self.pos_on_map[0] > 9000:
            self.game.load_ending("good_ending")

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
        # World and humans move around player, to make the map visible only sometimes

        # Horizontal movement
        if movement[0] >= 0:
            if self.game.world.position[0] + 1000 >= self.game.world.WORLD_SIZE[0] or self.pos_on_screen[0] < 475:
                self.pos_on_screen[0] += movement[0]
                self.bounding_box.update((self.pos_on_screen[0]+self.velocity[0], self.pos_on_screen[1]), PLAYER_SIZE)
            else:
                self.pos_on_map[0] += movement[0]
                self.game.world.position[0] += movement[0]
                for human in self.game.world.humans:
                    human[1].pos_on_screen[0] -= movement[0]
                    human[1].bounding_box.update((human[1].pos_on_screen[0]-self.velocity[0], human[1].pos_on_screen[1]), HUMAN_SIZE)
            
        if movement[0] <= 0:
            if self.game.world.position[0] <= 0 or self.pos_on_screen[0] > 475:
                self.pos_on_screen[0] += movement[0]
                self.bounding_box.update((self.pos_on_screen[0]+self.velocity[0], self.pos_on_screen[1]), PLAYER_SIZE)
            else:
                self.pos_on_map[0] += movement[0]
                self.game.world.position[0] += movement[0]
                for human in self.game.world.humans:
                    human[1].pos_on_screen[0] -= movement[0]
                    human[1].bounding_box.update((human[1].pos_on_screen[0]-self.velocity[0], human[1].pos_on_screen[1]), HUMAN_SIZE)

        # Vertical movement
        if movement[1] >= 0:
            if self.game.world.position[1] + 1000 >= self.game.world.WORLD_SIZE[1] or self.pos_on_screen[1] < 475:
                self.pos_on_screen[1] += movement[1]
                self.bounding_box.update((self.pos_on_screen[0], self.pos_on_screen[1]+self.velocity[1]), PLAYER_SIZE)
            else:
                self.pos_on_map[1] += movement[1]
                self.game.world.position[1] += movement[1]
                for human in self.game.world.humans:
                    human[1].pos_on_screen[1] -= movement[1]
                    human[1].bounding_box.update((human[1].pos_on_screen[0], human[1].pos_on_screen[1]-self.velocity[1]), HUMAN_SIZE)
        
        if movement[1] <= 0:
            if self.game.world.position[1] <= 0 or self.pos_on_screen[1] > 475:
                self.pos_on_screen[1] += movement[1]
                self.bounding_box.update((self.pos_on_screen[0], self.pos_on_screen[1]+self.velocity[1]), PLAYER_SIZE)
            else:
                self.pos_on_map[1] += movement[1]
                self.game.world.position[1] += movement[1]
                for human in self.game.world.humans:
                    human[1].pos_on_screen[1] -= movement[1]
                    human[1].bounding_box.update((human[1].pos_on_screen[0], human[1].pos_on_screen[1]-self.velocity[1]), HUMAN_SIZE)

    def input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # Positive x is east
            if self.velocity[0] < self.MAX_VELOCITY:
                self.velocity[0] += 1
            if self.velocity[0] == self.MAX_VELOCITY:
                self.velocity[0] = self.MAX_VELOCITY

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # Negative x is west
            if self.velocity[0] > -self.MAX_VELOCITY:
                self.velocity[0] -= 1
            if self.velocity[0] == -self.MAX_VELOCITY:
                self.velocity[0] = -self.MAX_VELOCITY

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            # Negative y is north
            if self.velocity[1] > -self.MAX_VELOCITY:
                self.velocity[1] -= 1
            if self.velocity[1] == -self.MAX_VELOCITY:
                self.velocity[1] = -self.MAX_VELOCITY

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # Positive y is west
            if self.velocity[1] < self.MAX_VELOCITY:
                self.velocity[1] += 1
            if self.velocity[1] == self.MAX_VELOCITY:
                self.velocity[1] = self.MAX_VELOCITY

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
