import random

from Parametres import Parametre
from Joueurs import Joueur

class Partie:
    def __init__():
        self.mot = self.choix_mot()
        self.parametres = Parametre()
        self.joueur = Joueur()

        self.nombre_coup = self.parametres.get_Nombre_Coups()
        self.mot = self.choix_mot()
        self.grille = ''

    def choix_mot(self):
        grille_mots = self.parametres.get_Liste_Mots()
        nombre_mot = len(grille_mots)
        nombre_hasard = random.rand(1,nombre_mot)
        return grille_mots[nombre_hasard]

    def verication_reponse(self,reponse):
        if len(reponse)!=1 or not reponse.isalpha():
            return 'Mauvaise saisie - Recommencez !'
        else:
            if reponse in self.mot:
                position = self.mot.find(reponse)
                self.grille[position]=reponse
            return self.grille

    def verification_gagnant(self):
        return self.grille.find('-') <0
            

    def debuter_partie(self):
        self.joueur.get_Name()
        self.joueur.get_Score()
        self.grille = '-' * self.nombre_coup

        self.joueur_Partie()

    def joueur_partie(self):
        print('Début de la partie')
        while(self.nombre_coup>0):
            saisie = input('Tapez une lettre')
            print(self.verication_reponse())
            if self.verification_gagnant():
                print('Bravo, vous avez gagné !!!')
                self.joueur.set_Score(self.nombre_coup)
                return
            self.nombre_coup-=1
        print('Vous avez perdu !!!')
        
        return





