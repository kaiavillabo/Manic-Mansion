import pygame as pg
from constants import *
from bilder import *
from character import Character
from sau import Sau

class Rodhette(Character):
    def __init__(self, x, y, spillebrett):
        super().__init__(x, y, rodhette_image)
        self.spillebrett = spillebrett
        self.carry = False
        self.dead = False

    def move(self):
        if not self.dead:
            keys_pressed = pg.key.get_pressed()

            # nye potensielle koordinater
            new_x = self.x
            new_y = self.y

            if keys_pressed[pg.K_LEFT]:
                new_x -= RODHETTE1_SPEED
            if keys_pressed[pg.K_RIGHT]:
                new_x += RODHETTE1_SPEED
            if keys_pressed[pg.K_DOWN]:
                new_y += RODHETTE1_SPEED
            if keys_pressed[pg.K_UP]:
                new_y -= RODHETTE1_SPEED

            # sjekker om hun går utenfor skjermen
            if 0 <= new_x <= WIDTH - self.width and 0 <= new_y <= HEIGHT - self.height:
                # Sjekk om hun kolliderer med en busk
                if not self.kolliderer_med_busker(new_x, new_y):
                    self.x = new_x
                    self.y = new_y

            if not self.carry:  # kan kun plukke opp en sau om hun ikke allerede bærer en
                for sau in self.spillebrett.sauer:
                    if self.kolliderer_med_sau(sau, self.x, self.y):
                        self.pick_up(sau)
                        break  # stopper etter å ha plukket opp en sau

            # sjekker om rødhette har nådd frisonen med en sau
            if self.carry and self.x <= FREEZONE:
                self.drop_sau()

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
    
    def kolliderer_med_sau(self, sau, new_x, new_y):
        return (
            new_x < sau.x + sau.width and
            new_x + self.width > sau.x and
            new_y < sau.y + sau.height and
            new_y + self.height > sau.y
        )

    def pick_up(self, sau):
        self.carry = True
        self.carrying_sau = sau
        sau.x = -100  # flytter sauen ut av skjermen

    def drop_sau(self):
        if self.carrying_sau:
            self.carrying_sau.x = 25  # setter ny x-posisjon i frisonen, samme y
            self.carry = False
            self.carrying_sau = None