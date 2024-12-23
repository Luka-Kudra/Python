# Učitati dva cijela broja i izračunati njihov zbir, proizvod, razliku i količnik. Na 
# izlaz prikazati svaki od ovih rezultata koji je trocifren,  ako nema niti jednog 
# onda ispisati da nema trocifrenih rezultata


def je_cijeli_broj(broj):
    broj = str(broj)
    if(len(broj) == 0):
        return False
    # Za negativne brojeve
    if(broj[0] == "-"):
        broj = broj[1:]
    # za pozitivne brojeve
    return broj.isdigit()


def je_Ntocifren(broj, n):
    broj = str(broj)
    if (je_cijeli_broj(broj)):
        broj = broj.removeprefix("-")
        if (len(broj) == n):
            return True

    return False
    

broj1 = input("Prvi broj: ")
broj2 = input("Drugi broj: ")

if (je_cijeli_broj(broj1) and je_cijeli_broj(broj2)):
    broj1 = int(broj1)
    broj2 = int(broj2)

    zbir = broj1 + broj2
    proizvod = broj1 * broj2
    razlika = broj1 - broj2
    ima_trocifrenih_rez = False

    if(je_Ntocifren(zbir, 3)):
        print("Zbir =", zbir)
        ima_trocifrenih_rez = True
    if(je_Ntocifren(proizvod, 3)):
        print("Proizvod =", proizvod)
        ima_trocifrenih_rez = True
    if(je_Ntocifren(razlika, 3)):
        print("Razlika =", razlika)
        ima_trocifrenih_rez = True

    if (broj2 != 0):
        kolicnik = broj1 // broj2
        if(je_Ntocifren(kolicnik, 3)):
            print("Kolicnik =", kolicnik)
            ima_trocifrenih_rez = True

    if (not ima_trocifrenih_rez):
        print("Nema trocifrenih rezultata.")
else:
    print("POGRESAN UNOS!")