# exemple de liste avec selection des nombres pairs grace à une boucle for
# tests des differents tris selon le l'identation de la dernière ligne de code qui print la liste


print("")
print("************************************************")
print("************************************************")
print("")

liste_nombres = [9,23, 789, 9876, 2873, 76, 112, 9289, 23,16,20,22, 10, 234]
liste_nombres_pairs = [] # initialisation de la variable contenant une liste vide
liste_nombres_pairs1 = []
liste_nombres_pairs2 = []

for i in liste_nombres:
    if i%2 == 0: # ici si i%2=0 cela veut dire que le nombre est pair
        liste_nombres_pairs.append(i) # ajoute le à la liste grâce à la méthode append
print(liste_nombres_pairs) # ressort du programme et imprime le resultat du tri


print("")
print("************************************************")
print("************************************************")
print("")


for i in liste_nombres:
    if i%2 == 0: # ici si i%2=0 cela veut dire que le nombre est pair
        liste_nombres_pairs1.append(i) # ajoute le à la liste grâce à la méthode append
    print(liste_nombres_pairs1) # ressort du programme et imprime le resultat du tri


print("")
print("************************************************")
print("************************************************")
print("")

for i in liste_nombres:
    if i%2 == 0: # ici si i%2=0 cela veut dire que le nombre est pair
        liste_nombres_pairs2.append(i) # ajoute le à la liste grâce à la méthode append
        print(liste_nombres_pairs2) # ressort du programme et imprime le resultat du tri
