# Napisati program koji
# računa rješenja kvadratne jednačine ax^2+bx+c. 
# Koeficijenti a, b i c su cijeli brojevi koje unosi korisnik. Program može da 
# pronađe samo realna rješenja, u slučaju da su rješenja kompleksna, na izlaz 
# javiti grešku. 

from math import sqrt


def je_cijeli_broj(broj):
    broj = str(broj)
    if(len(broj) == 0):
        return False
    # Za negativne brojeve
    if(broj[0] == "-"):
        broj = broj[1:]
    # za pozitivne brojeve
    return broj.isdigit()


def je_realan_broj(broj):
    broj = str(broj)
    # Ako korisnik nije unio nista, vracamo False
    if (len(broj) == 0):
        return False
    # Ako uneseni broj sadrzi jednu tacku, dijelimo ga na dva dijela
    if (broj.count(".") == 1):
        razdvojen_broj = broj.split(".")
        # Ako korisnik nije unio pocetnu cifru prije decimala,
        # podrazumijeva se 0 (npr. ".nn" = "0.nn")
        if (len(razdvojen_broj[0]) == 0):
            razdvojen_broj[0] = "0"
        # Ako je broj negativan, pretvaramo ga u pozitivan uklanjajuci "-"
        if (razdvojen_broj[0][0] == "-"):
            razdvojen_broj[0] = razdvojen_broj[0][1:]
        # Provjeravamo da li su broj ispred i broj iza decimale cifre
        return (razdvojen_broj[0].isdigit() and razdvojen_broj[1].isdigit())
    # Realni brojevi mogu biti i cijeli brojevi (nemaju decimalu)
    elif (broj.count(".") == 0):
        if(broj[0] == "-"):
            broj = broj[1:]
        return broj.isdigit()

    return False


print("=== Unos koeficijenata kvadratne jednacine ===")
a = input("a = ")
b = input("b = ")
c = input("c = ")

if (not je_cijeli_broj(a) or not je_cijeli_broj(b) or not je_cijeli_broj(c)):
    print("GRESKA: Pogresan unos!")
    exit()

a = int(a)
b = int(b)
c = int(c)

# Privremena varijabla kako bi izvrsili provjeru
# jer sqrt() vraca ValueError ako je broj negativan
D_kv_temp = pow(b,2) - (4 * a * c)

if (D_kv_temp < 0):
    print("GRESKA: Rjesenje je kompleksno")
    exit()

D = sqrt(D_kv_temp)

rezultat1 = (-b + D) / (2 * a)
rezultat2 = (-b - D) / (2 * a)

if (je_realan_broj(rezultat1) and je_realan_broj(rezultat2)):
    # ako je D = 0
    if (rezultat1 == rezultat2):
        print("x =", rezultat1)
    else:
        print("x1 =", rezultat1)
        print("x2 =", rezultat2)
