# Napisati program koji od korisnika traži da unese prirodan broj koji predstavlja 
# dužinu niza, a nakon toga zatražiti da unese sve elemente jedan po jedan. 
# Elementi niza su cijeli brojevi. Nakon toga iz datog niza izračunati zasebno 
# dvije sume. Jednu sumu čine samo parni brojevi, a drugu sumu čine samo 
# neparni brojevi iz datog niza. Prikazati na izlaz dobijene sume.

def je_cijeli_broj(broj):
    broj = str(broj)
    if(len(broj) == 0):
        return False
    # Za negativne brojeve
    if(broj[0] == "-"):
        broj = broj[1:]
    # za pozitivne brojeve
    return broj.isdigit()


duzina_niza = ""
while (not duzina_niza.isdigit()):
    duzina_niza = input("Unesite duzinu niza: ")

niz = []

for index in range(int(duzina_niza)):
    element = ""
    while(not je_cijeli_broj(element)):
        print("Unesite ", index, ". element niza: ", sep="", end = "")
        element = input()
    niz.append(int(element))

suma_parnih = 0
suma_neparnih = 0
    
for element in niz:
    if (element % 2 == 0):
        suma_parnih += element
    else:
        suma_neparnih += element

print("Suma parnih:", suma_parnih, "\nSuma neparnih:", suma_neparnih)