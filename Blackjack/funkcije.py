import random

def suma(niz):
    suma = 0
    for i in range(0,len(niz)):
        suma += niz[i]
    return suma

def random_karte(niz):
    nov = [] 
    for i in range(0,2):
        nov.append(random.choice(niz))

    return nov 

def provera_black_jack(niz):
    if 11 in niz and 10 in niz:
        return True
    return False


def proces(kompjuter,igrac,karte):
    
    odgovor = "da"
    

    while odgovor == "da":    
        suma_igrac = suma(igrac)

        if provera_black_jack(kompjuter):
            print("Kompjuter pobedio")
            return
        elif provera_black_jack(igrac):
            print("Igrac pobedio")
            return

        if suma_igrac > 21:
            if 11 in igrac:
                if suma_igrac - 10 > 21:
                    print("Kompjuter pobedio")
                    return
                else:
                    for i in range(0,len(igrac)):
                        if igrac[i] == 11:
                            igrac[i] = 1
                            suma_igrac = suma(igrac)
                            break 
            else:
                print("Kompjuter pobedio")
                return
        elif suma_igrac <=21:
            
            print(f"Igrac: {igrac}")
            print(f"Diler : {kompjuter[0]} , _")
            odgovor = input("Da li zelite da vucete kartu? ").lower()
            
            if odgovor == "da":
                igrac.append(random.choice(karte))
                print(igrac)
                print(kompjuter)

    while suma(kompjuter) < 17:
        kompjuter.append(random.choice(karte))
        print(f"Kompjuter: {kompjuter}")

    
    if suma(kompjuter) > 21:
        print("Igrac pobedio")
        return


    if suma(kompjuter) > suma(igrac):
        print("Kompjuter pobedio")
        return
    elif suma(kompjuter) < suma(igrac):
        print("Igrac pobedio")
        return
    else:
        print("Izjednaceno")
        return
    
    print(igrac)
    print(kompjuter)