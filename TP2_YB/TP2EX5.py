nb = int(input("Entrez un nombre entier : "))
signe = ""
parite = ""
if nb > 0:
    signe = "positif"
    if nb % 2 == 0:
        parite = "paire"
    else:
        parite = "impaire"
elif nb < 0:
    signe = "negatif"
    if nb % 2 == 0 :
        parite = "paire"
    else:
        parite =" impaire"
else:
    signe = "zero"
    parite = "pair"
print("le nombre est {} et {}".format(signe, parite))

