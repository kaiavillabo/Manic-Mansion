import pygame as pg
from spillebrett import Spillebrett
from bilder import *
from rodhette import Rodhette
from ulv import Ulv
from busk import Busk
from spawnpoint import spawnpoint

pg.init()

brett = Spillebrett()
koordinater = spawnpoint()

rodhette = Rodhette(25, 327, brett)
ulver = [Ulv(x, y) for x, y in koordinater[:3]]

busker = [Busk(x, y) for x, y in koordinater[3:]]

brett.leggTilObjekt(rodhette)
for ulv in ulver:
    brett.leggTilObjekt(ulv)
for busk in busker:
    brett.leggTilObjekt(busk)

brett.mainloop()