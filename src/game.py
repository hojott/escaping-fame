import pygame

# Use relative imports because running app from main.py
from .constants import *
from .graphics import *
from .logic.world import World
from .logic.battle import Battle
from .logic.player import Player

class Game:
    def __init__(self):
        pygame.init()

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)

        self.screen: tuple = pygame.display.set_mode(SCREEN_SIZE)

        pygame.display.set_caption("Tulevaisuuspeli")

        self.icon = pygame.image.load('src/graphics/start_game.png')
        pygame.display.set_icon(self.icon)

        self.state: str = "menu"
        self.world: World = None
        self.battle: Battle = None
        self.player: Player = None

        self.start_game()


    def start_game(self):
        self.running: bool = True
        self.load_menu()

        clock = pygame.time.Clock()

        while self.running:
            keys = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            
            # Drawing
            if self.state == "menu":
                drawMenu(self.screen)

                if keys[pygame.K_0]:
                    self.start_battle()
                if keys[pygame.K_q]:
                    self.running = False

            elif self.state == "battle":
                drawBattle(self, self.battle)

            elif self.state == "game":
                self.world.tick()

                self.player.tick()

                if keys[pygame.K_ESCAPE]:
                    self.load_menu()
                if keys[pygame.K_0]:
                    self.start_battle()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "menu":
                        if mouse_pos[0] > 215 and mouse_pos[0] < 785:
                            if mouse_pos[1] > 350 and mouse_pos[1] < 460:
                                self.load_game()
                            elif mouse_pos[1] > 500 and mouse_pos[1] < 610:
                                self.running = False

                    elif self.state == "battle":
                        if self.battle.turn % 3 != 1:
                            self.battle.switchTurn()
                        else:
                            for i, textbox in enumerate(self.battle.textbox_rects):
                                if textbox.collidepoint(mouse_pos[0], mouse_pos[1]):
                                    self.battle.pickDialog(i)

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

    def load_menu(self):
        self.state = "menu"

    def load_game(self):
        self.state = "game"
        self.world = World(self, map_num = 0)
        self.player = Player(self, pos_on_map = [10, 10], pos_on_screen = [10, 10])

    def start_battle(self):
        self.state = "battle"
        self.battle = Battle(self)
