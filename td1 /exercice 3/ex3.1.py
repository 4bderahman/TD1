
nombre1 = float(input("Entrez le premier nombre: "))
nombre2 = float(input("Entrez le deuxième nombre: "))
nombre3 = float(input("Entrez le troisième nombre: "))


if nombre1 >= nombre2 and nombre1 >= nombre3:
    print("Le plus grand nombre est:", nombre1)
else: 
    if nombre2 >= nombre1 and nombre2 >= nombre3:
        print("Le plus grand nombre est:", nombre2)
    else:
        print("Le plus grand nombre est:", nombre3)

