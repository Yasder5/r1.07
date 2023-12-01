nMax = 10
v1 = []
v2 = []
n = int(input("compris entre 1 et nMax (10) "))
if n < 1 or n > nMax:
    while n < 1 or n > nMax:
        n = int(input("compris entre 1 et nMax (10) "))
print("Saisie du premier vec ")
for i in range(n):
    v1.append(int(input("v1 {} ".format(i))))
print("Saisie du deuxieme vec ")
for j in range(n):
    v2.append(int(input("v2 {} ".format(j))))


produitScalaire = 0
for i in range(n):
    produitScalaire += v1[i] * v2[i]

print("Le produit sclaire de v1 et v2 vaut ", produitScalaire)
