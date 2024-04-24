str1 = input("Prvi string: ")
str2 = input("Drugi string: ")
str3 = input("Treci string: ")
str4 = input("Cetvrti string: ")

def ispis(str1,str2,str3,str4):
    recenica = str1.capitalize() + " " + str2 + " " + str3 + " " + str4 + "."
    duzina = len(recenica)
    samoglasnik = samoglasnici(recenica)
    return recenica,duzina,samoglasnik

def samoglasnici(unos):
    samoglasnik_a = unos.count("a") + unos.count("A")
    samoglasnik_e = unos.count("e") + unos.count("E")
    samoglasnik_i = unos.count("i") + unos.count("I")
    samoglasnik_o = unos.count("o") + unos.count("O")
    samoglasnik_u = unos.count("u") + unos.count("U")
    broj_samoglasnika = samoglasnik_a + samoglasnik_e + samoglasnik_i + samoglasnik_o + samoglasnik_u
    return broj_samoglasnika

recenica,duzina,samoglasnik = ispis(str1,str2,str3,str4)
print(recenica)
print("Broj znakova u recenici: ",duzina)
print("Broj samoglasnika u recenici: ",samoglasnik)