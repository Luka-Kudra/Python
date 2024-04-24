unos = input("Unesi svoje godine: ")
if unos.isdigit():
    if (int(unos)>18):
        print("Pristup dozvoljen")
    else:
        print("Pristup odbijen")
else:
    print("Pogrešan unos")