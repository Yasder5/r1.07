x = int(input("Entrez x : "))
y = int(input("Entrez y : "))

print("Avant permutation :\nx : {} \ny : {}".format(x,y))

x , y = y , x
print("Après permutation :\nx : {} \ny : {}".format(x,y))
