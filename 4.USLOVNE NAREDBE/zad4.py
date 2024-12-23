# Napisati program koji od korisnika 
# traži unos dvocifrenog cijelog broja. 
# Provjeriti da li je broj dvocifren , i ako jeste
# ispisati veću od njegovih cifara na izlaz

def je_cijeli_broj(broj):
    broj = str(broj)
    if(len(broj) == 0):
        return False
    # Za negativne brojeve
    if(broj[0] == "-"):
        broj = broj[1:]
    # za pozitivne brojeve
    return broj.isdigit()


def je_Ntocifren(broj, n):
    broj = str(broj)
    if (je_cijeli_broj(broj)):
        broj = broj.removeprefix("-")
        if (len(broj) == n):
            return True

    return False
        

broj1 = input("Unesite prvi broj: ")
broj2 = input("Unesite drugi broj: ")

if (not je_cijeli_broj(broj1) or not je_cijeli_broj(broj2)):
    print("POGRESAN UNOS!")
    exit()

if (not je_Ntocifren(broj1, 2) or not je_Ntocifren(broj2, 2)):
    print("BROJEVI NISU DVOCIFRENI!")
    exit()

broj1 = abs(int(broj1))
broj2 = abs(int(broj2))

# Inicijalizujemo da veca cifra bude prva cifra za oba broja
# 24 // 10 = 2, a 24 % 10 = 4
veca_cifra1 = broj1 // 10
veca_cifra2 = broj2 // 10

# Ako je druga cifra veca od nase inicijalne, uzimamo vrijednost druge
if (broj1 % 10 > veca_cifra1):
    veca_cifra1 = broj1 % 10
if (broj2 % 10 > veca_cifra2):
    veca_cifra2 = broj2 % 10

print("Veca cifra od prvog broja je:", veca_cifra1)
print("Veca cifra od drugog broja je:", veca_cifra2)