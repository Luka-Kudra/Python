unos = input("Unesi četvorocifren cjeli broj: ")

def zamjena_mjesta(unos):
    cifra1 = unos[3]
    cifra2 = unos[2]
    cifra3 = unos[1]
    cifra4 = unos[0]
    obrnut_broj = cifra1 + cifra2 + cifra3 + cifra4
    return obrnut_broj

print(zamjena_mjesta(unos))