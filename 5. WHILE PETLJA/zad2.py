# Unos prirodnog broja
# Faktorijel tog broja
# Sumu svih prirodnih od 1 do unesenog

broj = ""
while(not broj.isdigit()):
    broj = input("Unesite prirodan broj: ")

brojac = 1
faktoriel = 1
suma = 0
while (brojac <= int(broj)):
    faktoriel *= brojac
    suma += brojac
    brojac += 1
print("Fakt: ", faktoriel)
print("Suma:", suma)