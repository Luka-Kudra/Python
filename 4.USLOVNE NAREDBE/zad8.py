# Napisati funkciju koja prima jedan argument tipa string. Ova funkcija treba da 
# provjeri da li je dati argument realan broj i da na izlaz vrati True ako jeste, a 
# ako nije vraća False. Verifikovati rad funkcije u glavnom programu, tražeći od 
# korisnika unos nakon čega se poziva funkcija i prikazuje rezultat njenog 
# izvršavanja.


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

a = input("Unesite realan broj: ")
print(je_realan_broj(a))