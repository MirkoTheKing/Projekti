from umetnost import logo

kupci = []
potvrda =  input("Da li zelite da dodate kupca?").lower()

kupac = {}

print(logo)

while potvrda == "da":
    
    ime = input("Unesite ime kupca ")
    
    cena = int(input("Unesite cenu kupca"))
    
    kupac[ime] = cena

    kupci.append(kupac)

    potvrda =  input("Da li zelite da dodate kupca?").lower()

maks = kupci[0][0]

for i in range(1,len(kupci)):
    if maks < kupci[i][0]:
        maks = kupci[i]


print(maks)
    
    
