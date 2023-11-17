BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvive = int(input("Donnez le nombre de convives : "))
fromage = (fromage * nbConvive) / BASE
eau = (eau * nbConvive) / BASE
ail = (ail * nbConvive) / BASE
pain = (pain * nbConvive) / BASE
print("Pour faire une fondue fribourgeoise pour {} personnes, il vous faut :\n- {} gr de fromage\n- {} dl d'eau\n- {} gouse(s) d'ail\n- {} gr de pain".format(nbConvive, fromage, eau, ail, pain))