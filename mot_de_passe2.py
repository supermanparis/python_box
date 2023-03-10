#comptabilisation du nombre de tentatives

mot_de_pass = ""
tentative = 0

while not mot_de_pass == "mksdcndcqklsn":
    mot_de_pass = input("Quel est votre mot de passe? ")
    tentative = tentative + 1
    print("Tentative N°: "+ str(tentative))

print("Accès Autorisé, Bienvenue !, vous avez réussit au bout de la tenative numéro " + str(tentative))