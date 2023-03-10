#comptabilisation du nombre de tentatives + ajout de if et else

mot_de_pass = ""
tentative = 0

while not mot_de_pass == "mksdcndcqklsn":
    mot_de_pass = input("Quel est votre mot de passe? ")
    tentative = tentative + 1

    if not mot_de_pass == "mksdcndcqklsn":
        print("La tentative N°: "+ str(tentative) + " est incorrect!")
    else :
        print("Accès Autorisé, Bienvenue !, vous avez réussit au bout de la tenative numéro " + str(tentative))


