korisnik_unos = input("Unesite neki tekst: ")

broj_samoglasnika = (
                        korisnik_unos.count("a") + korisnik_unos.count("e")
                        + korisnik_unos.count("i") + korisnik_unos.count("o") + korisnik_unos.count("u")
                        + korisnik_unos.count("A") + korisnik_unos.count("E")
                        + korisnik_unos.count("I") + korisnik_unos.count("O") + korisnik_unos.count("U")
                    )


print("U tekstu ima", broj_samoglasnika, "samoglansika")