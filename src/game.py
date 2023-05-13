import pygame

# Use relative imports because running app from main.py
from .constants import *
from .graphics import *
from .logic.world import World
from .logic.battle import Battle

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)
        self.screen: tuple = pygame.display.set_mode(SCREEN_SIZE)
        self.state: str = "menu"
        self.world: World = None
        self.battle: Battle = None

        self.start_game()


    def start_game(self):
        self.running: bool = True

        clock = pygame.time.Clock()

        while self.running:
            if self.state == "menu":
                drawMenu(self.screen)
            elif self.state == "battle":
                self.battle.rects = drawBattle(self, self.battle)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        self.start_battle()
                    if self.state == "menu":
                        if event.key == pygame.K_q:
                            self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.state == "menu":
                        if pos[0] > 215 and pos[0] < 785:
                            if pos[1] > 550 and pos[1] < 660:
                                self.load_game()
                            elif pos[1] > 700 and pos[1] < 810:
                                self.running = False

                    if self.state == "battle":
                        if self.battle.turn % 2 == 0:
                            self.battle.switchTurn()
                        else:
                            for i, textbox in enumerate(self.battle.textbox_rects):
                                if textbox.collidepoint(pos[0], pos[1]):
                                    self.battle.pickDialog(i)

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

    def load_game(self):
        self.state = "game"
        self.world = World(self)

    def start_battle(self):
        self.state = "battle"
        self.battle = Battle(self)
