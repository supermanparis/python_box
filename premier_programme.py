# definition de la fonction afficher information personne

def afficher_information_personne (nom,age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")

    if age >= 18:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes mineur.")


# definition de la fonction demander nom

def demander_nom():
    reponse_nom = ""
    while reponse_nom =="":
        reponse_nom = input("quel est votre nom? ")
    return reponse_nom
    


# definition de la fonction 
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " ,Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int
    



'''
# Partie 1 : Demander nom
nom = ""
while nom == "":
    nom = input("Quel est votre nom ? ")
'''

# Partie 2 : Demander age + demander nom  avec l'APPEL des foncions demander_age() et demander_nom() et la definition des variables
nom1 = demander_nom()
nom2 = demander_nom()
age1 = demander_age(nom1)
age2 = demander_age(nom2)

afficher_information_personne (nom1,age1)
afficher_information_personne (nom2,age2)

'''
# Partie 3 : Afficher les infos
print("Vous vous appelez " + nom1 + ", vous avez " + str(age1) + " ans")
print("L'an prochain vous aurez " + str(age1+1) + " ans")

print("Vous vous appelez " + nom2 + ", vous avez " + str(age2) + " ans")
print("L'an prochain vous aurez " + str(age2+1) + " ans")

'''


