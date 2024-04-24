def provjera_realnog_broja():
    while True:
        unos = input("Unesi realan broj: ")
        if unos.replace('.', '', 1).isdigit():
            return round(float(unos), 2)
        elif unos.startswith('-') and unos[1:].replace('.', '', 1).isdigit():
            return round(float(unos), 2)
        else:
            print("Niste unjeli realan broj")

