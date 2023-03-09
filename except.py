'''
nom = input("Quel est votre nom ?")
age = input("Quel est votre age ?")

age_prochain = int(age)+1

print("Vous vous appelez "+ nom + " et vous aurez "+ str(age_prochain) + " ans l'an prochain inch'Allah.")





nom = input("Quel est votre nom ?")
age = input("Quel est votre age ?")

try:
    age_prochain = int(age)+1

except:
    print("ERREUR, Vous devez entrer une valeure numérique pour l'age !")

else:
    print("Vous vous appelez "+ nom + " et vous aurez "+ str(age_prochain) + " ans l'an prochain inch'Allah.")

'''


for i in range (5):
    print(i)
