import pygame
from .constants import *

exit = pygame.image.load("src/graphics/exit.png")
exit = pygame.transform.scale(exit, BUTTON_SIZE)

start_game = pygame.image.load("src/graphics/start_game.png")
start_game = pygame.transform.scale(start_game, BUTTON_SIZE)

def drawMenu(screen):
    screen.fill((255, 182, 193))
    screen.blit(start_game, (215, 550))
    screen.blit(exit, (215, 700))
