from Scores import score

class Joueur():
    def __init__(self):
        self.name = self.get_Name()
        self.score_joueur = self.get_Score()
        self.grille_score = score()

    def get_Name(self):
        nom_utilisateur = input("Tapez votre nom")
        if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
            return self.getName()
        else:
            return nom_utilisateur

    def get_Score(self):
        actual_score = self.grille_score.retourner_score(self.name)
        print('Le score actuel de {} est de {}'.format(self.name,
                                                       actual_score))
        return actual_score

    def set_Score(self,new_score):
        self.score_joueur = self.score_joueur + new_score
        self.grille_score.sauvegarder_Score(self.name,self.score_joueur)
        print('Le nouveau score actuel de {} est de {}'.format(self.name,
                                                               self.score_joueur))



