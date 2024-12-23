# Napisati program unutar koga se definiše cjelobrojni niz proizvoljne dužine 
# (koja mora biti veća od 5) i elemenata. Nakon toga je potrebno na izlaz 
# ispisati najmanji i najveći element iz datog niza.
import random

niz = []

for _ in range(random.randint(5,15)):
    niz.append(random.randint(0,100))

najmanji = niz[0]
najveci = niz[0]

for element in niz:
    if (element > najveci):
        najveci = element
    if (element < najmanji):
        najmanji = element

print("Najveci broj je", najveci,"\nNajmanji broj je", najmanji)