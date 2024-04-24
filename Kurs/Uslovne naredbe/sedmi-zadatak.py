unos = input("Unesi cjeli broj: ")

def provjera_cjelog_broja(unos):
    if len(unos) <= 0:
        return False
    if unos[0] == '-':
        unos = unos[1:] #ukloni - iz stringa
    if unos.isdigit():
        return True
    else:
        return False
    
print(provjera_cjelog_broja(unos))