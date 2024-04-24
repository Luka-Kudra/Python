prvi_broj = input("Prvi broj: ")
drugi_broj = input("Drugi broj: ")
prvi_broj = int(prvi_broj)
drugi_broj = int(drugi_broj)

sabiranje = prvi_broj + drugi_broj
oduzimanje = prvi_broj - drugi_broj
mnozenje = prvi_broj * drugi_broj
djeljenje = prvi_broj / drugi_broj
ostatak = prvi_broj % drugi_broj
stepenovanje = prvi_broj ** drugi_broj
cjelobrojno_djeljenje = prvi_broj // drugi_broj

print("Zbir: ",sabiranje)
print("Razlika: ",oduzimanje)
print("Proizvod: ",mnozenje)
print("Kolicnik: ",djeljenje)
print("Ostatak: ",ostatak)
print("Stepen: ",stepenovanje)
print("Rezultat cjelobrojnog djeljenja: ",cjelobrojno_djeljenje)