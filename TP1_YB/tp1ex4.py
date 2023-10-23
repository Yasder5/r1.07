minute = int(input("donner le nombre de minute depuis le debut du mois "))
heure = minute / 60
jour = heure /24
heure = heure - (jour * 24)
print(f"il c'est passer {jour} jours et {heure} heures depuis le début du mois")
