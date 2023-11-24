def sommeN(n):
    somme = 0
    for i in range(n+1):
        somme += i
    print("La somme de {} entier est {}".format(n,somme))

def boucleAttente():
    g = int(input("Donnez un nombre entier :"))
    while g != 100:
        g = int(input("Donnez un autre nombre entier :"))
    print("C'est bon vous avez trouvez")

def LectureDeValeur():
    infDix = 0
    EntreDixEtQuinze = 0
    supQuinze = 0
    liste = []
    for i in range(10):
        n = int(input("Donnez un nombre entier entre 0 et 20 : "))
        if 0 > n or n > 20:
            print("Recommencer !")
            LectureDeValeur()
        liste.append(n)
        if n < 10:
            infDix += 1
        elif n < 15:
            EntreDixEtQuinze += 1
        else :
            supQuinze += 1
    print("Pour la liste {} le nb de chiffre inf à 10 est {}, le nb de chiffres sup ou égale 10 dix et Inf à 15 quinze est {}, le nb de chiffre sup à 15 est {}".format(liste, infDix, EntreDixEtQuinze, supQuinze))

def plusGrandNbN():
    n = int(input("Donnez un entier N : "))
    somme = 0
    for i in range(n):
        somme += i
        if somme > n:
            print("grand nombre N tel que la somme de zero à lui meme soit inferieur ou égal à N est ", i-1)
            return 0
LectureDeValeur()