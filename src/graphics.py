import pygame
from .constants import *

exit = pygame.image.load("src/graphics/exit.png")
exit = pygame.transform.scale(exit, BUTTON_SIZE)

start_game = pygame.image.load("src/graphics/start_game.png")
start_game = pygame.transform.scale(start_game, BUTTON_SIZE)

player = pygame.image.load("src/graphics/start_game.png")
player = pygame.transform.scale(player, PLAYER_SIZE)

def drawMenu(screen):
    screen.fill((255, 182, 193))
    screen.blit(start_game, (215, 550))
    screen.blit(exit, (215, 700))

def drawWorld(screen):
    screen.fill((255, 182, 193))

def drawPlayer(screen, pos_on_screen: list):
    screen.blit(player, tuple(pos_on_screen))
