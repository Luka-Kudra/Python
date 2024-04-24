def provjera_cjelog_broja():
    while True:
        unos = input("Unesi cjeli broj: ")
        if not unos:
            print("Niste uneli ceo broj")
        elif unos.isdigit() or (unos[0] == '-' and unos[1:].isdigit()):
            return int(unos)
        else:
            print("Niste unjeli ceo broj")
print(" - Prvo ćemo unjeti broj elemenata - ")
granica = provjera_cjelog_broja()
niz = []
niz_elemenata = range(granica)
novi_niz = []
print(" - Sada unosimo elemente - ")
for element in niz_elemenata:    
    niz.append(provjera_cjelog_broja())
    i = element
    if int(niz[i]) > 0:
        novi_niz.append(int(niz[i]))
print(" - Rezultat - ")
print("Uneseni niz :",niz)
print("Novi niz: ",novi_niz)
