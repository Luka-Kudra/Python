unos = input("Unesi realni broj: ")

def provjera_realnog_broja(unos):
    if len(unos) <= 0:
        return False
    if unos[0] == '-':
        unos = unos[1:]
    if unos.count(".") == 1:
        ispred_zareza,iza_zareza = unos.split(".")
        if ispred_zareza.isdigit() and iza_zareza.isdigit():
           return True
        else: 
            return False
    else:
        return False
   
print(provjera_realnog_broja(unos))