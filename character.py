from constants import *
from bilder import *

class Character:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.dy = 0 # horisontal fart
        self.dx = 0 # vertikal fart
        self.image = image
        self.height = self.image.get_height()
        self.width = self.image.get_width()
       

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))