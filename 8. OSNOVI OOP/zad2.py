# Napisati program koji ima dvije klase Osoba i Mjesto. Klasa mjesto treba da 
# ima mogućnost da evidentira sve osobe koje su rođene u tom mjestu. Takođe 
# treba da ima metode koje ispisuju date osobe, kao i mogućnost pretrage 
# osoba iz tog mjesta prema prezimenu
import random


class Osoba:
    ime = ""
    prezime = ""
    godine = 0

    def ispisi_osobu(self):
        print(self.ime, self.prezime, self.godine)

class Mjesto:
    niz_osoba = []

    def ispisi_sve_osobe(self):
        if len(self.niz_osoba) != 0:
            for osoba in self.niz_osoba:
                osoba.ispisi_osobu()

    def pretrazi_osobu(self, trazeno_prezime):
        if len(self.niz_osoba) != 0:
            for osoba in self.niz_osoba:
                if osoba.prezime == trazeno_prezime:
                    osoba.ispisi_osobu()


banja_luka = Mjesto()
sarajevo = Mjesto()

lista_imena = ["Luka", "Jovan", "Zoran", "Stefan", "Ilija", "Marko", "Nemanja"]
lista_prezimena = ["Stankovic", "Ilic", "Lucic", "Runjajic", "Petrovic", "Smiljic", "Tubic"]
for _ in range(0,8):
    osoba = Osoba()
    osoba.ime = random.choice(lista_imena)
    osoba.prezime = random.choice(lista_prezimena)
    osoba.godine = random.randint(0,100)
    banja_luka.niz_osoba.append(osoba)

banja_luka.ispisi_sve_osobe()
prezime = input("Unesite prezime trazenih osoba: ")
banja_luka.pretrazi_osobu(prezime)