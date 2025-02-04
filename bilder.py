import pygame as pg
from constants import *

bakgrunn = pg.image.load("bilder/bakgrunnGress.jpg")
bakgrunn = pg.transform.scale(bakgrunn, SIZE)
rodhette_image = pg.image.load("bilder/rodhette.webp")
rodhette_image = pg.transform.scale(rodhette_image, (50, 100))
ulv_image = pg.image.load("bilder/ulv.png")
ulv_image = pg.transform.scale(ulv_image, (50, 50))