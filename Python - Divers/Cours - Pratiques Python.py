###############################################################

liste = ['croco','gavial','alligator','caiman']

for indice in range(0, len(liste)):
    print('liste[%d] = %r'%(indice, liste[indice]))

for indice, valeur in enumerate(liste):
    print("liste[{}] = {}".format(indice,valeur))

# ou sinon, comme enumerate renvoie une liste de tuples :
for indval in enumerate(liste):
    # print %F"liste[{indval[0]}] = {indval[1]}"
    print("liste[{}] = {}".format(indval[0],indval[1]))

###############################################################

def syracuse(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        yield n

for n in syracuse(3):
    print(n)

###############################################################

def compteur(x):
    n = 0
    while n <= x:
        v = (yield n)  # Prenez l'habitude de mettre des parenthèses
                       # autour d'une instruction yield ;)
        if v is not None:
            n = v
        else:
            n += 1

gen = compteur(25)

for i in gen:
    print(i)
    # Si on en est à 15, on veut passer directement à 18
    if i == 15:
        gen.send(18)

###############################################################

new_animal = [animal for animal in liste if animal[0]=='c']

print(new_animal)

###############################################################

gen = (elem + 's' for elem in liste)

for elem in gen: 
    print(elem)

###############################################################

for animal,indice in zip(liste,range(0,len(liste))):
    print('The wild {} is number {}'.format(animal,indice))

###############################################################

#from itertools import map

pair = lambda n: n % 2 == 0
carre = lambda n: n ** 2

map(carre, range(10)) # Renvoie un générateur

for elem in list(map(pair, range(10))): 
    print(elem)

###############################################################

with open('fichier', 'w') as f:
    f.read()

###############################################################






