def provjera_cjelog_broja():
    while True:
        unos = input("Unesi cjeli broj: ")
        if not unos:
            print("Niste unjeli ceo broj")
        elif unos.isdigit() or (unos[0] == '-' and unos[1:].isdigit()):
            return int(unos)
        else:
            print("Niste unjeli ceo broj")

unos = provjera_cjelog_broja()

broj1 = 0
broj2 = 1
broj3 = 0

brojac = 2

if unos == 0:
    print("Trazeni broj je:",broj1)
elif unos == 1:
    print("Trazeni broj je:",broj2)
else:
    while brojac <= unos:
        if brojac == 0:
            print(broj1)
            print(broj2)
        broj3 = broj1 + broj2
        broj1 = broj2
        broj2 = broj3
        brojac += 1
    print("Trazeni broj je:",broj3)

#ovaj zadatak sam na brzinu uradio na casu kada smo bili i kasnije i zaboravio na njega,zato nije bio savrsen