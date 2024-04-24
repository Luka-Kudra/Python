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
novi_niz = []
for element in niz_elemenata:    
    niz.append(input("Unesi element: "))
    i = element
    if int(niz[i]) > 2:
        novi_niz.append(int(niz[i]) / 2)
    else:
        novi_niz.append(int(niz[i]) * 2)
print("Uneseni niz :",niz)
print("Novi niz: ",novi_niz)


    



