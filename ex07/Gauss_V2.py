nbr = 1
nbrSomme = 1
nbrInput = int(input ("Quel est votre nombre ? :\n"))
while (nbr < nbrInput) :
  nbr += 1
  nbrSomme += nbr
print (f"Nous allons calculer la somme de tous les nombre de 1 jusqu'à {nbrInput}\nLe résultat est {nbrSomme}")
