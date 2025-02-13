import pygame as pg
from constants import *
from bilder import *
from character import Character

class Sau(Character):
    def __init__(self, x, y):
        super().__init__(x, y, sau_image)