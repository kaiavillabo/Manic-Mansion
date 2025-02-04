import pygame as pg
from spillebrett import Spillebrett
from bilder import *
from rodhette import Rodhette
from ulv import Ulv

pg.init()

brett = Spillebrett()

rodhette = Rodhette(200, 100)
ulv = Ulv(0,0)
ulv2 = Ulv(100,30)
brett.leggTilObjekt(rodhette)
brett.leggTilObjekt(ulv)
brett.leggTilObjekt(ulv2)


brett.mainloop()