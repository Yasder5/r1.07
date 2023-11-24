import time
n = int(input("Donnez un nombre entier :"))
def boucleWhile(n):
    while n!=0 :
        print(n)
        n-=1
        time.sleep(1)

def boucleFor(n):
    for i in range(n):
        print(n)
        n-=1
        time.sleep(1)

boucleWhile(n)