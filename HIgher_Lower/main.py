import random
from podaci import data
from umetnost import *
from fun import *

indikator = True
poeni = 0 
licnost1 = random.choice(data)
licnost2 = random.choice(data)

while indikator:
    
    odgovor = uporedi(licnost1,licnost2)

    lepo_stampanje(licnost1 )
    print()
    lepo_stampanje(licnost2 )

    nagadjanje = pogadjanje(licnost1,licnost2)


    indikator = odgovor == nagadjanje

    if indikator:
        poeni+= 1
        licnost1 = odgovor
        licnost2 = random.choice(data)

print(f"Steta, sakupili ste {poeni}")