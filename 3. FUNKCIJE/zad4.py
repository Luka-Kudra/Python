def izdvoj_cifre(broj):
    broj = int(broj)
    cifra1 = broj // 100
    broj %= 100
    cifra2 = broj // 10
    broj %= 10
    cifra3 = broj
    return cifra1, cifra2, cifra3


broj = input("Unesite trocifren broj: ")
broj_cifra1,broj_cifra2,broj_cifra3 = izdvoj_cifre(broj)
print("Zbir cifara broja:", (broj_cifra1 + broj_cifra2 + broj_cifra3))