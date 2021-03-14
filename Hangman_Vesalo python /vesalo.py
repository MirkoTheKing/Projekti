import random
import faze
import reci

rec = random.choice(reci.reci)
slova = []
ekran = [] 
zivot = 6
for i in range(0, len(rec)):
    ekran.append("_")

print(f'Rec je : {rec}.')

print(faze.logo)
kraj_igre = False

while not kraj_igre:
    korisnik_slovo = input("Unesite slovo koje zelite da pogodite\n").lower()
    
    if korisnik_slovo in slova:
      print("Samo da znate da ste vec bili uneli ovo slovo!")
    else:
      slova.append(korisnik_slovo)

    for i in range(0,len(rec)):
        if rec[i] == korisnik_slovo:
            ekran[i] = korisnik_slovo
        

    if korisnik_slovo not in rec:
            zivot = zivot - 1
            print("\nOvo slovo nije u reci, probajte opet. P.S. ZIVOT MANJE!!!")
            if zivot == 0:
                kraj_igre = True
                print("Kraj igre, izgubili ste")

    print(f"{' '.join(ekran)}")
    
    if "_" not in ekran:
        kraj_igre = True
        print("Pobeda")            

    

    
    print(faze.faze[zivot])
