# Napisati program koji modifikuje elemente niza koji sadrži brojeve i ima 
# proizvoljnu dužinu. Modifikacija koju treba izvršiti je sledeća: ako je element 
# niza veći od granične vrijednosti (koju unosi korisnik) tada treba dati element 
# podijeliti sa 2, a u slučaju da je manji, tada ga treba pomnožiti sa 2. Na izlaz 
# prvo prikazati početni niz, a nakon toga modifikovani.
import random

niz1 = []

for _ in range(random.randint(5,15)):
    niz1.append(random.randint(0,100))

granica = ""
while (not granica.isdigit()):
    granica = input("Unesite granicnu vrijednost: ")

granica = int(granica)
niz2 = []

for element in niz1:
    if (element > granica):
        element = element // 2
        niz2.append(element)
    elif (element < granica):
        element = element * 2
        niz2.append(element)
    else:
        niz2.append(element)

print("Prvobitni niz:", niz1)
print("Modifikovani niz:", niz2)


