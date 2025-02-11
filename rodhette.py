import pygame as pg
from constants import *
from bilder import *
from character import Character

class Rodhette(Character):
    def __init__(self, x, y):
        super().__init__(x, y, rodhette_image)
        self.carry = False
        self.dead = False


    def move(self):
        if not self.dead:
            keys_pressed = pg.key.get_pressed()
            if keys_pressed[pg.K_LEFT] and self.x > 0:
                self.x -= RODHETTE1_SPEED
                self.image = rodhette_image
            if keys_pressed[pg.K_RIGHT] and self.x < WIDTH - self.width:
                self.x += RODHETTE1_SPEED
                self.image = rodhette_image
            if keys_pressed[pg.K_DOWN] and self.y < HEIGHT - self.height:
                self.y += RODHETTE1_SPEED
                self.image = rodhette_image
            if keys_pressed[pg.K_UP] and self.y > 0:
                self.y -= RODHETTE1_SPEED
                self.image = rodhette_image
