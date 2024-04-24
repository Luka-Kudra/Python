broj1 = int(input("Unesi prvi broj: "))
broj2 = int(input("Unesi drugi broj: "))

zbir = broj1 + broj2
razlika = broj1 - broj2
proizvod = broj1 * broj2
kolicnik = broj1 / broj2

def broj_cifara(broj):
    broj = str(abs(broj)) #abs uklanja - kod negativnih brojeva
    if (len(broj) == 3):
        return broj

brojac = 0

if broj_cifara(zbir) != None:
    print("Zbir:",zbir)
else: 
    brojac = brojac + 1
if broj_cifara(razlika) != None:
    print("Razlika:",razlika)
else: 
    brojac = brojac + 1
if broj_cifara(proizvod) != None:
    print("Proizvod:",proizvod)
else: 
    brojac = brojac + 1
if broj_cifara(kolicnik) != None:
    print("Kolicnik:",kolicnik)
else: 
    brojac = brojac + 1

if (brojac >= 4):
    print("Nijedan broj nije trocifren")