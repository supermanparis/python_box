# definition de la fonction afficher information personne

def afficher_information_personne (nom,age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")

# Ajout de differentes conditions elif == 17 ou == 18

    if age == 17:
        print("Vous êtes presque majeur.")
    elif age >=12 and age <18: # ou possible d 'ecrire :     12 <= age <18:
        print("Vous êtes adolescent.")
    elif age < 5:
        print("Vous êtes un bébé.")
    elif age == 18:
        print("Vous êtes tout juste majeur.")
    elif age > 60:
        print("Vous êtes senior.")
    elif age < 10:
        print("Vous êtes enfant.")
    elif age >= 18:
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


# utilisation d'une boucle for pour generer le nom d'une personne

for i in range(0,3):
    nom = "prenom"+ str(i+1) # ici on genere l1 nom avec une concatenation de prenom + str(i+1) pour commencer à"prenom1" sinon "prenomO"
    age = demander_age(nom) # ici on va faire appel a la fonction demander(age) et demander l'age de la variabel générée au dessus :nom
    afficher_information_personne(nom, age) # ici on va faaire appel a la fonction avec pour paramametre le nom et l'age générés au dessus.

'''
# Partie 3 : Afficher les infos
print("Vous vous appelez " + nom1 + ", vous avez " + str(age1) + " ans")
print("L'an prochain vous aurez " + str(age1+1) + " ans")

print("Vous vous appelez " + nom2 + ", vous avez " + str(age2) + " ans")
print("L'an prochain vous aurez " + str(age2+1) + " ans")

'''


