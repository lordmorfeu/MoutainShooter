#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        if entity_name.startswith('Level1Bg'):
            return [Background(f'Level1Bg{i}', (x, 0)) for i in range(7) for x in (0, WIN_WIDTH)]
        elif entity_name.startswith('Level2Bg'):
            return [Background(f'Level2Bg{i}', (x, 0)) for i in range(5) for x in (0, WIN_WIDTH)]
        elif entity_name == 'Player1':
            return Player('Player1', (10, WIN_HEIGHT // 2 - 30))
        elif entity_name == 'Player2':
            return Player('Player2', (10, WIN_HEIGHT // 2 + 30))
        elif entity_name == 'Enemy1':
            return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
        elif entity_name == 'Enemy2':
            return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
