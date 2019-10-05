import os
import pickle
import numpy as np

#########################################################################################################

class Parametre:
    def __init__(self):
        self.Liste_Mots = self.get_Liste_Mots()
        self.Nombre_coups = self.get_Nombre_Coups()

    def get_Liste_Mots(self):
        Liste_Mots = ['Crocodile',
                      'Alligator',
                      'Caiman',
                      'Gavial',
                      'Rhinoceros',
                      'Tigre',
                      'Tamanoir',
                      'Anaconda',
                      'Phacochere',
                      'Zebre',
                      'Girafe',
                      'Hippopotame',
                      'Leopard',
                      'Antilope']
        return Liste_Mots

    def get_Nombre_Coups(self):
        liste_coups = 10
        return liste_coups

#########################################################################################################

class Score:
    def __init__(self):
        self.path = 'C:\\Users\\monne\\source\\repos\\Jeu_Pendu'
        self.name = 'Score_Game'
        self.name_file = name_file = os.path.join(self.path,self.name)

    def charger_Score(self):        
        if os.path.exists(self.name_file):
            with open(self.name_file,"rb") as f:
                depickler = pickle.Unpickler(f)
                try:
                    fichier = depickler.load()
                except:
                    fichier = dict()
        else:
            fichier = dict()
        return fichier

    def sauvegarder_Score(self,name,score):
        fichier_score = self.charger_Score()
        if name in fichier_score:
            fichier_score[name]+=score
        else:
            fichier_score[name]=score
        with open(self.name_file,'wb') as f:
            pickler = pickle.Pickler(f)
            pickler.dump(fichier_score)

    def retourner_Score(self,name):
        fichier_score = self.charger_Score()
        if name in fichier_score:
            return fichier_score[name]
        else:
            return 0

#########################################################################################################

class Joueur():
    def __init__(self):
        self.grille_score = Score()
        self.name = self.get_Name()
        self.score_joueur = self.get_Score()

    def get_Name(self):
        nom_utilisateur = input("Tapez votre nom : ")
        if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
            print('Nom au mauvais format')
            return self.getName()
        else:
            return nom_utilisateur

    def get_Score(self):
        actual_score = self.grille_score.retourner_Score(self.name)
        print('Le score actuel de {} est de {}'.format(self.name,
                                                       actual_score))
        return actual_score

    def set_Score(self,new_score):
        self.score_joueur = self.score_joueur + new_score
        self.grille_score.sauvegarder_Score(self.name,new_score)
        print('Le nouveau score actuel de {} est de {}'.format(self.name,
                                                               self.score_joueur))

#########################################################################################################

class Partie:
    def __init__(self):
        self.parametres = Parametre()
        self.mot = self.choix_mot().lower()
        self.joueur = Joueur()

        self.nombre_coup = self.parametres.get_Nombre_Coups()
        self.mot = self.choix_mot()
        self.grille = ''

        self.liste_positions = list()

    def choix_mot(self):
        grille_mots = self.parametres.get_Liste_Mots()
        nombre_mot = len(grille_mots)
        nombre_hasard = int(np.random.rand(1)[0]*nombre_mot)
        return grille_mots[nombre_hasard].lower()

    def trouve(self,letter,debut,fin):
        if debut > fin:
            return 
        else:
            position = self.mot.find(letter,debut,fin) 
            if position != -1:
                self.liste_positions.append(position)
                self.trouve(letter,position+1,fin)
            else:
                return 

    def verification_reponse(self,reponse):
        if len(reponse)!=1 or not reponse.isalpha():
            return 'Mauvaise saisie - Recommencez !'

        self.trouve(reponse.lower(),0,len(self.mot))
        
        if self.liste_positions:
            for position in self.liste_positions:
                mot = list(self.grille)
                mot[position]=reponse.lower()
                self.grille = ''.join(mot)
         
        self.liste_positions = list()                
        return self.grille

    def verification_gagnant(self):
        return self.grille.find('-') <0
            

    def debuter_partie(self):
        self.grille = '-' * len(self.mot)

        self.jouer_partie()

    def jouer_partie(self):
        print('Début de la partie ! ')
        while(self.nombre_coup>0):
            saisie = input('Tapez une lettre : ')
            print(self.verification_reponse(saisie))
            if self.verification_gagnant():
                print('Bravo, vous avez gagné !!!')
                self.joueur.set_Score(self.nombre_coup)
                return
            self.nombre_coup-=1
        print('Vous avez perdu !!!')
        print('La réponse était : {} '.format(self.mot))
        
        return

#########################################################################################################

partie = Partie()

partie.debuter_partie()


