# expression lambda vs fonction


print("#############################")
print("##############   ICI AVEC LA DEFINITION D'UNE FONCTION ###############")
print("#############################")


def ma_fonction(x,y):
    return x**2 +y

ma_fonction(2,5)

resultat = ma_fonction(2,5)

print(resultat)

print("#############################")
print("##############   ICI AVEC LA MEME FONCTION ECRIT EN EXPRESSION FONCTION LAMBDA SUR UNE LIGNE ###############")
print("#############################")

ma_fonction2 = lambda x,y: x**2 +y

print(ma_fonction(2,5))