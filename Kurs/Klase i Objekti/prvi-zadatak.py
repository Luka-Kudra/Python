class Kalkulator:
    operand1 = 0
    operand2 = 0
    
    def sabiranje(self):
        zbir = self.operand1 + self.operand2
        print(zbir)
    
    def oduzimanje(self):
        razlika = self.operand1 - self.operand2
        print(razlika)

    def mnozenje(self):
        proizvod = self.operand1 * self.operand2
        print(proizvod)

    def djeljenje(self):
        if self.operand2 == 0:
            print("Nije moguće djeljenje sa nulom")
        else:
            kolicnik = self.operand1 / self.operand2
            print(kolicnik)

def provjera_cjelog_broja():
    while True:
        unos = input("Unesi cjeli broj: ")
        if not unos:
            print("Niste uneli ceo broj")
        elif unos.isdigit() or (unos[0] == '-' and unos[1:].isdigit()):
            return int(unos)
        else:
            print("Niste uneli ceo broj")

kalkulator = Kalkulator()
kalkulator.operand1 = provjera_cjelog_broja()
kalkulator.operand2 = provjera_cjelog_broja()
kalkulator.sabiranje()
kalkulator.oduzimanje()
kalkulator.mnozenje()
kalkulator.djeljenje()

