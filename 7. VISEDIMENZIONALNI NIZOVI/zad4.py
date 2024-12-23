# Implementirati funkciju koja vrši sabiranje dvije matrice. Unutar funkcije provjeriti 
# da li je moguće izvšiti sabiranje (mogu se sabirati samo matrice istih dimenzija) i 
# ako nije vratiti None. U glavnom programu od korisnika tražiti unos dimenzija 
# matrice i njenih elemenata (cijeli brojevi, provjeriti i obezbjediti korektan unos) i 
# testirati funkciju. Rezultat sabiranja ispisati na izlaz.

def je_cijeli_broj(broj):
    broj = str(broj)
    if(len(broj) == 0):
        return False
    # Za negativne brojeve
    if(broj[0] == "-"):
        broj = broj[1:]
    # za pozitivne brojeve
    return broj.isdigit()


def matrica_saberi(matrica1, matrica2):
    if (len(matrica1) == 0 or len(matrica2) == 0):
        print("GRESKA: Pogresna dimenzija matrice")
        return None
    if (len(matrica1) != len(matrica2)) or (len(matrica1[0]) != len(matrica2[0])):
        print("GRESKA: Matrice nisu iste dimenzije")
        return None
    for i in range(len(matrica1)):
        for j in range(len(matrica1[i])):
            if (not je_cijeli_broj(matrica1[i][j])) or (not je_cijeli_broj(matrica2[i][j])):
                print("GRESKA: Nepodrzan sadrzaj matrice")
                return None

    rezultat = []
    for i in range(len(matrica1)):
        red = []
        for j in range(len(matrica1[i])):
            red.append(int(matrica1[i][j]) + int(matrica2[i][j]))
        rezultat.append(red)
    return rezultat


def matrica_unos():
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

    return matrica


print("Unos prve matrice")
matrica1  = matrica_unos()
print("Unos druge matrice")
matrica2 =  matrica_unos()

print(matrica1)
print(matrica2)
sabrana = matrica_saberi(matrica1, matrica2)
print("Sabrana matrica:", sabrana)