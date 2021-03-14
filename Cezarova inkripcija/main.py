alfabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

putanja = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift):
    nov_text = " "
    
    for slovo in text:
        pozicija = alfabet.index(slovo)
        if pozicija + shift > 25:
            nova_poz = pozicija + shift - 26
        else:
            nova_poz = pozicija + shift  
    
        novo_slovo = alfabet[nova_poz]
   
        nov_text = nov_text + novo_slovo
   
    print(nov_text)

def decrypt(text,shift):
    nov_text = ""
    
    for slovo in text:
        pozicija = alfabet.index(slovo)
        
        if pozicija - shift < 0:
            nova_poz = pozicija - shift + 26
        else:
            nova_poz = pozicija - shift
        
        novo_slovo = alfabet[nova_poz]
        
        nov_text = nov_text + novo_slovo

    print(nov_text)
    # novi_text = [] MOJ KOD

    # for i in range(0,len(alfabet)):
    #     for j in range(0,len(text)):
    #         if alfabet[i] == text[j]:
    #             novi_text.append(alfabet[i + shift])


    # print(f"{''.join(novi_text)}")
if putanja == "encode":
        encrypt(text,shift)
else:
        decrypt(text,shift)   


