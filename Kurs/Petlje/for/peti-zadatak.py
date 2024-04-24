def provjera_realnog_broja():
    while True:
        unos = input("Cjena: ")
        if unos.replace('.', '', 1).isdigit():
            return round(float(unos), 2)
        elif unos.startswith('-') and unos[1:].replace('.', '', 1).isdigit():
            return round(float(unos), 2)
        else:
            print("Niste unjeli realan broj")

def uklanjanje_proizvoda(los_proizvod):
    for red in evidencija:
        for element in red:
            if element == los_proizvod:
                evidencija.remove(red)
                return True
    return False

# Napisao sam par proizvoda da prikaz na pocetku nebi bio prazan 
evidencija = [
    ["Banana","10.00"],
    ["Jabuka","8.00"]
] 

print("- Koju komandu zelite? -")
print("Ukoliko zelite prikazati evidenciju upisite 'Prikazi'")
print("Ukoliko zelite dodati proizvod upisite 'Dodaj'")
print("Ukoliko zelite ukloniti proizvod upisite 'Ukloni'")
print("Ukoliko zelite zaustaviti program upisite 'Stop'")

while True:
    unos = input("\nVasa komanda: ")
    print()

    if unos == "Prikazi":
        print("- Lista proizvoda -")
        for red in evidencija:
            for element in red:
                print(element, end= " ")
            print()

    elif unos == "Dodaj":
        novi_proizvod = input("Ime proizvoda: ")
        nova_cjena = provjera_realnog_broja()
        novi_niz = [novi_proizvod,nova_cjena]
        evidencija.append(novi_niz)
        print("Dodali ste novi proizvod")

    elif unos == "Ukloni":
        los_proizvod = input("Ime proizvoda: ")
        if uklanjanje_proizvoda(los_proizvod) == True:
            print("Proizvod je uklonjen")
        else:
            print("Unjeli ste nepostojeci proizvod")
    elif unos == "Stop": 
        break
    else:
        print("Niste unjeli postojecu komandu")