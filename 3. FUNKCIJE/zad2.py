def informacije_o_stringu(s1,s2,s3,s4):
    spojena = s1.capitalize() + " " + s2 + " " + s3 + " " + s4 + "."
    br_znakova = len(spojena)
    br_samoglasnika = izbroj_samoglasnike(spojena)
    return spojena,br_znakova,br_samoglasnika

    
def izbroj_samoglasnike(korisnik_unos):
     return (
                  korisnik_unos.count("a")
                + korisnik_unos.count("e")
                + korisnik_unos.count("i")
                + korisnik_unos.count("o")
                + korisnik_unos.count("u")
                + korisnik_unos.count("A")
                + korisnik_unos.count("E")
                + korisnik_unos.count("I")
                + korisnik_unos.count("O")
                + korisnik_unos.count("U")
            )

# main()
string_1 = input("String 1: ")
string_2 = input("String 2: ")
string_3 = input("String 3: ")
string_4 = input("String 4: ")

spojena, br_znakova, br_samoglasnika = informacije_o_stringu(string_1, string_2, string_3, string_4)
print("Spojena recenica:", spojena)
print("Broj znakova u recenici:", br_znakova)
print("Broj samoglasnika:", br_samoglasnika)