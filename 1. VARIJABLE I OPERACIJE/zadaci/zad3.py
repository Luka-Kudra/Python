korisnik_vrijeme = int(input('Vrijeme u sekundama: '))

minute = korisnik_vrijeme // 60
sekunde = korisnik_vrijeme % 60

sati = minute // 60
minute = minute % 60
print(sati, minute , sekunde)