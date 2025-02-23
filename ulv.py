from constants import *
from bilder import *
from character import Character

class Ulv(Character):
    def __init__(self, x, y):
        super().__init__(x, y, ulv_image)
        self.dx = ULV_SPEED
        self.dy = ULV_SPEED
        self.is_bestemor = False

    def update(self, busker):
        super().move()

        if self.x <= FREEZONE or self.x >= ((WIDTH-FREEZONE) - self.width):
            self.dx = -self.dx  

        # sjekk kollisjon med kantene
        if self.y <= 0 or self.y >= (HEIGHT - self.height):
            self.dy = -self.dy

        for busk in busker:
            if self.kolliderer_med(busk):  
                # hvis kollisjon skjer, snu retning på ulven
                if self.x < busk.x or self.x + self.width > busk.x + busk.width:
                    self.dx = -self.dx  # snu horisontal retning hvis kollisjon på x
                if self.y < busk.y or self.y + self.height > busk.y + busk.height:
                    self.dy = -self.dy  # snu vertikal retning hvis kollisjon på y

    def kolliderer_med(self, busk): # aabb kollisjonssjekk
        return (
            self.x < busk.x + busk.width and
            self.x + self.width > busk.x and
            self.y < busk.y + busk.height and
            self.y + self.height > busk.y
        )
    
    def toggle_bestemor(self):
        # bytter mellom ulv og bestemor bilde
        if self.is_bestemor:
            self.image = ulv_image
        else:
            self.image = bestemor_image
        self.is_bestemor = not self.is_bestemor