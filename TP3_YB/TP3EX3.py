from random import *
x = randint(0,100)
g = int(input("Deviner le nombre ! :"))
while g!=x:
    if g > x :
        g = int(input("Le nombre est plus petit. Essayer encore :"))
    else:
        g = int(input("Le nombre est plus grand. Essayer encore :"))
print("Bravo ! Vous avez trouvez !")