# Od korisnika zahtjevati unos dva realna broja koji predstavljaju x i y 
# koordinate tačke. U zavisnosti od unosa ispisati u kom kvadrantu se data 
# tačka nalazi.


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


tacka_x = input("x koordinata tacke: ")
tacka_y = input("y koordinata tacke: ")

if (je_realan_broj(tacka_x) and je_realan_broj(tacka_y)):
    tacka_x = float(tacka_x)
    tacka_y = float(tacka_y)
    if(tacka_x > 0 and tacka_y > 0):
        print("Tacka se nalazi u PRVOM kvadrantu.")
    elif(tacka_x < 0 and tacka_y > 0):
        print("Tacka se nalazi u DRUGOM kvadrantu.")
    elif(tacka_x < 0 and tacka_y < 0):
        print("Tacka se nalazi u TRECEM kvadrantu.")
    elif(tacka_x > 0 and tacka_y < 0):
        print("Tacka se nalazi u CETVRTOM kvadrantu.")
    else:
        print("Tacka NE PRIPADA ni jednom kvadrantu.")
else:
    print("POGRESAN UNOS!")