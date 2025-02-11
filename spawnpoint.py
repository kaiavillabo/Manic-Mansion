from random import randint
from constants import *

# bestemmer tilfeldige koordinater på spillebrettet som startpunkt for ulvene og plasseringer for buskene
# og sørger for at det er forskjellige steder 

def spawnpoint(antall=6, bredde=WIDTH, hoyde=HEIGHT, margin=50, min_avstand=100): # marginen så de ikke er helt i kanten av brettet 
    koordinater = []

    while len(koordinater) < antall:
        x = randint(FREEZONE + margin, bredde - (FREEZONE + margin))
        y = randint(margin, hoyde - margin)

        if all(abs(x - kx) >= min_avstand or abs(y - ky) >= min_avstand for kx, ky in koordinater):
            koordinater.append((x, y)) 

    return list(koordinater)

print(spawnpoint())