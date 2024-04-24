def provjera_cjelog_broja():
    while True:
        unos = input("Unesi cjeli broj: ")
        if not unos:
            print("Niste unjeli ceo broj")
        elif unos.isdigit() or (unos[0] == '-' and unos[1:].isdigit()):
            return int(unos)
        else:
            print("Niste unjeli ceo broj")