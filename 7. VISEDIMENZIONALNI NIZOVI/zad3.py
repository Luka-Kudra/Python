# Napisati program koji kreira dvije matrice dimenzija 3x3 cijelih brojeva čiji se 
# elementi kreiraju pomoću randombiblioteke. Nakon toga u novu matricu 
# smjestiti veći od elemenata kreirane dvije matrice za odgovarajuću poziciju

from random import randint


matrica1 = []
matrica2 = []
for i in range(3):
    red1 = []
    red2 = []
    for j in range(3):
        red1.append(randint(-99,99))
        red2.append(randint(-99,99))
    matrica1.append(red1)
    matrica2.append(red2)

nova_matrica = []

for i in range(3):
    red = []
    for j in range(3):
        if (matrica1[i][j] > matrica2[i][j]):
            red.append(matrica1[i][j])
        else:
            red.append(matrica2[i][j])
    nova_matrica.append(red)

print(matrica1)
print(matrica2)
print("\nRezultat:", nova_matrica)