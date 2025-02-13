import pygame as pg
from constants import *
from bilder import *
from character import Character

class Rodhette(Character):
    def __init__(self, x, y, spillebrett):
        super().__init__(x, y, rodhette_image)
        self.spillebrett = spillebrett
        self.carry = False
        self.dead = False

    def move(self):
        if not self.dead:
            keys_pressed = pg.key.get_pressed()

            # Lagre de nye potensielle koordinatene
            new_x = self.x
            new_y = self.y

            # Bevegelse basert på tastetrykk
            if keys_pressed[pg.K_LEFT]:
                new_x -= RODHETTE1_SPEED
            if keys_pressed[pg.K_RIGHT]:
                new_x += RODHETTE1_SPEED
            if keys_pressed[pg.K_DOWN]:
                new_y += RODHETTE1_SPEED
            if keys_pressed[pg.K_UP]:
                new_y -= RODHETTE1_SPEED

            # Sjekk om hun går utenfor skjermen
            if 0 <= new_x <= WIDTH - self.width and 0 <= new_y <= HEIGHT - self.height:
                # Sjekk om hun kolliderer med en busk
                if not self.kolliderer_med_busker(new_x, new_y):
                    self.x = new_x
                    self.y = new_y

            self.image = rodhette_image

    def kolliderer_med_busker(self, new_x, new_y):
        for busk in self.spillebrett.busker:
            if self.kolliderer_med_busk(busk, new_x, new_y):
                return True
        return False

    def kolliderer_med_busk(self, busk, new_x, new_y):
        return (
            new_x < busk.x + busk.width and
            new_x + self.width > busk.x and
            new_y < busk.y + busk.height and
            new_y + self.height > busk.y
        )
