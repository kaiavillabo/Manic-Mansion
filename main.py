import pygame as pg
from bilder import *
from rodhette import Rodhette
from ulv import Ulv
from busk import Busk
from spawnpoint import spawnpoint
from sau import Sau
from spillebrett import Spillebrett

pg.init()

brett = Spillebrett()

koordinater = spawnpoint()

rodhette = Rodhette(25, 327, brett)

ulver = [Ulv(x, y) for x, y in koordinater[:3]]

busker = [Busk(x, y) for x, y in koordinater[3:]]

sau1 = Sau(WIDTH-75, 177)
sau2 = Sau(WIDTH-75, 327)
sau3 = Sau(WIDTH-75, 477)

sauer = [sau1, sau2, sau3]

brett.leggTilObjekt(rodhette)
for ulv in ulver:
    brett.leggTilObjekt(ulv)
for busk in busker:
    brett.leggTilObjekt(busk)
for sau in sauer:
    brett.leggTilObjekt(sau)

brett.mainloop()