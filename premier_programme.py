#on distingue 3 Parties :

# Partie 1 : Demander nom
nom = ""
while nom == "":
    nom = input("Quel est votre nom ? ")
# Partie 2 : Demander age
age = 0
while age == 0:
    age_str = input("Quel est votre age ? ")
    try:
        age = int(age_str)
    except ValueError:
        print("ERREUR: Vous devez rentrer un nombre pour l'age")
# Partie 3 : Afficher les infos
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age+1) + " ans")



