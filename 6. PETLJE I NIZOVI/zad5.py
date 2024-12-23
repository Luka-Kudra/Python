# Napisati program koji služi za vođenje evidencije o proizvodima unutar 
# prodavnice voća i povrća. Proizvod je definisan nazivom proizvoda i 
# njegovom cijenom po kilogramu. Korisniku omogućiti meni koji će se uvijek 
# prikazivati (osim u slučaju gašenja terminala) i koji će mu nuditi sledeće 
# opcije:
        # ■ Prikaz svih proizvoda i njihove cijene po kg
        # ■ Dodavanje novog proizvoda
        # ■ Uklanjanje postojećeg proizvoda (ako se proba uklanjanje nepostojećeg proizvoda na 
        # izlazu obavijesiti o grešci)
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


proizvodi = []
cijene = []

while True:
    print("\n===== PRODAVNICA =====")
    print("Unesite \"1\" za ispis proizvoda")
    print("Unesite \"2\" za dodavanje novog proizvoda")
    print("Unesite \"3\" za uklanjanje postojeceg proizvoda")

    opcija = input(":")
    print("========================")
    match(opcija):
        case "1":
            if (len(proizvodi) == 0):
                    print("Nemate proizvoda u prodavnici.")
                    continue
            print("\nProizvod : Cijena po kg")
            for index in range(len(proizvodi)):
                print(proizvodi[index], ":", cijene[index])
        case "2":
            print("Unos novog proizvoda\n")
            naziv = input("Naziv: ")
            while (naziv in proizvodi):
                print("Taj proizvod vec postoji!")
                naziv = input("Naziv: ")
            cijena = ""
            while (not je_realan_broj(cijena)):
                cijena = input("Cijena: ")
            proizvodi.append(naziv)
            cijene.append(cijena)
        case "3":
            if (len(proizvodi) == 0):
                    print("Nemate proizvoda u prodavnici.")
                    continue
            print("Uklanjanje proizvoda\n")
            naziv = input("Unesite naziv proizvoda koji zelite ukloniti: ")
            while (naziv not in proizvodi):
                print("Taj proizvod ne postoji!")
                naziv = input("Unesite naziv proizvoda koji zelite ukloniti: ")
            index = proizvodi.index(naziv)
            proizvodi.pop(index)
            cijene.pop(index)
        case _ :
            continue
            
