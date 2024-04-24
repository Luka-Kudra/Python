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

def pomnozena_matrica(nova_matrica,skalarni_broj):
    for i in range(len(nova_matrica)):
        for j in range(len(nova_matrica)):
            nova_matrica[i][j] *= skalarni_broj
    return nova_matrica

red = int(input("Unesi broj redova matrice: "))
kolona = int(input("Unesi broj kolona matrice: "))
skalarni_broj = int(input("Unesi skalarni broj: "))
print() #pravi samo novi red

matrica = kreiranje_matrice(red,kolona)
print("\nOrginalna matrica:")
for red in matrica:
    print(red)

nova_matrica = pomnozena_matrica(matrica,skalarni_broj)
print("\nMatrica pomnozena sa skalarnim brojem:")
for red in nova_matrica:
    print(red)

