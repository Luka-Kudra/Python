# Napisati funkciju koja prima jedan argument tipa string. Ova funkcija treba da 
# provjeri da li je dati argument cijeli broj i da na izlaz vrati True ako jeste, a 
# ako nije vraća False. Verifikovati rad funkcije u glavnom programu, tražeći od 
# korisnika unos nakon čega se poziva funkcija i prikazuje rezultat njenog 
# izvršavanja.

def je_cijeli_broj(broj):
    broj = str(broj)
    if(len(broj) == 0):
        return False
    # Za negativne brojeve
    if(broj[0] == "-"):
        broj = broj[1:]
    # za pozitivne brojeve
    return broj.isdigit()

broj = input("Unesite cijeli broj: ")

print(je_cijeli_broj(broj))