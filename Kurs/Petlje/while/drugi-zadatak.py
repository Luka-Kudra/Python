unos = input("Unesi prirodan broj: ")

if unos.isdigit():
    unos = int(unos)
else: 
    print("Broj nije prirodan")

faktorijel_brojac = unos
faktorijel = 1
suma = unos

while faktorijel_brojac >= 1:
    faktorijel *= faktorijel_brojac 
    faktorijel_brojac -= 1
    suma += faktorijel_brojac
print("Faktoriel:",faktorijel)
print("Suma",suma)
