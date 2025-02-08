import pygame as pg
from spillebrett import Spillebrett
from bilder import *
from rodhette import Rodhette
from ulv import Ulv

pg.init()

brett = Spillebrett()

rodhette = Rodhette(25, 327)
ulv = Ulv(0,0)
ulv2 = Ulv(100,30)
ulv3 = Ulv(50, 70)
brett.leggTilObjekt(rodhette)
brett.leggTilObjekt(ulv)
brett.leggTilObjekt(ulv2)
brett.leggTilObjekt(ulv3)

brett.mainloop()