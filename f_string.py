# Utilisation de f string

def demander_infos():
    nom = input("Quel est votre nom?")
    prenom = input("Quel est votre prenom?")
    age = input("Quel est votre age?")
    
    print(f"Vous vous appelez {nom} {prenom}.") # ici f string
    print(f"Vous avez {age} ans.") # ici utilisation d'une f string

    print("Vous vous appelez %s." %nom) # ici une autre façon
    print(f"Vous avez %s" %age,"printemps.")

demander_infos()