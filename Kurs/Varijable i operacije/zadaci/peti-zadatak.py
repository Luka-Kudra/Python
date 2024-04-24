import math
str_kvadrata = 5
str1_pravougaonika = 3
str2_pravougaonika = 5
poluprecnik_kruga = 3

pov_kvadrata = str_kvadrata ** 2
obim_kvadrata = str_kvadrata * 4
pov_pravougaonika = str1_pravougaonika * str2_pravougaonika
obim_pravougaonika = str1_pravougaonika * 2 + str2_pravougaonika*2
pov_kruga = (poluprecnik_kruga ** 2) * math.pi
obim_kruga = 2 * poluprecnik_kruga * math.pi

print("Kvadrat \nP =",pov_kvadrata,", O =",obim_kvadrata,"\n")
print("Pravougaonik \nP =",pov_pravougaonika,", O =",obim_pravougaonika,"\n")
print("Krug \nP =",pov_kruga,", O =",obim_kruga,"\n")