a = float(input("Entrez le coefficient a: "))
b = float(input("Entrez le coefficient b: "))

if a == 0 and b == 0 :
    print("il ya une infinité de solutions pour x")
else :
    if a == 0 and b != 0 :
        print("il ya une infinité de solutions pour x")
    else :
        x = -b / a
        print("la solution est :", x)