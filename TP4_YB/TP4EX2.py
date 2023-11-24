# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes qued'étudiants
notes = []
for i in range(nombreEtudiants):
    n = float(input(" Note etudiant {} : ".format(i)))
    if n < 0 or n > 20 :
        print("notz non valide recommencer :")
        nombreEtudiants += 1
    notes.append(n)

for j in range(len(notes)):
    moyenne += notes[j]
moyenne = moyenne/nombreEtudiants
print("Moyenne classe : ", moyenne)
print("Numéro de l’Etudiant |  note  | ecart a la moyenne")
for k in range(nombreEtudiants):
    print("{}                    |  {}   |  {}".format(k, notes[k], (notes[k]- moyenne).__round__(2)))