a = int(input("Unesi prvu stranicu trougla: "))
b = int(input("Unesi drugu stranicu trougla: "))
c = int(input("Unesi trecu stranicu trougla: "))
if a + b > c and a + c > b and c + b > a:
    if (a == b == c):
        print("Trougao je jednakostraničan")
    elif (a == b or a == c or b ==c):
        print("Trougao je jednakokrak")
    else:
        print("Trougao je raznostraničan")
else:
    print("Od ovih stranica nije moguće napraviti trougao")
