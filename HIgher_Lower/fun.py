def uporedi(licnost1,licnost2):
    broj1 = licnost1["follower_count"]
    broj2 = licnost2["follower_count"]

    if broj1 > broj2:
        maks = licnost1
    else:
        maks = licnost2

    return maks

def lepo_stampanje(licnost):
    string = " "
    for kljuc in licnost:
        if kljuc != "follower_count":
            if kljuc != "country":
                string = string + licnost[kljuc] + "->"
            else:
                string = string + licnost[kljuc] + "."

    print(string)

def pogadjanje(licnost1,licnost2):
    
    guess = input("Koga birate?-> A za prvu opciju B za drugu    ")

    if guess == "A":
        return licnost1
    elif guess == "B":
        return licnost2
    else:
        print("GRESKA MORONU,REKAO SAM TI KOJA SLOVA")
        exit(0)
    