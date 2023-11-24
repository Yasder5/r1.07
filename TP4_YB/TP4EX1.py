table = []
n = float(input("Vous cherchez la table de multiplication de quel nombre ? : "))
for i in range(10):
    table.append(n*i)
for j in range(10):
    print("{} * {} = {}".format(n, j, table[j].__round__(1)))