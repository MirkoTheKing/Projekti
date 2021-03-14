def saberi(n1,n2):
    return n1+ n2

def oduzmi(n1,n2):
    return n1 - n2

def pomnozi(n1,n2):
    return n1 * n2

def podeli(n1,n2):
    return n1 / n2

spisak = {
    "+" : saberi , 
    "-" : oduzmi ,
    "*" : pomnozi , 
    "/" : podeli
}

broj1 = int(input("Unesite prvi broj "))



for simbol in spisak:
    print(simbol)

operacija = input("Izaberite jednu od operacija iznad! ")

broj2 = int(input("Unesite durig broj "))

odgovor = spisak[operacija]

print(odgovor(broj1,broj2))


