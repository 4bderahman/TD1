cds = int(input("Entrez le nombre de CDs à acheter: "))

if cds < 10:
    prix = 5
elif cds <= 20:
    prix = 4
else:
    prix = 3

total = cds * prix
print("Le prix total à payer est: ", total, "DH")
