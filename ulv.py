import pygame as pg
from constants import *
from bilder import *
from character import Character

class Ulv(Character):
    def __init__(self, x, y):
        super().__init__(x, y, ulv_image)
        self.dx = ULV_SPEED
        self.dy = ULV_SPEED
