def je_cijeli_broj(broj):
    broj = str(broj)
    if(len(broj) == 0):
        return False
    # Za negativne brojeve
    if(broj[0] == "-"):
        broj = broj[1:]
    # za pozitivne brojeve
    return broj.isdigit()


broj = input("Unesite cijeli broj: ")
while (not je_cijeli_broj(broj)):
    broj = input("Unesite cijeli broj ponovo: ")
print("Ispravan unos")
