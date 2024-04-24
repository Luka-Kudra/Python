import random

print("Dobrodošli u igru pogadjanja! ")
print("Zamisli broj izmedju 1 i 100")
a = input("Pritisni bilo koji taster kada zamislis broj")

nivo = input("Koji nivo igrice zelite: ")

if nivo == "1":
    for i in range(10):
        pokusaj = random.randint(1,100)
        print("Da li ste zamislili", pokusaj, "?")
        odgovor = input("Da li sam pogodio broj?")
        if odgovor == "D":
            break
if nivo == "2":
    donja_granica = 1
    gornja_granica = 100
    for i in range(10):
        pokusaj = random.randint(donja_granica,gornja_granica)
        print("Da li ste zamislili", pokusaj, "?")
        odgovor = input("Da li sam pogodio broj? (Da,M,V)")
        if odgovor == "Da":
            print("Pogodio si")
            break
        elif odgovor == "M":
            gornja_granica = pokusaj - 1
        elif odgovor == "V": 
            donja_granica = pokusaj - 1
if nivo == "3":
    donja_granica = 1
    gornja_granica = 100
    for i in range(10):
        pokusaj = (donja_granica + gornja_granica) // 2
        print("Da li ste zamislili", pokusaj, "?")
        odgovor = input("Da li sam pogodio broj? (Da,M,V)")
        if odgovor == "Da":
            print("Pogodio si")
            break
        elif odgovor == "M":
            gornja_granica = pokusaj - 1
        elif odgovor == "V": 
            donja_granica = pokusaj - 1