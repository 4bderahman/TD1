note = float(input("Entrez la note de l'étudiant: "))


if note < 6:
    print("L'étudiant est non concerné par le rattrapage.")
elif note < 12:
    print("L'étudiant peut passer le rattrapage.")
else:
    print("L'étudiant valide la matière.")