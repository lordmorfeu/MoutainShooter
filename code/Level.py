#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.remaining_time = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entities: list[Entity] = []
        self.entities.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entities.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entities.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for entity in self.entities:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
                if isinstance(entity, (Player, Enemy)):
                    shot = entity.shoot()
                    if shot is not None:
                        self.entities.append(shot)
                if entity.name == 'Player1':
                    self.display_text(14, f'Player 1 - HP: {entity.health} | Score: {entity.score}', C_GREEN, (10, 25))
                if entity.name == 'Player2':
                    self.display_text(14, f'Player 2 - HP: {entity.health} | Score: {entity.score}', C_CYAN, (10, 45))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    enemy_type = random.choice(('Enemy1', 'Enemy2'))
                    self.entities.append(EntityFactory.get_entity(enemy_type))
                if event.type == EVENT_TIMEOUT:
                    self.remaining_time -= TIMEOUT_STEP
                    if self.remaining_time == 0:
                        for entity in self.entities:
                            if isinstance(entity, Player) and entity.name == 'Player1':
                                player_score[0] = entity.score
                            if isinstance(entity, Player) and entity.name == 'Player2':
                                player_score[1] = entity.score
                        return True

                if not any(isinstance(entity, Player) for entity in self.entities):
                    return False

            self.display_text(14, f'{self.name} - Time: {self.remaining_time / 1000 :.1f}s', C_WHITE, (10, 5))
            self.display_text(14, f'FPS: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.display_text(14, f'Entities: {len(self.entities)})', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entities)
            EntityMediator.verify_health(entity_list=self.entities)

    def display_text(self, size: int, content: str, color: tuple, position):
        font: Font = pygame.font.SysFont(name='Lucia Sans Typewriter', size=size)
        text_surf: Surface = font.render(content, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=position[0], top=position[1])
        self.window.blit(source=text_surf, dest=text_rect)
