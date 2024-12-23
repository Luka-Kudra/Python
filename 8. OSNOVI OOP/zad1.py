# Kreirati klasu Kalkulator.
# Ova klasa treba da ima dva atributa koji su operandi operacija kalkulatora.
# Operacije koje kalkulator obavlja su osnovne aritmetičke operacije
# i one treba da se implementiraju pomoću metoda klase. 
# Testirati implementaciju instancirajući konkretan objekat klase i pozivajući 
# implementirane metode.

class Kalkulator:
    operand1 = 0
    operand2 = 0

    def saberi(self):
        rezultat = self.operand1 + self.operand2
        return rezultat

    def oduzmi(self):
        rezultat = self.operand1 - self.operand2
        return rezultat

    def pomnozi(self):
        rezultat = self.operand1 * self.operand2
        return rezultat

    def podijeli(self):
        rezultat = self.operand1 / self.operand2
        return rezultat


kalkulator = Kalkulator()

kalkulator.operand1 = int(input("Unesite prvi broj: "))
kalkulator.operand2 = int(input("Unesite drugi broj: "))

print(kalkulator.saberi())
print(kalkulator.oduzmi())
print(kalkulator.pomnozi())
print(kalkulator.podijeli())
