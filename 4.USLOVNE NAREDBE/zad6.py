# Napisati program koji od korisnika
# traži unos tri broja koji predstavljaju stranice trougla.
# Ispitati da li je od tih stranica uopšte moguće napraviti trougao,
# a ako jeste ispisati da li je on jednakostraničan, jednakokrak ili raznostraničan.

# **Funkcija vrlo lako moze puci jer nije odradjena provjera
# vrijednosti koje su poslate u nju, ali u glavnom programu je vec izvrsena
# provjera pa nisam htio pisati sigurnu funkciju jer se koristi samo u ovom zadatku**
def moze_biti_trougao(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    if (a == 0 or b == 0 or c == 0):
        return False
    # Uslov koji stranice moraju ispunjavati kako bi mogle biti trougao
    if ((a + b >= c) and (b + c >= a) and (a + c >= b)):
        return True
    return False


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


stranica_a = input("Unesite stranicu a trougla: ")
stranica_b = input("Unesite stranicu b trougla: ")
stranica_c = input("Unesite stranicu c trougla: ")

if (not je_realan_broj(stranica_a) and not je_realan_broj(stranica_b) and not je_realan_broj(stranica_c)):
    print("POGRESAN UNOS!")
    exit()

if (not moze_biti_trougao(stranica_a, stranica_b, stranica_c)):
    print("GRESKA: Ove stranice ne mogu obrazovati trougao!")
    exit()

if ((stranica_a != stranica_b) and (stranica_a != stranica_c) and (stranica_b != stranica_c)):
    print("RAZNOSTRANICAN")
elif ((stranica_a == stranica_b and stranica_a != stranica_c) or
      (stranica_b == stranica_c and stranica_b != stranica_a) or
      (stranica_a == stranica_c and stranica_a != stranica_b)
    ):
    print("JEDNAKOKRAK")
else:
    print("JEDNAKOSTRANICAN")