def provjera_cjelog_broja():
    while True:
        unos = input("Unesi broj elemenata niza: ")
        if not unos:
            print("Niste uneli ceo broj")
        elif unos.isdigit() or (unos[0] == '-' and unos[1:].isdigit()):
            return int(unos)
        else:
            print("Niste unjeli ceo broj")

granica = provjera_cjelog_broja()
niz = []
niz_elemenata = range(granica)
if granica > 5:
    for element in niz_elemenata:
        niz.append(input("Unesi element: "))
    niz.sort()
    print("Najmanji element niza:", niz[0])
    print("Najveci element niza:", niz[granica-1])
else:
    print("Niz treba imati više od 5 elemenata")



