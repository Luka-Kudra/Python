unos = input("Unesi string: ")
samoglasnik_a = unos.count("a") + unos.count("A")
samoglasnik_e = unos.count("e") + unos.count("E")
samoglasnik_i = unos.count("i") + unos.count("I")
samoglasnik_o = unos.count("o") + unos.count("O")
samoglasnik_u = unos.count("u") + unos.count("U")
broj_samoglasnika = samoglasnik_a + samoglasnik_e + samoglasnik_i + samoglasnik_o + samoglasnik_u
print(broj_samoglasnika)
