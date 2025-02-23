from constants import *
from bilder import *
from character import Character

class Busk(Character):
    def __init__(self, x, y):
        super().__init__(x, y, busk_image)