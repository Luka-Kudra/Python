import math

a = input("a = ")
b = input("b = ")
c = input("c = ")

def provjera_cjelog_broja(unos):
    if unos[0] == '-':
        unos = unos[1:] 
    if unos.isdigit():
        return int(unos)
    else:
        return None

a = provjera_cjelog_broja(a)
b = provjera_cjelog_broja(b)
c = provjera_cjelog_broja(c)

if None in {a, b, c}:
    print("Niste unjeli sve cjele brojeve")
elif a == 0:
    print("Jednacina nema rjesenja")
else:
    D = b**2 - 4 * a * c
    if D < 0:
        print("Rjesenje je kompleksni broj")
    else:
        prvo_rjesenje = (-b + math.sqrt(D)) / (2 * a)
        drugo_rjesenje = (-b - math.sqrt(D)) / (2 * a)
        print("Prvo rjesenje: ",prvo_rjesenje)
        print("Drugo rjesenje: ",drugo_rjesenje)
