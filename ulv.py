import pygame as pg
from constants import *
from bilder import *
from character import Character

class Ulv(Character):
    def __init__(self, x, y):
        super().__init__(x, y, ulv_image)
        self.dx = ULV_SPEED
        self.dy = ULV_SPEED

    def update(self):
        super().move()

        if self.x <= 0 or self.x >= (WIDTH - self.width):
            self.dx = -self.dx  

            # Sjekk kollisjon med topp/bunn kant
        if self.y <= 0 or self.y >= (HEIGHT - self.height):
            self.dy = -self.dy