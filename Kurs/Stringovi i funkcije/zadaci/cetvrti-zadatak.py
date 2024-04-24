import math
broj1 = int(input("Unesi prvi broj: "))
broj2 = int(input("Unesi drugi broj: "))

def sabiranje(broj1,broj2):
    zbir = broj1 + broj2
    return zbir
def oduzimanje(broj1,broj2):
    razlika = broj1 - broj2
    return razlika
def mnozenje(broj1,broj2):
    proizvod = broj1 * broj2
    return proizvod
def djeljenje(broj1,broj2):
    kolicnik = broj1 / broj2
    return kolicnik
def stepenovanje(broj1,broj2):
    stepen = broj1 ** broj2
    return stepen
def korjenovanje(broj):
    korjen = math.sqrt(broj)
    return korjen

print(sabiranje(broj1,broj2))
print(oduzimanje(broj1,broj2))
print(mnozenje(broj1,broj2))
print(djeljenje(broj1,broj2))
print(stepenovanje(broj1,broj2))
print(korjenovanje(broj1))
print(korjenovanje(broj2))

