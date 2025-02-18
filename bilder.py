import pygame as pg
from constants import *

bakgrunn = pg.image.load("bilder/bakgrunnGress.jpg")
bakgrunn = pg.transform.scale(bakgrunn, SIZE)
rodhette_image = pg.image.load("bilder/rodhette.webp")
rodhette_image = pg.transform.scale(rodhette_image, (50, 100))
ulv_image = pg.image.load("bilder/ulv.png")
ulv_image = pg.transform.scale(ulv_image, (50, 50))
busk_image = pg.image.load("bilder/busk.png")
busk_image = pg.transform.scale(busk_image, (70, 53))
sau_image = pg.image.load("bilder/sau.png")
sau_image = pg.transform.scale(sau_image, (63, 49))
blod_image = pg.image.load("bilder/blod.webp")
blod_image = pg.transform.scale(blod_image, (500, 500))
firework_image = pg.image.load("bilder/firework.webp")
firework_image = pg.transform.scale(firework_image, (500, 500))
bestemor_image = pg.image.load("bilder/bestemor.webp")
bestemor_image = pg.transform.scale(bestemor_image, (50, 90))