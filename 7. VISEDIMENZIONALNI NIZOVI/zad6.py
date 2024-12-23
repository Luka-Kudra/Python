# Napravite program koji omogućava korisniku rezervaciju sjedišta u bioskopu. 
# Bioskop ima 50 sjedišta i prikazan je kao lista listi, gdje svaka unutrašnja lista 
# predstavlja red sjedišta. Svako sjedište je označeno brojem 0 ako je 
# slobodno, odnosno brojem 1 ako je rezervisano. Korisnik treba imati 
# mogućnost rezervisati sjedište po unosu rednog broja reda i kolone. Program 
# treba provjeravati jesu li sjedišta već rezervsana i, ako jesu, treba obavijestiti 
# korisnika da je sjedište već zauzeto i zatražiti unos novih podataka. Nakon 
# svake rezervacije, treba prikazati ažuriranu listu sjedišta. Program treba 
# završiti kada su sva sjedišta rezervirana ili kada korisnik odluči da želi završiti 
# rezervaciju.

def provjera_rezervacije(red, kolona):
    if (not red.isdigit() or not kolona.isdigit()):
        return False
    red = int(red)
    kolona = int(kolona)
    if (red > BR_REDOVA or kolona > BR_SJEDISTA_PO_REDU):
        print("Greska: Neispravan broj reda ili kolone")
        return False
    if (sjedista[red][kolona] == 1):
        print("Sjediste je vec zauzeto")
        return False
    else:
        sjedista[red][kolona] = 1
    return True


def sjedista_puna():
    br_slobodnih_sjedista = 0
    for red in range(BR_REDOVA):
        for sjediste in range(BR_SJEDISTA_PO_REDU):
            if sjediste == 0:
                br_slobodnih_sjedista += 1
    if br_slobodnih_sjedista == 0:
        return True
    return False


sjedista = []

BR_REDOVA = 5
BR_SJEDISTA_PO_REDU = 10

for _ in range(BR_REDOVA):
    sjedista_u_redu = []
    for _ in range(BR_SJEDISTA_PO_REDU):
        sjedista_u_redu.append(0)
    sjedista.append(sjedista_u_redu)

while True:
    print("   ", end = "")
    for indeks_kolone in range(BR_SJEDISTA_PO_REDU):
        print(indeks_kolone, " ", end = "")
            
    print()
    brojac = 0
    for red in sjedista:
        print( brojac, red)
        brojac += 1

    print("\n==== REZERVACIJA sjedista =====")
    signal = " "
    while (signal != ""):
        if(signal == "kraj"):
            exit()
        signal = input("Kliknite \"enter\" da nastavite rezervaciju ili unesite \"kraj\" da izadjete: ")
    print("Unesite broj reda i kolone sjedista koje zelite rezervisati")

    if(sjedista_puna()):
        print("Sva sjedista u bioskopu su zauzeta")
        break
    rezervacija_red = ""
    rezervacija_kolona = ""
    while (not provjera_rezervacije(rezervacija_red, rezervacija_kolona)):
        rezervacija_red = input("[red]: ")
        rezervacija_kolona = input("[kolona]: ")
        