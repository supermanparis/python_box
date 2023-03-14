

# test d'un QCM pour apprendre python




reponse = ""


def question_1():
    print("Bonjour, avec ce petit QCM, nous allons tester vos connaissances sur quelques dates clés du football.")
    print("Question 1 : En quelle année le Brésil à t-il gagné sa première coupe du monde??")
    print( "A- 1930")
    print( "B- 1934")
    print( "C- 1970")
    print( "D- 1994")
    print( "E- 1958")

    reponse = input("Choisissez la lettre (en Majuscule) de la réponse de votre choix.")

    if reponse == "E":
        print("Bien joué ! Bonne réponse !")
    elif reponse == "A":
        print("Mauvaise réponse !, l'Uruguay à gagné en 1930 ")
    elif reponse == "B":
        print("Mauvaise réponse !, l'Italie à gagné en 1934 ")
    elif reponse == "C":
        print("Mauvaise réponse !, En 1970 ils'aggissait de la deuxième coupe du Monde du Brésil! ")
    elif reponse == "D":
        print("Mauvaise réponse !, En 1994 ils'aggissait de la troisième coupe du Monde du Brésil!  ")
    else :
        input("Choisissez la lettre (en Majuscule) de la réponse de votre choix.")

question_1()


