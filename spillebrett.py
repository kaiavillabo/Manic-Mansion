import pygame as pg
from constants import *
from bilder import *


class Spillebrett:
    def __init__(self):
        self.running = True
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(SIZE)
        self.overlay = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.objekter = []

    def leggTilObjekt(self, objekt):
        self.objekter.append(objekt)

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

            pg.draw.rect(self.overlay, (0, 0, 0, 128), (0, 0, FREEZONE, HEIGHT))
            pg.draw.rect(self.overlay, (0, 0, 0, 128), (WIDTH - FREEZONE, 0, FREEZONE, HEIGHT))

            self.screen.blit(self.overlay, (0, 0))

            for objekt in self.objekter:
                objekt.flytt()
                objekt.tegn(self.screen)

            pg.display.update()