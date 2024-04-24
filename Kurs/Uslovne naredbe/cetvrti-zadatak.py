unos = int(input("Unesite dvocifreni cijeli broj: "))

if -99 <= unos <= -10 or 10 <= unos <= 99:
    cifra1 = abs(unos) // 10
    cifra2 = abs(unos) % 10
    if (cifra1>cifra2):
        print(cifra1)
    else:
        print(cifra2)
else:
    print("Pogrešan unos")

