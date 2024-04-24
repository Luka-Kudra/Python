def provjera_cjelog_broja():
    while True:
        unos = input()
        if not unos:
            print("Niste uneli ceo broj")
            print("Pokusajte ponovo:",end = " ")
        elif unos.isdigit() or (unos[0] == '-' and unos[1:].isdigit()):
            return int(unos)
        else:
            print("Niste unjeli ceo broj")
            print("Pokusajte ponovo:",end = " ")

def kreiranje_matrice(red,kolona):
    matrica = []
    for i in range(red):
        red = []
        for j in range(kolona):
            print("Unesi element za",i+1,"red i",j+1,"kolonu:",end = " ")
            element = provjera_cjelog_broja()
            red.append(element)
        matrica.append(red)
    return matrica

def ispis_elemenata_matrice(matrica,srednja_vrijednost):
    for i in range(len(matrica)):
        for j in range(len(matrica)):
            if matrica[i][j] > srednja_vrijednost:
                print("Broj",matrica[i][j],"u",i+1,"redu i u",j+1,"koloni")

red = int(input("Unesi broj redova matrice: "))
kolona = int(input("Unesi broj kolona matrice: "))
print() #pravi samo novi red

matrica = kreiranje_matrice(red,kolona)

zbir_elemenata = 0
for i in range(len(matrica)):
    for j in range(len(matrica)):
        zbir_elemenata += matrica[i][j]
srednja_vrijednost = zbir_elemenata / (red * kolona)

print("\nSrednja vrijednost je:",srednja_vrijednost)
print("\nBrojevi veci od srednje vrijednosti su:")
ispis_elemenata_matrice(matrica,srednja_vrijednost)

