# Implementirati funkciju koja vrši množenje dvije matrice. Unutar funkcije provjeriti 
# da li je moguće izvšiti množenje (matrice se mnogu množiti ako je broj kolona prve 
# jednak broju redova druge matrice) i ako nije vratiti None. U glavnom programu od 
# korisnika tražiti unos dimenzija matrice i njenih elemenata (cijeli brojevi, provjeriti i 
# obezbjediti korektan unos) i testirati funkciju. Rezultat množenjaispisati na izlaz.

def je_cijeli_broj(broj):
    broj = str(broj)
    if(len(broj) == 0):
        return False
    # Za negativne brojeve
    if(broj[0] == "-"):
        broj = broj[1:]
    # za pozitivne brojeve
    return broj.isdigit()

    
def matrica_pomnozi(matrica1, matrica2):
    if ((len(matrica1) <= 0 or len(matrica2) <= 0) or
        (len(matrica1) != len(matrica2[0])) or
        (len(matrica1[0]) != len(matrica2))):
        print("GRESKA: Matrice nisu potrebne dimenzije")
        return None
    for red in matrica1:
        for element in red:
            if (not je_cijeli_broj(element)):
                print("GRESKA: Nepodrzan sadrzaj matrice")
                return None
    for red in matrica2:
        for element in red:
            if (not je_cijeli_broj(element)):
                print("GRESKA: Nepodrzan sadrzaj matrice")
                return None
      
    rezultat = []
    # indeks i iterira kroz broj redova prve matrice
    for i in range(len(matrica1)):
        # varijabla u koju smjestamo niz vrijednosti kao red rezultantne matrice
        red = []
        # j petlja iterira kroz kolone u drugoj matrici
        for j in range(len(matrica2[0])):
            zbir_pomnozenih_elemenata = 0
            # k iterira kroz kolone (elemente reda) u prvoj matrici
            for k in range(len(matrica1[0])):
                # prolazimo kroz elemente u redu prve matrice i mnozimo sa elementima kolone druge matrice
                zbir_pomnozenih_elemenata += int(matrica1[i][k]) * int(matrica2[k][j])
            red.append(zbir_pomnozenih_elemenata)
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
pomnozena = matrica_pomnozi(matrica1, matrica2)
print("Pomnozena matrica:", pomnozena)