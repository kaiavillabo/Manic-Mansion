import pygame as pg
from constants import *
from bilder import *
from character import Character

class Ulv(Character):
    def __init__(self, x, y):
        super().__init__(x, y, ulv_image)
        self.dx = ULV_SPEED
        self.dy = ULV_SPEED

    def update(self, busker):
        super().move()

        if self.x <= FREEZONE or self.x >= ((WIDTH-FREEZONE) - self.width):
            self.dx = -self.dx  

            # Sjekk kollisjon med topp/bunn kant
        if self.y <= 0 or self.y >= (HEIGHT - self.height):
            self.dy = -self.dy

        for busk in busker:
            if self.kolliderer_med(busk):  
                # Hvis kollisjon skjer, snu retning på ulven
                if self.x < busk.x or self.x + self.width > busk.x + busk.width:
                    self.dx = -self.dx  # Snu horisontal retning hvis kollisjon på x
                if self.y < busk.y or self.y + self.height > busk.y + busk.height:
                    self.dy = -self.dy  # Snu vertikal retning hvis kollisjon på y

    def kolliderer_med(self, busk): # aabb kollisjonssjekk
        return (
            self.x < busk.x + busk.width and
            self.x + self.width > busk.x and
            self.y < busk.y + busk.height and
            self.y + self.height > busk.y
        )