import pygame
import random

from ..graphics import textbox_small, enemies
from ..dialogs import dialogs

class Battle:
    def __init__(self, game):
        self.game = game
        self.textbox_rects = [pygame.Rect(250, 200 + 120 * i, textbox_small.get_width(), textbox_small.get_height()) for i in range(4)]
        self.turn = 0
        self.questions = random.randint(2, 4)
        self.dialog = None
        self.player_pick = None
        self.enemy = enemies[random.randint(0, 2)]
        self.generateDialog()

    def generateDialog(self):
        player = self.game.player

        if player.stress < 4 and len(dialogs[0]) > 0:
            self.dialog = dialogs[0].pop()
        elif player.stress < 7 and len(dialogs[1]) > 0:
            self.dialog = dialogs[1].pop()
        elif player.stress < 10 and len(dialogs[2]) > 0:
            self.dialog = dialogs[2].pop()
        elif len(dialogs[3]) > 0:
            self.dialog = dialogs[3].pop()
        elif len(dialogs[0]) > 0 or len(dialogs[1]) > 0 or len(dialogs[2]) > 0:
            self.dialog = random.choice(dialogs[2][0] if len(dialogs[2]) > 0 else dialogs[1][0] if len(dialogs[1]) > 0 else dialogs[0][0] if len(dialogs[0]) > 0 else [None])
        else:
            print("no more dialogs")
            return
        if self.dialog == []:
            print("no more dialogs")
            return

    def switchTurn(self):
        self.turn += 1

    def pickDialog(self, dialogIndex):
        self.player_pick = self.dialog["answers"][dialogIndex]
        self.game.player.endTurn(self.player_pick[1])
        self.switchTurn()
        self.generateDialog()
        self.questions -= 1
        if self.questions == 0:
            self.endBattle()

    def endBattle(self):
        print("battle ends")
        self.game.state = "game"
