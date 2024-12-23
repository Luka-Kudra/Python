from math import sqrt


def udaljenost_tacaka(tacka1_x, tacka1_y, tacka2_x, tacka2_y):
    return sqrt((tacka1_x - tacka2_x)**2 + (tacka1_y - tacka2_y)**2)


def obim_trougla(tacka1_x, tacka1_y, tacka2_x, tacka2_y, tacka3_x, tacka3_y):
    AB = udaljenost_tacaka(tacka1_x, tacka1_y, tacka2_x, tacka2_y)
    BC = udaljenost_tacaka(tacka2_x, tacka2_y, tacka3_x, tacka3_y)
    AC = udaljenost_tacaka(tacka1_x, tacka1_y, tacka3_x, tacka3_y)
    return AB + BC + AC


tacka1_x = int(input("Tacka 1, koordinata x? "))
tacka1_y = int(input("Tacka 1, koordinata y? "))

tacka2_x = int(input("Tacka 2, koordinata x? "))
tacka2_y = int(input("Tacka 2, koordinata y? "))

tacka3_x = int(input("Tacka 3, koordinata x? "))
tacka3_y = int(input("Tacka 3, koordinata y? "))

print("Obim trougla konstruisanog nad tim tackama:", obim_trougla(tacka1_x, tacka1_y, tacka2_x, tacka2_y, tacka3_x, tacka3_y))