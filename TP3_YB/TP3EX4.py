
def boucleWhile(n):
    fact = 1
    while n!=0 :
        fact*=n
        n-=1
    print(fact)

def boucleFor(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact)

p = int(input("Quelle Boucle vous voulez utiliser For (1) ? Ou While (2) ? : "))
n = int(input("Donnez un nombre entier pour la boucle : "))
if p == 1 :
    boucleFor(n)
else:
    boucleWhile(n)