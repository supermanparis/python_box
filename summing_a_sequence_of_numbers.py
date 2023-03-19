# Summing a sequence of numbers
# La fonction sum() ne fonctionne qu’avec des valeurs numériques!
# Si vous essayez de l’utiliser avec un type non numérique, vous obtiendrez une erreur.

l = range(3,10,2)   # exemple range avec trois paramètres, on lui donne un start qui ici est 3,  un stop qui ici est 10, et un step qui ici est 2. 
#Ainsi, range(3, 10, 2) nous renvoie : [3, 5, 7, 9].


sum(l) # la somme de l pour un range de (3,10,2) sera de 24 car 3+5+7+9 = 24

print(sum(l))


# En appelant range avec un seul paramètre, on lui donne un stop. Ainsi, range(3) nous renvoie : [0, 1, 2].