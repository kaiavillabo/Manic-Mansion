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
        self.carrying_sau = None
        self.sauer_levert = 0
        self.leverte_sauer = set()

    def get_speed(self):
        # returnerer hastigheten basert på om Rødhette bærer en sau eller ikke.
        return RODHETTE2_SPEED if self.carry else RODHETTE1_SPEED

    def move(self):
        if self.dead:
            return  # Hvis Rødhette er død, kan hun ikke bevege seg

        keys_pressed = pg.key.get_pressed()
        speed = self.get_speed()

        new_x = self.x
        new_y = self.y

        if keys_pressed[pg.K_LEFT]:
            new_x -= speed
        if keys_pressed[pg.K_RIGHT]:
            new_x += speed
        if keys_pressed[pg.K_DOWN]:
            new_y += speed
        if keys_pressed[pg.K_UP]:
            new_y -= speed

        # sjekk om hun går utenfor skjermen
        if 0 <= new_x <= WIDTH - self.width and 0 <= new_y <= HEIGHT - self.height:
            if not self.kolliderer_med_busker(new_x, new_y):
                self.x = new_x
                self.y = new_y

        # sjekk kollisjon med ulv
        for ulv in self.spillebrett.ulver:
            if self.kolliderer_med_ulv(ulv, new_x, new_y):
                self.die()  # Rødhette dør ved kollisjon med ulv
                break  # Ingen grunn til å fortsette bevegelsen

        # plukk opp sau hvis hun ikke allerede bærer en
        if not self.carry:
            for sau in self.spillebrett.sauer:
                if self.kolliderer_med_sau(sau, self.x, self.y) and sau not in self.leverte_sauer:
                    self.pick_up(sau)
                    break  

        # slipp sau i frisonen
        if self.carry and self.x <= FREEZONE:
            self.drop_sau()

        self.image = rodhette_image

    def kolliderer_med_ulv(self, ulv, new_x, new_y):
        return (
            new_x < ulv.x + ulv.width and
            new_x + self.width > ulv.x and
            new_y < ulv.y + ulv.height and
            new_y + self.height > ulv.y
        )

    def die(self):
        self.dead = True  # Stopper bevegelse
        self.spillebrett.game_over()  # Kaller game_over metoden i Spillebrett

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
            # sjekk at sauen ikke allerede er levert
            if self.carrying_sau not in self.leverte_sauer:
                self.sauer_levert += 1
                self.leverte_sauer.add(self.carrying_sau)  # registrer at sauen er levert
                print(f"Sau levert! Totalt levert: {self.sauer_levert}")  # debug

            self.carrying_sau.x = 25  # plasser sauen i frisonen
            self.carry = False
            self.carrying_sau = None

        if self.sauer_levert == 3:
            self.spillebrett.vinn_spill()

    # def die(self):
    #     self.dead = True
    #     self.spillebrett.game_over()