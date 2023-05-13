import pygame
from .constants import *
from .map import maps

exit = pygame.image.load("src/graphics/exit.png")
exit = pygame.transform.scale(exit, BUTTON_SIZE)

start_game = pygame.image.load("src/graphics/start_game.png")
start_game = pygame.transform.scale(start_game, BUTTON_SIZE)

mainmenu = pygame.image.load("src/graphics/mainmenu.png")
mainmenu = pygame.transform.scale(mainmenu, SCREEN_SIZE)

mainCharacter_battle = pygame.image.load("src/graphics/mainCharacter_battle.png")
mainCharacter_battle = pygame.transform.scale(mainCharacter_battle, CHARACTER_SIZE)

enemy1 = pygame.image.load("src/graphics/enemy1.png")
enemy1 = pygame.transform.scale(enemy1, CHARACTER_SIZE)

enemy2 = pygame.image.load("src/graphics/enemy2.png")
enemy2 = pygame.transform.scale(enemy2, CHARACTER_SIZE)

enemy3 = pygame.image.load("src/graphics/enemy3.png")
enemy3 = pygame.transform.scale(enemy3, CHARACTER_SIZE)

enemies = [enemy1, enemy2, enemy3]

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
    screen.blit(mainmenu, (0, 0))
    screen.blit(start_game, (215, 350))
    screen.blit(exit, (215, 500))

def drawBattle(game, battle):
    screen = game.screen

    screen.fill((255, 255, 0))
    screen.blit(mainCharacter_battle, (0, 230))
    screen.blit(battle.enemy, (500, 50))
    screen.blit(textbox, (100, 780))

    if battle.turn % 3 == 1:
        for i in range(4):
            coords = (250, 200 + 120 * i)
            screen.blit(textbox_small, coords)
            renderText(battle.dialog["answers"][i][0], (275, 232 + 120 * i), game)
    else:
        renderText("Click to continue...", (640, 900), game)
    if battle.turn % 3 != 2:
        renderText(battle.dialog["dialog"], (160, 820), game)
    elif battle.player_pick[1] == 1:
        renderText("Your pick was bad, so your stress increases.", (160, 820), game)
    elif battle.player_pick[1] == 0:
        renderText("Your pick neutral, so your stress doesn't change.", (160, 820), game)
    else:
        renderText("Your pick good, so your stress relieves.", (160, 820), game)

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
