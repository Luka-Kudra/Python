x = float(input("Unesi x: "))
y = float(input("Unesi y: "))
if (x>0 and y>0):
    print("Tacka se nalazi u prvom kvadrantu")
elif (x<0 and y>0):
    print("Tacka se nalazi u drugom kvadrantu")
elif (x<0 and y<0):
    print("Tacka se nalazi u trecem kvadrantu")
elif (x>0 and y<0):
    print("Tacka se nalazi u cetvrtom kvadrantu")
else :
    print("Tacka ne pripada kvadrantu")