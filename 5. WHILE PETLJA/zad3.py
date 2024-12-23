# unos jednog prirodnog broja N
# prvih N fibon. brojeva
# Prva dva su 0 i 1, a svaki sljedeci je zbir prethodna dva

broj = ""
while (not broj.isdigit()):
    broj = input("Unesite prirodan broj N: ")

Fib_0 = 0
Fib_1 = 1
brojac = 2  # jer prva dva vec imamo
print(Fib_0)
print(Fib_1)

while (brojac < int(broj)):
    Fib_trenutni = Fib_0 + Fib_1    #tekuci Fib. broj je zbir prethodna dva
    print(Fib_trenutni)
    Fib_0 = Fib_1                   # sada je 0-ti Fib broj dobio vrijednost 1-tog
    Fib_1 = Fib_trenutni            # drugi Fib broj je dobio vrijednost tekuceg
    brojac += 1