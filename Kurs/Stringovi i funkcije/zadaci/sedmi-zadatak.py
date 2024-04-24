unos = input("Unesi trocifren cjeli broj: ")

def razdvajanje_cifara(unos):
    cifra1 = int(unos[0])
    cifra2 = int(unos[1])
    cifra3 = int(unos[2])
    return cifra1,cifra2,cifra3

cifra1,cifra2,cifra3 = razdvajanje_cifara(unos)
zbir_cifara = cifra1 + cifra2 + cifra3
print("Zbir cifara je:",zbir_cifara)
