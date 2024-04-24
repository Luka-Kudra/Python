import random
broj = random.randint(1,100)
print("Zamislio sam broj, pokusaj pogoditi")

for broj_pokusaja in range(10):
    pokusaj = int(input("Unesi broj: "))
    if pokusaj < broj:
        print("Zamislio sam veci broj")
    elif pokusaj > broj:
        print("Zamislio sam manji broj")
    else:
        print("Pogodio si broj")
        break
