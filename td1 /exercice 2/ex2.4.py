age = int(input("entrer l‘age de l‘enfant:"))

if age >= 6 and age <= 7:
    print("Poussin")
else:
    if age >= 8 and age <= 9:
        print("Pupille")
    else:
        if age >= 10 and age <= 11:
            print("Minime")
        else:
            if age >= 12:
                print("Cadet")