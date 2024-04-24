import random

def kreiranje_matrice(red,kolona):
    matrica = []
    for i in range(red):
        red = []
        for j in range(kolona):
            element = random.randint(0,100)
            red.append(element)
        matrica.append(red)
    return matrica

def sortiranje_matrice(red,kolona,prva_matrica,druga_matrica):
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

prva_matrica = kreiranje_matrice(3,3)
druga_matrica = kreiranje_matrice(3,3)
treca_matrica = sortiranje_matrice(3,3,prva_matrica,druga_matrica)   

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
