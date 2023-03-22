# Merging/Upserting two dictionaries
# fusionner / mettra à jour 2 dictionnaires

a = {'a':1, 'b':1}
b = {'b':2,'c':1}
a.update(b)
print(a)

# output:
# >>{'a':1, 'b':2, 'c':1}
