# Removing useless characters on the end/start/both of your string

name = '//George//'
name.strip('/')  # ici strip tous les '/'
# output : >>'George'

#############

name.rstrip('/') # ici rstrip , donc tous les '/' qui sont a right, a droite
# output : >>'//George'

#############

name.lstrip('/') # ici lstrip , donc tous les '/' qui sont a left, a gauche
# output : >>'George//'