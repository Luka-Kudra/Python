import math


def saberi_brojeve(br_1, br_2):
    return br_1 + br_2

def oduzmi_brojeve(br_1, br_2):
    return br_1 - br_2

def pomnozi_brojeve(br_1, br_2):
    return br_1 * br_2

def podijeli_brojeve(br_1, br_2):
    return br_1 / br_2

def stepenuj_broj(br, n = 1):
    return br ** n

def korjenuj_broj(br):
    return math.sqrt(br)


broj_1 = int(input("Broj 1: "))
broj_2 = int(input("Broj 2: "))

print("Sabrana dva broja: ", saberi_brojeve(broj_1, broj_2))
print("Oduzeta dva broja: ", oduzmi_brojeve(broj_1, broj_2))
print("Pomnozena dva broja: ", pomnozi_brojeve(broj_1, broj_2))
print("Podijeljena dva broja: ", podijeli_brojeve(broj_1, broj_2))
print("Stepenovana dva broja prvi na eksponent drugog: ", stepenuj_broj(broj_1, broj_2))
print("Kvadratni korijen prvog broja: ", korjenuj_broj(broj_1))
print("Kvadratni korijen drugog broja: ", korjenuj_broj(broj_2))
