import numpy as np

def choix_hasard(choix):
    nombre_hasard = np.random.rand(1)[0]
    return int(choix*nombre_hasard)

nb_essai = 100000

nombre_reussite_methode1 = list()
nombre_reussite_methode2 = list()

plateau_jeu = np.zeros(3)
plateau_jeu[choix_hasard(3)] = 1

for choix in range(1,nb_essai):
    choix_joueur = choix_hasard(3)
    if plateau_jeu[choix_joueur] == 1:
        nombre_reussite_methode1.append(1)
    else:
        nombre_reussite_methode1.append(0)

for choix in range(1,nb_essai):
    new_plateau_jeu = np.zeros(2)
    if plateau_jeu[0]==1:
        new_plateau_jeu[0]=1
    else:
        new_plateau_jeu[1]=1
    choix_joueur = choix_hasard(2)
    if new_plateau_jeu[choix_joueur] == 1:
        nombre_reussite_methode2.append(1)
    else:
        nombre_reussite_methode2.append(0)

print('-'*30)

result_1 = sum(nombre_reussite_methode1)/len(nombre_reussite_methode1)
result_2 = sum(nombre_reussite_methode2)/len(nombre_reussite_methode2)

result= [result_1,result_2]

for num,res in enumerate(result):
    print('Probabilité de succès de la méthode n° {} : {:.2%}'.format(num+1,res))

print('-'*30)

choix_joueur = np.random.randint(1,4,size=nb_essai)
choix_porte = np.random.randint(1,4,size=nb_essai)

succes_strategie_premier_choix = (choix_joueur == choix_porte)*1
succes_strategie_second_choix = (choix_joueur != choix_porte)*1

#print(choix_joueur)
#print(choix_porte)
#print(succes_strategie_premier_choix)
#print(succes_strategie_second_choix)

result_1 = np.mean(succes_strategie_premier_choix)
result_2 = np.mean(succes_strategie_second_choix)

result= [result_1,result_2]

for num,res in enumerate(result):
    print('Probabilité de succès de la méthode n° {} : {:.2%} '.format(num+1,res))

print('-'*30)

