import random

def provjera_realnog_broja():
    while True:
        unos = input()
        if unos.replace('.', '', 1).isdigit():
            return round(float(unos), 2) 
        elif unos.startswith('-') and unos[1:].replace('.', '', 1).isdigit():
            return round(float(unos), 2)
        else:
            print("Niste unjeli realan broj")
            print("Pokusajte ponovo:",end=" ")

def kreiranje_matrice(red,kolona):
    matrica = []
    for i in range(red):
        red = []
        for j in range(kolona):
            print("Unesi element za",i+1,"red i",j+1,"kolonu:",end = " ")
            element = provjera_realnog_broja()
            red.append(element)
        matrica.append(red)
    return matrica



def sabiranje_matrice(red,kolona,prva_matrica,druga_matrica):
    matrica = []
    for i in range(red):
        red = []
        for j in range(kolona):
            if prva_matrica[i][j] > druga_matrica[i][j]:
                element = prva_matrica[i][j]
            else:
                element = druga_matrica[i][j]
            red.append(element)
        matrica.append(red)
    return matrica

matrica1_redovi = int(input("Unesi broj redova prve matrice: "))
matrica1_kolone = int(input("Unesi broj kolona prve matrice: "))
matrica2_redovi = int(input("Unesi broj redova druge matrice: "))
matrica2_kolone = int(input("Unesi broj kolona druge matrice: "))
print() #pravi samo novi red
if (matrica1_kolone and matrica1_redovi) == (matrica2_kolone and matrica2_redovi):
    prva_matrica = kreiranje_matrice(matrica1_redovi,matrica1_kolone)
    druga_matrica = kreiranje_matrice(matrica2_redovi,matrica2_kolone)
    treca_matrica = sabiranje_matrice(matrica1_redovi,matrica2_kolone,prva_matrica,druga_matrica)   

    print("Prva matrica")
    for red in prva_matrica:
            print(red)
    print()

    print("Druga matrica")
    for red in druga_matrica:
        print(red)
    print()

    print("Treca matrica")
    for red in treca_matrica:
        print(red)
else:
    print("Niste unjeli 2 iste matrice")
