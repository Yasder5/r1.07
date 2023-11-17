from datetime import *
Annee_courant = datetime.now().year
age = int(input("Donnez votre age :\n"))
annee = Annee_courant - age
print("Votre annez de naissance est : " + str(annee))