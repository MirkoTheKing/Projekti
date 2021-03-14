import random
from funkcije import *


karte = [11,2,3,4,5,6,7,8,9,10,10,10,10]
kompjuter = []
igrac = [] 

kompjuter = random_karte(karte)
igrac = random_karte(karte)


proces(kompjuter,igrac,karte)
