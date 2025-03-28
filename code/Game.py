#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_choice = menu.run()

            if menu_choice in MENU_OPTION[:3]:
                player_scores = [0, 0]  # [Player1, Player2]
                level = Level(self.window, 'Level1', menu_choice, player_scores)
                level_result = level.run(player_scores)

                if level_result:
                    level = Level(self.window, 'Level2', menu_choice, player_scores)
                    level_result = level.run(player_scores)

                    if level_result:
                        score.save(menu_choice, player_scores)

            elif menu_choice == MENU_OPTION[3]:
                score.show()
            elif menu_choice == MENU_OPTION[4]:
                pygame.quit()
                quit()

