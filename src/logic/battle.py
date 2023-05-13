import pygame
from ..graphics import textbox_small

class Battle:
    def __init__(self, game):
        self.game = game
        self.textbox_rects = [pygame.Rect(250, 200 + 120 * i, textbox_small.get_width(), textbox_small.get_height()) for i in range(4)]
        self.turn = 0
        self.enemy_dialog = None
        self.player_dialogs = None
        self.generateDialog()

    def generateDialog(self):
        # TODO: proper dialog generation
        self.enemy_dialog = "hahahahaha et ole yksin >:)"
        self.player_dialogs = ["nyyh :(", "apuaaaa", "Mui.", "test"]

    def switchTurn(self):
        self.turn += 1
    
    def pickDialog(self, dialogIndex):
        # TODO
        print(dialogIndex)
