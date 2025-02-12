import pygame as pg
from constants import *
from bilder import *
from ulv import Ulv
from busk import Busk


class Spillebrett:
    def __init__(self):
        self.running = True
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(SIZE)
        self.overlay = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.objekter = []
        self.ulver = []
        self.busker = []

    def leggTilObjekt(self, objekt):
        self.objekter.append(objekt)
        if isinstance(objekt, Ulv):  # sjekk om objektet er en ulv
            self.ulver.append(objekt)
        if isinstance(objekt, Busk):  # sjekk om objektet er en busk
            self.busker.append(objekt)

    def fjernObjekt(self, objekt):
        self.objekter.remove(objekt)

    def mainloop(self):
        while self.running:

            # Sjekk om brukeren avslutter vinduet:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.clock.tick(FPS)

            # lager bakgrunnen med frisonene
            self.screen.blit(bakgrunn, (0,0))

            for ulv in self.ulver:
                ulv.update(self.busker)  # snur når de treffer kantene og buskene

            pg.draw.rect(self.overlay, (0, 0, 0, 128), (0, 0, FREEZONE, HEIGHT))
            pg.draw.rect(self.overlay, (0, 0, 0, 128), (WIDTH - FREEZONE, 0, FREEZONE, HEIGHT))

            self.screen.blit(self.overlay, (0, 0))

        # Oppdater og tegn alle objekter
            for objekt in self.objekter:
                if not isinstance(objekt, Ulv):  # Rodhette og andre objekter
                    objekt.move()
                objekt.draw(self.screen)

            pg.display.update()