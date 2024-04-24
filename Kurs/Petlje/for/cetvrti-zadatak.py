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
parna_suma = 0
neparna_suma = 0
print(" - Sada unosimo elemente - ")
for element in niz_elemenata:    
    niz.append(provjera_cjelog_broja())
    i = element
    if ((int(niz[i])) % 2 == 0):
        parna_suma = parna_suma + int(niz[i])
    else:
        neparna_suma = neparna_suma + int(niz[i])
print(" - Rezultat - ")
print("Parna suma: ",parna_suma)
print("Neparna suma: ",neparna_suma)
