import pygame
from .constants import *
from .dialogs import texts
from .map import maps
from math import floor
from random import choice

exit = pygame.image.load("src/graphics/exit.png")
exit = pygame.transform.scale(exit, BUTTON_SIZE)

info = pygame.image.load("src/graphics/info.png")
info = pygame.transform.scale(info, BUTTON_SIZE)

start_game = pygame.image.load("src/graphics/start_game.png")
start_game = pygame.transform.scale(start_game, BUTTON_SIZE)

mainmenu = pygame.image.load("src/graphics/mainmenu.png")
mainmenu = pygame.transform.scale(mainmenu, SCREEN_SIZE)

intro = pygame.image.load("src/graphics/intro.png")
intro = pygame.transform.scale(intro, SCREEN_SIZE)

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

player = pygame.image.load("src/graphics/mc.png")
player = pygame.transform.scale(player, PLAYER_SIZE)

human1_tex = pygame.image.load("src/graphics/randdude.png")
human1_tex = pygame.transform.scale(human1_tex, HUMAN_SIZE)

car1_tex = pygame.image.load("src/graphics/car.png")
car1_tex = pygame.transform.scale(car1_tex, CAR_SIZE)

car2_tex = pygame.image.load("src/graphics/car_reversed.png")
car2_tex = pygame.transform.scale(car2_tex, CAR_SIZE)

kaarija_tex = pygame.image.load("src/graphics/kaarija.png")
kaarija_tex = pygame.transform.scale(kaarija_tex, CAR_SIZE)

fan1_tex = pygame.image.load("src/graphics/en1.png")
fan1_tex = pygame.transform.scale(fan1_tex, HUMAN_SIZE)

fan2_tex = pygame.image.load("src/graphics/en2.png")
fan2_tex = pygame.transform.scale(fan2_tex, HUMAN_SIZE)

tiles = {}
"""
tiles = {
    "sw1": sw1-kuva
    ...
}
"""
for i in range(1, 10):
    tiles[f"sw{i}"] = pygame.image.load(f"src/graphics/tiles/sw{i}.png")
    tiles[f"sw{i}"] = pygame.transform.scale(tiles[f"sw{i}"], TILE_SIZE)

stressbar = pygame.image.load("src/graphics/stressbar.png")
stressbar = pygame.transform.flip(stressbar, False, True)

stresspoint = pygame.image.load("src/graphics/stresspoint.png")
stresspoint2 = pygame.image.load("src/graphics/stresspoint2.png")
stresspoint3 = pygame.image.load("src/graphics/stresspoint3.png")
stresspoint4 = pygame.image.load("src/graphics/stresspoint4.png")
stresspoint5 = pygame.image.load("src/graphics/stresspoint5.png")

joke_ending = pygame.image.load("src/graphics/jokeEnding.png")
joke_ending = pygame.transform.scale(joke_ending, SCREEN_SIZE)

kaarija_ending = pygame.image.load("src/graphics/kaarija_ending.png")
kaarija_ending = pygame.transform.scale(kaarija_ending, SCREEN_SIZE)

good_ending = pygame.image.load("src/graphics/good_ending.png")
good_ending = pygame.transform.scale(good_ending, SCREEN_SIZE)

bad_ending = pygame.image.load("src/graphics/bad_ending.png")
bad_ending = pygame.transform.scale(bad_ending, SCREEN_SIZE)

endings = {
    "joke_ending": joke_ending,
    "kaarija_ending": kaarija_ending,
    "good_ending": good_ending,
    "bad_ending": bad_ending
}

def drawMenu(game):
    screen = game.screen
    
    screen.blit(mainmenu, (0, 0))
    screen.blit(start_game, (215, 270))
    screen.blit(info, (215, 420))
    screen.blit(exit, (215, 570))

def drawInfo(game):
    screen = game.screen

    screen.blit(intro, (0, 0))
    for i, row in enumerate(texts["intro"]):
        renderText(row, (20, 40 + i * 40), game)

def drawPause(game):
    screen = game.screen

    pause_overlay = pygame.Surface(SCREEN_SIZE)
    pause_overlay.set_alpha(128)
    pause_overlay.fill((0, 0, 0))
    
    screen.blit(pause_overlay, (0, 0))

def drawPausemenu(game):
    bg = pygame.Rect(150, 490, 700, 100)
    pygame.draw.rect(game.screen, (255,255,204), bg)
    renderText("Game paused, esc to unpause.", (165, 500), game, True)

def drawUI(game, at_bottom = False):
    screen = game.screen

    alpha = 190
    if game.player.pos_on_screen[0] + PLAYER_SIZE[0] < 900 and game.player.pos_on_screen[0] > 100:
        if game.player.pos_on_screen[1] < 200:
            alpha = 40

        stressbar.set_alpha(alpha)
        for i in range(game.player.stress):
            stresspoint.set_alpha(alpha)

        time = game.player.time
        timebar_alpha = alpha if time > 0 else 0

        screen.blit(stressbar.convert_alpha(), (169, 800))
        stress = game.player.stress
        for i in range(10):
            if i < stress:
                if i < 3:
                    screen.blit(stresspoint3, (179 + i * 64.5, 855))
                elif i < 6:
                    screen.blit(stresspoint4, (179 + i * 64.5, 855))
                elif i < 9:
                    screen.blit(stresspoint5, (179 + i * 64.5, 855))
                else:
                    screen.blit(stresspoint2, (179 + i * 64.5, 855))
            else:
                screen.blit(stresspoint, (179 + i * 64.5, 855))

        timebar = pygame.Rect(240, 813, time * 26, 32)
        pygame.draw.rect(screen, (173, 216, 230, timebar_alpha), timebar)

    else:
        alpha = 190
        if game.player.pos_on_screen[0] < 900 and game.player.pos_on_screen[0] > 100:
            if game.player.pos_on_screen[1] < 200:
                alpha = 40

        stressbar.set_alpha(alpha)
        for i in range(game.player.stress):
            stresspoint.set_alpha(alpha)

        time = game.player.time
        timebar_alpha = alpha if time > 0 else 0

        screen.blit(stressbar.convert_alpha(), (169, 30))
        stress = game.player.stress
        for i in range(10):
            if i < stress:
                if i < 3:
                    screen.blit(stresspoint3, (179 + i * 64.5, 85))
                elif i < 6:
                    screen.blit(stresspoint4, (179 + i * 64.5, 85))
                elif i < 9:
                    screen.blit(stresspoint5, (179 + i * 64.5, 85))
                else:
                    screen.blit(stresspoint2, (179 + i * 64.5, 85))
            else:
                screen.blit(stresspoint, (179 + i * 64.5, 85))

        timebar = pygame.Rect(240, 43, time * 26, 32)
        pygame.draw.rect(screen, (173, 216, 230, timebar_alpha), timebar)

def drawBattle(game, battle):
    screen = game.screen

    screen.blit(mainCharacter_battle, (-80, 230))
    screen.blit(battle.enemy, (600, 100))
    screen.blit(textbox, (100, 780))

    dialog = battle.dialogs[floor(battle.turn / 3)]

    if battle.turn % 3 == 1:
        for i in range(4):
            coords = (250, 200 + 120 * i)
            screen.blit(textbox_small, coords)
            renderText(dialog["answers"][i][0], (275, 232 + 120 * i), game)
            renderText("Choose your answer...", (620, 900), game)
    else:
        renderText("Click to continue...", (640, 900), game)
    if battle.turn % 3 != 2:
        renderText(dialog["dialog"], (160, 820), game)
    elif battle.player_pick[1] == 1:
        renderText("Your pick was bad, so your stress increases.", (160, 820), game)
    elif battle.player_pick[1] == 0:
        renderText("Your pick neutral, so your stress doesn't change.", (160, 820), game)
    else:
        renderText("Your pick good, so your stress relieves.", (160, 820), game)

def renderText(text, coords, game, bigFont = False):
    if bigFont:
        text = game.bigFont.render(text, False, (0, 0, 0))
    else:
        text = game.font.render(text, False, (0, 0, 0))
    game.screen.blit(text, coords)

def drawWorld(game, map_num: int, world_pos: list) -> list[int, int]:
    screen = game.screen

    screen.fill((255, 182, 193))
    
    # Draw in all the tiles from map.py
    for y_pos, horizontal_stripe in enumerate(maps[map_num], -1):
        if y_pos == -1:
            # First line of list is map size (yes it has weird names)
            MAP_SIZE = horizontal_stripe
        else:
            for x_pos, vertical_point in enumerate(horizontal_stripe):
                screen.blit(tiles[vertical_point], (-world_pos[0] + TILE_SIZE[0]*x_pos, -world_pos[1] + TILE_SIZE[1]*y_pos))

    return MAP_SIZE

def drawPlayer(game, pos_on_screen: list):
    screen = game.screen

    screen.blit(player, tuple(pos_on_screen))

def drawHuman(game, position, texture):
    screen = game.screen

    screen.blit(texture, tuple(position))

def drawEnding(game, ending):
    screen = game.screen

    screen.blit(endings[ending], (0, 0))

    if ending == "joke_ending":
        y = 150
    elif ending == "kaarija_ending":
        y = 350
    elif ending == "bad_ending":
        y = 10
    else:
        y = 40

    for i, row in enumerate(texts[ending]):
        renderText(row, (20, y + i * 40), game)
