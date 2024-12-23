# Napisati program koji od korisnika
# traži unos tri broja, a zatim ih
# ispisuje u rastućem redoslijedu (od najmanjeg ka najvećem)


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


broj1 = input("Unesite prvi broj: ")
broj2 = input("Unesite drugi broj: ")
broj3 = input("Unesite treci broj: ")

if (je_realan_broj(broj1) and je_realan_broj(broj2) and je_realan_broj(broj3)):
    broj1 = float(broj1)
    broj2 = float(broj2)
    broj3 = float(broj3)
else:
    print("POGRESAN UNOS!")
    exit()

najveci_broj = broj1
najmanji_broj = broj1
srednji_broj = broj1

if(najveci_broj < broj2):
    najveci_broj = broj2
if(najveci_broj < broj3):
    najveci_broj = broj3

if(broj2 < najmanji_broj):
    najmanji_broj = broj2
if(broj3 < najmanji_broj):
    najmanji_broj = broj3

if(najmanji_broj < broj2 < najveci_broj):
    srednji_broj = broj2
if(najmanji_broj < broj3 < najveci_broj):
    srednji_broj = broj3

print(najmanji_broj,srednji_broj,najveci_broj, sep = "\n")