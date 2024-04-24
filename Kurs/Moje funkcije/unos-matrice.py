def provjera_realnog_broja():
    while True:
        unos = input()
        if unos.replace('.', '', 1).isdigit():
            return round(float(unos), 2) 
        elif unos.startswith('-') and unos[1:].replace('.', '', 1).isdigit():
            return round(float(unos), 2)
        else:
            print("Niste unjeli realan broj")
            print("Pokusajte ponovo:",end=" ")

def kreiranje_matrice(red,kolona):
    matrica = []
    for i in range(red):
        red = []
        for j in range(kolona):
            print("Unesi element za",i+1,"red i",j+1,"kolonu:",end = " ")
            element = provjera_realnog_broja()
            red.append(element)
        matrica.append(red)
    return matrica

red = int(input("Unesi broj redova matrice: "))
kolona = int(input("Unesi broj kolona matrice: "))
print() #pravi samo novi red

matrica = kreiranje_matrice(red,kolona)