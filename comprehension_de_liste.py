# exemple de liste avec selection des nombres pairs grace à compréhension de liste ("list comprehesion")


print("")
print("************************************************")
print("ICI AVEC BOUCLE FOR")
print("************************************************")
print("")

liste_nombres = [9,23, 789, 9876, 2873, 76, 112, 9289, 23,16,20,22, 10, 234]
liste_nombres_pairs = [] # initialisation de la variable contenant une liste vide pour trier les nombres pairs

for i in liste_nombres:
    if i%2 == 0: # ici si i%2=0 cela veut dire que le nombre est pair
        liste_nombres_pairs.append(i) # ajoute le à la liste grâce à la méthode append
print(liste_nombres_pairs) # ressort du programme et imprime le resultat du tri


print("")
print("************************************************")
print("ICI AVEC COMPREHENSION DE LISTE :")
print("************************************************")
print("")

liste_nombres_pairs_cdl = []

liste_nombres_pairs_cdl = [x for x in liste_nombres if x%2 == 0 ]
print(liste_nombres_pairs_cdl)


print("")
print("************************************************")
print("ICI t2 AVEC COMPREHENSION DE LISTE avec +2 sur le x : ")
print("************************************************")
print("")


liste_nombres_pairs_cdl_t2 = []

liste_nombres_pairs_cdl = [x+2 for x in liste_nombres if x%2 == 0 ]
print(liste_nombres_pairs_cdl)


print("")
print("************************************************")
print("ICI t3 AVEC COMPREHENSION DE LISTE avec carré (**2) sur le x : ")
print("************************************************")
print("")

liste_nombres_pairs_cdl_t3 = []

liste_nombres_pairs_cdl = [x**2 for x in liste_nombres if x%2 == 0 ]
print(liste_nombres_pairs_cdl)


print("")
print("************************************************")
print("ICI AVEC COMPREHENSION DE LISTE  pour trier les nombres impairs :")
print("************************************************")
print("")

liste_nombres_impairs_cdl = []

liste_nombres_pairs_cdl = [x**2 for x in liste_nombres if not x%2 == 0 ]
print(liste_nombres_pairs_cdl)