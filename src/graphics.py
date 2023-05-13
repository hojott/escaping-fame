import pygame
from .constants import *
from .map import maps

exit = pygame.image.load("src/graphics/exit.png")
exit = pygame.transform.scale(exit, BUTTON_SIZE)

start_game = pygame.image.load("src/graphics/start_game.png")
start_game = pygame.transform.scale(start_game, BUTTON_SIZE)

mainCharacter_battle = pygame.image.load("src/graphics/mainCharacter_battle.png")
mainCharacter_battle = pygame.transform.scale(mainCharacter_battle, CHARACTER_SIZE)

enemy1 = pygame.image.load("src/graphics/enemy1.png")
enemy1 = pygame.transform.scale(enemy1, CHARACTER_SIZE)

textbox = pygame.image.load("src/graphics/textbox.png")
textbox = pygame.transform.scale(textbox, TEXTBOX_SIZE)
textbox_small = pygame.transform.scale(textbox, SMALL_TEXTBOX_SIZE)

player = pygame.image.load("src/graphics/start_game.png")
player = pygame.transform.scale(player, PLAYER_SIZE)

tiles = {}
"""
tiles = {
    "sw1" = sw1-kuva
    ...
}
"""
for i in range(1, 6):
    tiles[f"sw{i}"] = pygame.image.load(f"src/graphics/tiles/sw{i}.png")
    tiles[f"sw{i}"] = pygame.transform.scale(tiles[f"sw{i}"], TILE_SIZE)

def drawMenu(screen):
    screen.fill((255, 182, 193))
    screen.blit(start_game, (215, 550))
    screen.blit(exit, (215, 700))

def drawBattle(game, battle):
    screen = game.screen

    screen.fill((255, 255, 0))
    screen.blit(mainCharacter_battle, (0, 230))
    screen.blit(enemy1, (500, 50))
    screen.blit(textbox, (100, 780))
    renderText(battle.enemy_dialog, (160, 820), game)

    if battle.turn % 2 == 0:
        renderText("Click to continue...", (640, 900), game)
    else:
        for i in range(4):
            coords = (250, 200 + 120 * i)
            screen.blit(textbox_small, coords)
            renderText(battle.player_dialogs[i], (275, 232 + 120 * i), game)

def renderText(text, coords, game):
    text = game.font.render(text, False, (0, 0, 0))
    game.screen.blit(text, coords)

def drawWorld(screen, map_num: int, world_pos: list) -> list[int, int]:
    screen.fill((255, 182, 193))
    for y_pos, horizontal_stripe in enumerate(maps[map_num], -1):
        if y_pos == -1:
            # First line of list is map size (yes it has weird name)
            MAP_SIZE = horizontal_stripe
        else:    
            for x_pos, vertical_point in enumerate(horizontal_stripe):
                screen.blit(tiles[vertical_point], (-world_pos[0] + 500*x_pos, -world_pos[1] + 500*y_pos))
    return MAP_SIZE

def drawPlayer(screen, pos_on_screen: list):
    screen.blit(player, tuple(pos_on_screen))
