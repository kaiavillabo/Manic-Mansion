import pygame as pg
from constants import *
from bilder import *
from ulv import Ulv
from busk import Busk
from sau import Sau
from rodhette import Rodhette
from character import Character

class Spillebrett:
    def __init__(self):
        self.running = True
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(SIZE)
        self.overlay = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.objekter = []
        self.ulver = []
        self.busker = []
        self.sauer = []
        self.rodhette = None
        self.blod = None

    def leggTilObjekt(self, objekt):
        self.objekter.append(objekt)
        if isinstance(objekt, Ulv):  # sjekk om objektet er en ulv
            self.ulver.append(objekt)
        elif isinstance(objekt, Busk):  # sjekk om objektet er en busk
            self.busker.append(objekt)
        elif isinstance(objekt, Sau):  # sjekk om objektet er en sau
            self.sauer.append(objekt)
        elif isinstance(objekt, Rodhette):
            self.rodhette = objekt  # Lagre referanse til Rødhette

    def fjernObjekt(self, objekt):
        self.objekter.remove(objekt)

    def vis_dodsskjerm(self):
        # Vis blodet bare hvis Rødhette er død
        self.screen.blit(blod_image, (262, 102))  # Plasserer blodet på skjermen
        font = pg.font.Font(None, 100)  # Lager stor font
        tekst = font.render("DU DØDE", True, BLACK)
        tekst_rect = tekst.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(tekst, tekst_rect)
        pg.display.update()

        # Stopp spillet helt etter noen sekunder
        pg.time.delay(3000)
        pg.quit()
        exit()
    
    def vinn_spill(self):
        self.screen.blit(firework_image, (262, 102))  
        font = pg.font.Font(None, 100)
        tekst = font.render("DU VANT!", True, BLACK)
        tekst_rect = tekst.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(tekst, tekst_rect)
        pg.display.update()

        pg.time.delay(3000)
        pg.quit()
        exit()

    def game_over(self):
        self.rodhette.dead = True
        self.vis_dodsskjerm()  # Vise Game Over-skjerm

    def mainloop(self):
        while self.running:

            # Sjekk om brukeren avslutter vinduet:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.clock.tick(FPS)

            # Lager bakgrunnen med frisonene
            self.screen.blit(bakgrunn, (0, 0))

            # Hvis Rødhette ikke er død, kan ulvene bevege seg
            if not self.rodhette.dead:
                for ulv in self.ulver:
                    ulv.update(self.busker)

                pg.draw.rect(self.overlay, (0, 0, 0, 128), (0, 0, FREEZONE, HEIGHT))
                pg.draw.rect(self.overlay, (0, 0, 0, 128), (WIDTH - FREEZONE, 0, FREEZONE, HEIGHT))

                self.screen.blit(self.overlay, (0, 0))

                # Oppdater og tegn alle objekter (inkludert Rødhette, hvis hun er i live)
                for objekt in self.objekter:
                    if not isinstance(objekt, Ulv):  # Rodhette og andre objekter
                        objekt.move()
                    objekt.draw(self.screen)

            # Hvis Rødhette er død, vis blodet og game over skjerm
            else:
                self.vis_dodsskjerm()  # Vis blod og "DU DØDE"-skriften

            pg.display.update()