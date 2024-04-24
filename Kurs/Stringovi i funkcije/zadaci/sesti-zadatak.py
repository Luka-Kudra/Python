import math
tacka1_x = int(input("x1: "))
tacka1_y = int(input("y1: "))
tacka2_x = int(input("x2: "))
tacka2_y = int(input("y2: "))
tacka3_x = int(input("x3: "))
tacka3_y = int(input("y3: "))

def udaljenost(prvi_x,prvi_y,drugi_x,drugi_y):
    rastojanje = round(math.sqrt((prvi_x - drugi_x)**2 + (prvi_y - drugi_y)**2),2)
    return rastojanje

def obim_trougla(tacka1_x,tacka1_y,tacka2_x,tacka2_y,tacka3_x,tacka3_y):
    obim = udaljenost(tacka1_x,tacka1_y,tacka2_x,tacka2_y) + udaljenost(tacka2_x,tacka2_y,tacka3_x,tacka3_y) + udaljenost(tacka3_x,tacka3_y,tacka1_x,tacka1_y)  
    return obim   
     
print("Obim trougla je ≈",obim_trougla(tacka1_x,tacka1_y,tacka2_x,tacka2_y,tacka3_x,tacka3_y))