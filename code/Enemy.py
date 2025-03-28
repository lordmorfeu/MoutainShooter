#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shootEnemy_sound = pygame.mixer.Sound(f'./asset/{self.name}ShotSound.mp3')
        self.shootEnemy_sound.set_volume(0.1)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.x -= ENTITY_SPEED[self.name]

    def shoot(self):
        if self.shot_delay > 0:
            self.shot_delay -= 1

        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            self.shootEnemy_sound.play()
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
