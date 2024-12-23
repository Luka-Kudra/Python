#  Fabrika za proizvodnju jaja pakuje jaja u kutije po 12 komada, a potom se 6 
# takvih kutija pakuje u jedan paket. Prilikom primanja narudžbe,
# kupac naručuje ukupan broj komada, a zatim se treba odrediti broj paketa i kutija 
# potreban da se upakuju sva naručena jaja. Napraviti program koji vrši takav 
# proračun.

br_jaja = input("Ukupan broj jaja: ")

if (not br_jaja.isdigit()):
    print("POGRESAN UNOS!")
    exit()

br_jaja = int(br_jaja)

br_kutija = 0
br_paketa = 0

br_kutija = br_jaja // 12
if (br_jaja % 12 != 0):
    br_kutija += 1

br_paketa = br_kutija // 6
if (br_kutija % 6 != 0):
    br_paketa += 1

print("broj paketa:", br_paketa)
print("broj kutija:", br_kutija)