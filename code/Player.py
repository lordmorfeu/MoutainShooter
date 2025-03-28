#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shootPlayer_sound = pygame.mixer.Sound(f'./asset/{self.name}ShotSound.wav')
        self.shootPlayer_sound.set_volume(0.05)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        """Move the player based on key inputs."""
        pressed_key = pygame.key.get_pressed()

        # Move up
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        # Move down
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        # Move left
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        # Move right
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        """Handle shooting with shot delay."""
        self.shot_delay -= 1

        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()

            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                self.shootPlayer_sound.play()
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
