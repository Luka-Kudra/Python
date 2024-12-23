# Napisati program koji od korisnika traži unos dimenzija matrice i njenih 
# elemenata (cijeli brojevi, provjeriti i obezbjediti korektan unos). Nakon toga 
# pronaći srednju vrijednost svih elemenata matrice, te na izlaz ispisati samo 
# one elemente matrice koji su veći od te srednje vrijednosti. Pored samog 
# elementa ispisati i poziciju na kome se on nalazi u matrici (red i kolona)

def je_cijeli_broj(broj):
    broj = str(broj)
    if(len(broj) == 0):
        return False
    # Za negativne brojeve
    if(broj[0] == "-"):
        broj = broj[1:]
    # za pozitivne brojeve
    return broj.isdigit()


# ucitavanje matrice
br_redova = ""
br_kolona = ""
while (not br_redova.isdigit()) or (not br_kolona.isdigit()):
    br_redova = input("Unesite broj redova matrice: ")
    br_kolona = input("Unesite broj kolona matrice: ")

matrica = []

print("Unesite elemente (cijele brojeve)")
for i in range(int(br_redova)):
    red = []
    for j in range(int(br_kolona)):
        element = ""
        while (not je_cijeli_broj(element)):
            element = input(f"Element [{i}][{j}]: ")
        red.append(element)
    matrica.append(red)

# Srednja vrijednost elemenata
suma = 0
srednja_vr = 0
for red in matrica:
    for element in red:
        suma += int(element)

srednja_vr = suma / (int(br_kolona) * int(br_redova))

# ispis
for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        if int(matrica[i][j]) > srednja_vr:
            print(matrica[i][j],f"na poziciji [{i}][{j}]")
