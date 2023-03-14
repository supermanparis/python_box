# Utilisation de f string

def demander_infos():
    nom = input("Quel est votre nom?")
    prenom = input("Quel est votre prenom?")
    age = input("Quel est votre age?")
    
    print(f"Vous vous appelez {nom} {prenom}.") # ici f string
    print(f"Vous avez {age} ans.") # ici utilisation d'une f string

    print("Vous vous appelez %s." %nom) # ici une autre façon
    print("Vous avez %s" %age,"printemps.")
    print("Vous vous appelez %s %s."%(nom, prenom)) # ici f string

    print("""
    Vous 
                mettez 
                        ce que 
            vous voulez
    
    """) # ici exemple d'un print sur plusieurs lignes.

    print ("hello", 20, 1.80, True) # ici test pour print sans concatenation maisavec une virgule.


demander_infos()