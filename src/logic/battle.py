import pygame
from random import choice, randint
from math import floor

from ..graphics import textbox_small, enemies
from ..dialogs import dialogs

class Battle:
    def __init__(self, game):
        self.game = game
        self.textbox_rects = [pygame.Rect(250, 200 + 120 * i, textbox_small.get_width(), textbox_small.get_height()) for i in range(4)]
        self.turn = 0
        self.questions = randint(3, 4)
        self.dialogs = []
        self.player_pick = None
        self.enemy = enemies[randint(0, 2)]
        self.generateDialogs()

    def generateDialogs(self):
        player = self.game.player

        all = dialogs[0] + dialogs[1] + dialogs[2] + dialogs[3]

        if len(all) < self.questions:
            raise ValueError("Ran out of dialogs")

        for _ in range(self.questions):
            if player.stress < 4 and len(dialogs[0]) > 0:
                self.dialogs.append(dialogs[0].pop())
            elif player.stress < 7 and len(dialogs[1]) > 0:
                self.dialogs.append(dialogs[1].pop())
            elif player.stress < 10 and len(dialogs[2]) > 0:
                self.dialogs.append(dialogs[2].pop())
            elif len(dialogs[3]) > 0:
                self.dialogs.append(dialogs[3].pop())
            elif len(all) > 0:
                chosen_dialog = choice(all)
                self.dialogs.append(chosen_dialog)
                for dialog_group in dialogs:
                    if chosen_dialog in dialog_group:
                        dialog_group.remove(chosen_dialog)
                        break
            else:
                print("no more dialogs")
        
        for i in range(len(self.dialogs)):
            dialog = self.dialogs[i]
            answers = dialog["answers"]
            new_answers = []
            for answer in answers:
                if isinstance(answer, tuple):
                    new_answers.append(answer)
                elif isinstance(answer, list):
                    random_answer = choice(answer)
                    new_answers.append(random_answer)
            dialog["answers"] = new_answers
            self.dialogs[i] = dialog

    def switchTurn(self):
        self.turn += 1

    def pickDialog(self, dialogIndex):
        self.player_pick = self.dialogs[floor(self.turn / 3)]["answers"][dialogIndex]
        self.game.player.endTurn(self.player_pick[1])
        self.switchTurn()
        self.questions -= 1
        if self.questions == 0:
            self.endBattle()

    def endBattle(self):
        self.game.state = "game"
