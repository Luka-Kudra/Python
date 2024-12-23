def izdvoj_cifre(broj):
    broj = int(broj)
    cifra1 = broj // 1000
    broj %= 1000
    cifra2 = broj // 100
    broj %= 100
    cifra3 = broj // 10
    broj %= 10
    cifra4 = broj
    return cifra1, cifra2, cifra3, cifra4


def okreni_cifre(broj):
    broj = int(broj)
    cifra4,cifra3,cifra2,cifra1 = izdvoj_cifre(broj)
    return cifra1 * 1000 + cifra2 * 100 + cifra3 * 10 + cifra4


unos = input("Unesite cijeli cetverocifren broj: ")
print("Okrenute cifre unesenog broja", okreni_cifre(unos))

