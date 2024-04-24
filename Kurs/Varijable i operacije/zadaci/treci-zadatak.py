sekunde = 34563
sati = sekunde // 3600
minuta = sekunde // 60 - (sati * 60)
sekundi = sekunde % minuta
print(sati, minuta, sekundi)
