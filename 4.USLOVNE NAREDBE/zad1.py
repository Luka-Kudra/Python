korisnik_ulaz = input("Godine starosti: ")
if (not korisnik_ulaz.isdigit()):
    print("POGRESAN UNOS!")
    exit()

korisnik_ulaz = int(korisnik_ulaz)
if (korisnik_ulaz >= 0):
    if (korisnik_ulaz >= 18):
        print("Pristup odobren")
    else:
        print("Pristup zabranjen")
