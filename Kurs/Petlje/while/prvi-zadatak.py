unos = input("Unesi cjeli broj: ")

def provjera_cjelog_broja(unos):
    if unos[0] == '-':
        unos = unos[1:] #ukloni - iz stringa
    if unos.isdigit():
        return True
    else:
        return False
    
while provjera_cjelog_broja(unos) == False:
    unos = input("Unesi cjeli broj ponovo: ")

