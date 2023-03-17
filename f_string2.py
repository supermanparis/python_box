# f string notation


print("**************** ICI AVEC CONCATENATION ****************")

nom = input("Quel est votre prénom?")
age = input("Quel est votre age?")

reponse = "Mon prénom est " + nom + " et j'ai "+ age +" ans."

print(reponse)

print("**************** ICI AVEC F-STRING ****************")



nom1 = input("Quel est votre prénom?")
age1 = input("Quel est votre age?")

reponse1 = (f"Mon prénom est {nom1} et j'ai {age1} ans.")

print(reponse1)