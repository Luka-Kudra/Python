# Napisati funkciju koja vrši množenje matrice sa skalarnim brojem (množenje 
# matrice nekim skalarnim brojem rezultuje u novu matricu kod koje su svi 
# elementi pomnoženi datim brojem). U glavnom programu od korisnika 
# zatražiti unos dimenzija matrice nakon čega korisnik unosi i sve njene 
# elemente. Poslije toga zatražiti i unos konstante sa kojom se množi. 
# Konstanta i elementi matrice su realni brojevi (provjeriti i obezbjediti korektan 
# unos). U glavnom programu nakon svih unosa prvo ispisati elemente 
# originalne matrice, a nakon poziva funkcije i elemente izmjenjene matrice

def je_realan_broj(broj):
    broj = str(broj)
    # Ako korisnik nije unio nista, vracamo False
    if (len(broj) == 0):
        return False
    # Ako uneseni broj sadrzi jednu tacku, dijelimo ga na dva dijela
    if (broj.count(".") == 1):
        razdvojen_broj = broj.split(".")
        # Ako korisnik nije unio pocetnu cifru prije decimala,
        # podrazumijeva se 0 (npr. ".nn" = "0.nn")
        if (len(razdvojen_broj[0]) == 0):
            razdvojen_broj[0] = "0"
        # Ako je broj negativan, pretvaramo ga u pozitivan uklanjajuci "-"
        if (razdvojen_broj[0][0] == "-"):
            razdvojen_broj[0] = razdvojen_broj[0][1:]
        # Provjeravamo da li su broj ispred i broj iza decimale cifre
        return (razdvojen_broj[0].isdigit() and razdvojen_broj[1].isdigit())
    # Realni brojevi mogu biti i cijeli brojevi (nemaju decimalu)
    elif (broj.count(".") == 0):
        if(broj[0] == "-"):
            broj = broj[1:]
        return broj.isdigit()

    return False


def matrica_pomnozi(matrica, n):
    # Provjera matrice
    for red in matrica:
        for element in red:
            if not je_realan_broj(element):
                print("GRESKA: Nepodrzan sadrzaj matrice")
                return None
    if not je_realan_broj(n):
        print("GRESKA: Neispravan koeficijent")
        return None
    
    rezultat = []
    # prolazi kroz svaki red iz matrice
    for red in matrica:
        # inicijalizujemo varijablu koja ce pamtiti nove vrijednosti reda za novu matricu
        # svaki put ce se resetovati na prazan niz
        red_nove_matrice = []
        # prolazi kroz svaki element reda preko indeksa
        for i in range(len(red)):
            # dodajemo elemente pomnozene sa n u red 
            red_nove_matrice.append(float(red[i]) * float(n))
        # dodajemo red u novu matricu
        rezultat.append(red_nove_matrice)
    return rezultat

  

br_redova = ""
br_kolona = ""
while (not br_redova.isdigit()) or (not br_kolona.isdigit()):
    br_redova = input("Unesite broj redova matrice: ")
    br_kolona = input("Unesite broj kolona matrice: ")

matrica = []

for i in range(int(br_redova)):
    red = []
    for j in range(int(br_kolona)):
        element = input(f"Unesite element na poziciji [{i}][{j}]: ")
        red.append(element)
    matrica.append(red)

koef = input("Unesite koeficijent mnozenja: ")

nova_matrica = matrica_pomnozi(matrica, koef)
print("Original:", matrica)
print("Nova matrica:", nova_matrica)


