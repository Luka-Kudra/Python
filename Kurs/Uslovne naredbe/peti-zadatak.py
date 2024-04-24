import time #ljepse mi izgledao ispis sa malim pauzama

broj1 = input("Prvi broj: ")
broj2 = input("Drugi broj: ")
broj3 = input("Treci broj: ")
time.sleep(0.5)

print(min(broj1,broj2,broj3))
time.sleep(0.5)

if min(broj1,broj2) < min(broj2,broj3):
    print(max(broj1,broj2))
else:
    print(max(broj2,broj3))
time.sleep(0.5)

print(max(broj1,broj2,broj3))



