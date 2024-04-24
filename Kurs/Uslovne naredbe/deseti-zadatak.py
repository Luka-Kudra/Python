broj_jaja = input("Unesi broj jaja: ")

def provjera_cjelog_broja(unos):
    if unos[0] == '-':
        unos = unos[1:] 
    if unos.isdigit():
        return int(unos)
    else:
        return None
    
broj_jaja = provjera_cjelog_broja(broj_jaja)

if broj_jaja == None:
    print("Niste unijeli broj")

else: 

    broj_kutija = broj_jaja // 12
    if broj_jaja % 12 > 0:
        broj_kutija = broj_kutija + 1
    print("Broj kutija: ",broj_kutija)

    broj_paketa = broj_kutija // 6
    if broj_kutija % 6 > 0:
        broj_paketa = broj_paketa + 1
    print("Broj paketa:", broj_paketa)